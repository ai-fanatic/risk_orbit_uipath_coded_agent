from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import START, StateGraph, END
from uipath_langchain.chat import UiPathChat
from pydantic import BaseModel
from uipath_langchain.chat.models import UiPathAzureChatOpenAI
from uipath import UiPath
from typing import List
import os


# Resolve folder key from folder path BEFORE initializing SDK
# The ECS API requires the folder_key (UUID) in X-UiPath-FolderKey header
FOLDER_PATH = os.getenv("UIPATH_FOLDER_PATH", "Agents")
print(f"🔑 Resolving folder key for: {FOLDER_PATH}")

# Create temporary SDK just for folder resolution
temp_sdk = UiPath()
folder_key = temp_sdk.folders.retrieve_key(folder_path=FOLDER_PATH)

if not folder_key:
    raise ValueError(f"❌ Failed to resolve folder key for folder path: {FOLDER_PATH}. Please verify the folder exists in Orchestrator.")

print(f"✅ Folder key resolved: {folder_key}")

# Set the folder key as an environment variable so the SDK uses it by default
os.environ["UIPATH_FOLDER_KEY"] = folder_key
print(f"📌 Set UIPATH_FOLDER_KEY environment variable")

# Initialize UiPath SDK (it should now use the UIPATH_FOLDER_KEY from environment)
sdk = UiPath()


class GraphState(BaseModel):
    topic: str
    retrieved_context: List[str] = []


class GraphOutput(BaseModel):
    report: str
    validation_status: str
    citations: List[str]


async def retrieve_context(state: GraphState) -> dict:
    """Retrieve relevant tariff and trade policy documents"""
    print(f"🔍 Retrieving context for: {state.topic}")
    
    # WORKAROUND for SDK bug: Make direct HTTP request with proper headers
    # The SDK's context_grounding.search_async doesn't set X-UiPath-FolderKey header
    
    # Get the index to retrieve its ID
    index = await sdk.context_grounding.retrieve_async(
        name="policy-index",
        folder_key=folder_key
    )
    
    print(f"📋 Index ID: {index.id}")
    
    # Make direct API request with proper headers
    # Based on SDK source code - the payload is NESTED:
    search_payload = {
        "query": {
            "query": state.topic,
            "numberOfResults": 10
        },
        "schema": {
            "name": "policy-index"
        }
    }
    
    # Use the SDK's API client to make the request with proper headers
    response = await sdk.api_client.request_async(
        method="POST",
        url=f"ecs_/v1/search",
        json=search_payload,
        headers={"X-UiPath-FolderKey": folder_key}  # Manually add the required header
    )
    
    # Parse the response - it's a list of document results
    results = response.json() if hasattr(response, 'json') else response
    
    # Extract content and metadata from retrieved documents
    context_list = []
    if isinstance(results, list):
        for i, result in enumerate(results):
            # ECS API returns results with 'id', 'reference', 'score', 'text', 'metadata' fields
            if isinstance(result, dict):
                # Extract the actual document text
                text = result.get('text', '')
                score = result.get('score', 0)
                metadata = result.get('metadata', {})
                source_file = metadata.get('source', metadata.get('fileName', f"Document {i+1}"))
                
                if text:  # Only add if there's actual text content
                    context_list.append(f"Source: {source_file} (Score: {score:.2f})\nContent: {text}")
                else:
                    # Fallback if text field is missing
                    ref = result.get('reference', 'No reference')
                    context_list.append(f"Source: {source_file}\nReference: {ref}")
            else:
                # Handle object responses
                text = result.text if hasattr(result, 'text') else str(result)
                source = result.metadata.get('source', 'Unknown') if hasattr(result, 'metadata') else 'Unknown'
                context_list.append(f"Source: {source}\nContent: {text}")
    
    print(f"✅ Retrieved {len(context_list)} relevant documents from index: {index.name}")
    
    return {"retrieved_context": context_list}


async def generate_report(state: GraphState) -> GraphOutput:
    """Generate tariff and trade validation report with context grounding"""
    
    llm = UiPathAzureChatOpenAI(
        model="gpt-4o-2024-08-06",
        temperature=0,
        max_tokens=4000,
        timeout=30,
        max_retries=2,
    )
    
    # Prepare context from retrieved documents
    context_text = "\n\n---\n\n".join(state.retrieved_context) if state.retrieved_context else "No relevant context found."
    
    # Enhanced system prompt for tariff and trade AI agent
    # Based on actual document structure: tradepolicy.txt and tariffpolicy.txt
    system_prompt = """You are an expert Global Tariff and Trade Policy Validation AI Agent specializing in international trade regulations, tariff classifications, and compliance analysis.

## Your Core Responsibilities:

1. **EXTRACT STRUCTURED DATA** from policy documents:
   - **Country/Region**: Identify the specific country or regional grouping (e.g., Indonesia, GCC, EU, Vietnam)
   - **Policy Identifier**: Extract regulation numbers, circulars, decrees (e.g., "MoF Regulation No. 115/2025", "Circular 31/2025")
   - **HS Codes**: Harmonized System codes (e.g., HS 8411, 8414, 8537, 8502.31)
   - **Tariff Rates**: Previous rate → New rate (e.g., "5% → 7%", "0% → 8%")
   - **Effective Dates**: When the policy becomes active (e.g., "November 10, 2025", "December 1, 2025")
   - **Product Categories**: Equipment types (e.g., gas turbines, solar inverters, hydraulic pumps, wind turbine blades)
   - **Compliance Requirements**: Certifications, documentation, pre-registration needs

2. **CALCULATE RISK INDICES**:
   - **Tariff Risk Index (TRI)**: 0-100 scale
     * > 70 = High uncertainty/volatility
     * 40-70 = Moderate watchlist
     * < 40 = Stable
   - **Trade Policy Risk Index (TPRI)**: Based on policy complexity and compliance burden

3. **PROVIDE ACTIONABLE INSIGHTS**:
   - Identify favorable vs. unfavorable tariff changes
   - Highlight zero-duty exemptions and concessions
   - Flag compliance requirements (certificates, digital portals, environmental fees)
   - Warn about safeguard duties, anti-dumping measures, or surcharges
   - Recommend sourcing alternatives if applicable

## Document Structure Awareness:

The policy documents contain:
- **Regional Sections**: Asia-Pacific, Middle East & GCC, Europe & Trans-Atlantic, Africa & Latin America
- **Country-Specific Updates**: Each with regulation numbers, effective dates, and detailed tariff changes
- **HS Code Mappings**: Specific product classifications and their tariff rates
- **Analytical Summaries**: Risk assessments and trend analysis

## Output Format:

For each query, provide:
1. **Executive Summary**: Brief overview of relevant findings
2. **Country/Region Analysis**: Specific regulations affecting the query
3. **Tariff Details**: Exact rates, changes, and effective dates
4. **HS Code Classification**: Relevant product codes
5. **Compliance Requirements**: Documentation, certifications, or registration needs
6. **Risk Assessment**: TRI/TPRI scores and risk level
7. **Recommendations**: Actionable guidance for trade compliance officers
8. **Citations**: Specific document sources (with section/page references when available)

## Critical Instructions:

- **ONLY use information from the provided context documents**
- If specific information is not found, clearly state: "This information is not available in the current policy documents"
- Always cite source documents (e.g., "According to tariffpolicy.txt Section 2" or "As per tradepolicy.txt Section A")
- Use precise HS codes, dates, and percentages from the documents
- Identify patterns across regions (e.g., rising protectionism, green energy incentives)
- Highlight time-sensitive information (effective dates, sunset reviews)

## Context Documents:
{context}

---

Now analyze the following query and provide a comprehensive, structured validation report:"""
    
    formatted_prompt = system_prompt.format(context=context_text)
    
    output = await llm.ainvoke(
        [SystemMessage(formatted_prompt), HumanMessage(state.topic)]
    )
    
    # Extract citations from retrieved context
    citations = [doc.split("Source: ")[1].split("\n")[0] if "Source: " in doc else "Unknown" 
                 for doc in state.retrieved_context]
    
    # Determine validation status based on response
    validation_status = "VERIFIED" if state.retrieved_context else "UNVERIFIED - No supporting documents found"
    
    return GraphOutput(
        report=output.content,
        validation_status=validation_status,
        citations=citations
    )


builder = StateGraph(GraphState, output=GraphOutput)

# Add nodes for retrieval and report generation
builder.add_node("retrieve_context", retrieve_context)
builder.add_node("generate_report", generate_report)

# Define the workflow: retrieve context first, then generate report
builder.add_edge(START, "retrieve_context")
builder.add_edge("retrieve_context", "generate_report")
builder.add_edge("generate_report", END)

graph = builder.compile()
