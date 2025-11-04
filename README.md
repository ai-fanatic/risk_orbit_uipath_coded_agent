# Risk Orbit Agent - Tariff and Trade Specialist

A UiPath coded agent that automates tariff and trade policy validation for global supply chain risk assessment. This agent is part of the **Risk Orbit** multi-agent framework, providing intelligent analysis of trade regulations, tariff rates, and compliance requirements to enable data-driven decision-making for equipment shipments.

## Overview

**Risk Orbit Agent** is a multi-agent framework built using UiPath coded agents that addresses the constant uncertainty facing global supply chains: tariff swings, port congestion, geopolitical instability, and shifting trade policies. The framework automates end-to-end risk evaluation for every equipment shipment by collecting supplier data, analyzing logistics timelines, assessing geopolitical conditions, and validating trade and tariff updates.

### The Problem

Global supply chain teams face significant challenges:
- **Fragmented Data**: Information scattered across ERPs, government policy databases, and news sources
- **Manual Research**: Trade compliance analysis taking hours or even days
- **Uncertainty**: Constant changes in tariffs, trade policies, and geopolitical conditions
- **Decision Delays**: Lack of timely, actionable insights for logistics and procurement teams

### The Solution

Risk Orbit brings all data sources together in an automated, intelligent workflow that:
- Triggers from email inquiries
- Collects data from multiple APIs (equipment, supplier, scheduler)
- Analyzes geopolitical conditions via news APIs and MCP integrations
- Validates trade and tariff policies using Context Grounding and LLM validation
- Delivers actionable insights to decision-makers within minutes

## Tariff and Trade Agent Scope

The **Tariff and Trade Agent** is a specialized coded agent within the Risk Orbit framework that focuses exclusively on trade policy validation and tariff analysis. It serves as the compliance intelligence layer that:

### Core Capabilities

1. **Policy Retrieval**: Uses UiPath Context Grounding to search indexed trade and tariff policy documents
2. **Structured Data Extraction**: Identifies and extracts:
   - Country/Region regulations
   - Policy identifiers (regulation numbers, circulars, decrees)
   - HS (Harmonized System) codes
   - Tariff rate changes (previous → new rates)
   - Effective dates
   - Compliance requirements
   - Product classifications

3. **Risk Assessment**: Calculates risk indices:
   - **Tariff Risk Index (TRI)**: 0-100 scale measuring tariff volatility
   - **Trade Policy Risk Index (TPRI)**: 0-100 scale measuring policy complexity

4. **Intelligent Analysis**: Provides:
   - Executive summaries
   - Country-specific analysis
   - Compliance requirement identification
   - Actionable recommendations
   - Source citations with document references

### Supported Policy Types

The agent analyzes policies covering:
- **Asia-Pacific**: Indonesia, Vietnam, Philippines, China, South Korea
- **Middle East & GCC**: UAE, Saudi Arabia, Qatar, Egypt
- **Europe & Trans-Atlantic**: EU, UK, US, Canada
- **Africa & Latin America**: Kenya, South Africa, Brazil, Mexico

## Integration into Risk Orbit Automation

The Tariff and Trade Agent operates as a critical component in the larger Risk Orbit workflow:

```
┌─────────────────────────────────────────────────────────────┐
│                    Risk Orbit Multi-Agent Framework         │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   Email Trigger (Maestro Workflow)  │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   Data Collection Layer              │
        │   • Equipment API                   │
        │   • Supplier API                    │
        │   • Scheduler API                    │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   Geopolitical Agent                 │
        │   • Port Status Check                │
        │   • Travel Advisory                 │
        │   • News API (MCP)                   │
        │   • Conflict Verification            │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   Tariff and Trade Agent (This)     │
        │   • Context Grounding Retrieval     │
        │   • Policy Validation                │
        │   • LLM Analysis                    │
        │   • Risk Assessment                  │
        └─────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────┐
        │   Email Notification                 │
        │   • Comprehensive Analysis           │
        │   • Actionable Insights              │
        └─────────────────────────────────────┘
```

### Workflow Integration

1. **Trigger**: Email inquiry received (e.g., "What are current tariff rates for importing gas turbine components from Indonesia and China?")

2. **Data Collection**: Maestro workflow collects shipment details from:
   - Equipment API (product specifications, HS codes)
   - Supplier API (supplier location, origin country)
   - Scheduler API (shipment timeline, destination ports)

3. **Geopolitical Analysis**: Geopolitical agent evaluates:
   - Port congestion and operational status
   - Travel advisories and regional stability
   - Real-time news and conflict verification via MCP

4. **Tariff and Trade Validation**: This agent performs:
   - Context Grounding search for relevant policy documents
   - Structured extraction of tariff rates, compliance requirements
   - LLM-powered validation against system prompts
   - Risk index calculation (TRI/TPRI)
   - Comprehensive report generation

5. **Decision Support**: Final email notification includes:
   - Combined geopolitical and trade risk assessment
   - Tariff impact analysis
   - Compliance requirement checklist
   - Actionable recommendations

## How It Achieves Its Purpose

### 1. Context-Aware Policy Retrieval

The agent leverages **UiPath Context Grounding** to maintain an indexed knowledge base of trade and tariff policies. Using semantic search, it retrieves the most relevant policy documents based on:
- Product categories (HS codes)
- Origin and destination countries
- Equipment types
- Regulatory keywords

**Example**: Query about "gas turbine components (HS 8411) from Indonesia" retrieves:
- Indonesia MoF Regulation No. 115/2025
- Regional trade policy updates
- Related compliance requirements

### 2. Intelligent Document Analysis

Using **GPT-4o** with specialized system prompts, the agent:
- Extracts structured data from policy documents
- Identifies tariff rate changes and effective dates
- Maps HS codes to specific regulations
- Calculates risk indices based on volatility and complexity
- Generates compliance requirement checklists

### 3. Structured Output Format

The agent produces comprehensive reports with:
- **Executive Summary**: High-level findings
- **Country/Region Analysis**: Specific regulations and requirements
- **Tariff Details**: Exact rates, changes, effective dates
- **HS Code Classification**: Product-specific regulations
- **Compliance Requirements**: Documentation, certifications, registrations
- **Risk Assessment**: TRI/TPRI scores with risk level classification
- **Recommendations**: Actionable guidance for compliance officers
- **Citations**: Source document references for traceability

### 4. Integration with UiPath Platform

The agent seamlessly integrates with:
- **UiPath Orchestrator**: For workflow orchestration and job management
- **Context Grounding Service**: For policy document indexing and retrieval
- **LLM Gateway**: For AI-powered analysis and validation
- **Maestro Workflows**: For end-to-end automation
- **MCP Servers**: For external data sources (news APIs)

### 5. Time and Cost Savings

**Before Risk Orbit**:
- Manual research: 4-8 hours per inquiry
- Fragmented data sources
- Risk of outdated information
- Inconsistent analysis quality

**After Risk Orbit**:
- Automated analysis: 2-5 minutes per inquiry
- Centralized, up-to-date policy database
- Consistent, comprehensive reporting
- 95%+ time reduction for trade compliance analysis

## Requirements

* Python 3.10 or higher
* UiPath Automation Cloud account
* UiPath Context Grounding index configured with trade/tariff policy documents
* Access to UiPath LLM Gateway (GPT-4o recommended)

## Installation

```bash
pip install uipath-langchain
```

Using `uv`:

```bash
uv add uipath-langchain
```

## Configuration

### Environment Variables

Create a `.env` file in your project root:

```env
UIPATH_URL=https://cloud.uipath.com/ACCOUNT_NAME/TENANT_NAME
UIPATH_ACCESS_TOKEN=YOUR_TOKEN_HERE
UIPATH_FOLDER_PATH=Agents
```

### Context Grounding Setup

1. **Create Policy Index**: In UiPath Orchestrator, navigate to Indexes and create a new index (e.g., "policy-index")

2. **Upload Policy Documents**: Add trade and tariff policy documents to the associated storage bucket

3. **Configure Index Settings**:
   - **Ingestion**: Advanced (recommended for documents with tables, graphs, structured data)
   - **Data Source**: Storage Bucket
   - **Folder**: Specify the Orchestrator folder containing the index

4. **Verify Index**: Ensure documents are ingested and searchable

### System Prompt Configuration

The agent uses a specialized system prompt that:
- Understands global trade policy document structure
- Extracts structured data (HS codes, tariff rates, dates)
- Calculates risk indices (TRI, TPRI)
- Provides actionable compliance guidance

Customize the system prompt in `main.py` to match your organization's specific requirements.

## Usage

### Command Line Interface

#### Initialize Project

```bash
uipath init
```

Creates a `uipath.json` configuration file.

#### Authenticate

```bash
uipath auth
```

Opens browser for authentication and updates `.env` file.

#### Run Agent Locally

```bash
uipath run -f input.json
```

Execute the agent with JSON input:

```json
{
  "topic": "What are the current tariff rates and compliance requirements for importing gas turbine components (HS 8411) from Indonesia and China? Please provide effective dates, rate changes, and any risk assessments."
}
```

#### Package for Deployment

```bash
uipath pack
```

Creates a `.nupkg` file for deployment to UiPath Orchestrator.

#### Publish to Orchestrator

```bash
uipath publish
```

Deploys the packaged agent to your UiPath Orchestrator.

### Integration in Maestro Workflow

1. **Create Maestro Workflow**: Design BPMN workflow with email trigger

2. **Add Coded Agent Activity**: Include "Invoke Coded Agent" activity in workflow

3. **Configure Agent Call**:
   - **Agent Name**: Select "Tariff and Trade Agent"
   - **Input Parameters**: Pass topic query from email or data collection
   - **Output Mapping**: Map agent output to workflow variables

4. **Handle Response**: Use agent output in subsequent workflow activities (email notification, reporting)

### Example Output

```json
{
  "report": "## Executive Summary:\nAnalysis of tariff rates for gas turbine components (HS 8411)...\n\n## Country/Region Analysis:\n\n### Indonesia:\n- Policy Identifier: MoF Regulation No. 115/2025\n- Effective Date: November 10, 2025\n- Tariff Change: 5% → 7%\n- Risk Assessment: TRI 65 (Moderate)...",
  "validation_status": "VERIFIED",
  "citations": ["tariffpolicy.txt Section 1", "tradepolicy.txt Section A"]
}
```

## Project Structure

```
uipath_coded_process/
├── main.py                 # Agent implementation with LangGraph
├── input.json              # Sample input query
├── output.json             # Agent output example
├── pyproject.toml          # Project dependencies and metadata
├── langgraph.json          # LangGraph configuration
├── uipath.json             # UiPath agent configuration (generated)
├── .env                    # Environment variables (not in git)
├── tradepolicy.txt         # Sample policy document
├── tariffpolicy.txt        # Sample policy document
└── README.md               # This file
```

## Key Components

### `main.py`

Contains the LangGraph agent implementation:

- **GraphState**: Input state model (topic query)
- **GraphOutput**: Output model (report, validation_status, citations)
- **retrieve_context()**: Context Grounding retrieval function
- **generate_report()**: LLM-powered analysis and report generation
- **graph**: Compiled LangGraph workflow

### Context Grounding Integration

The agent uses a workaround for the SDK's folder key handling:

```python
# Resolve folder key from folder path
folder_key = sdk.folders.retrieve_key(folder_path="Agents")

# Direct API call with proper headers
response = await sdk.api_client.request_async(
    method="POST",
    url="ecs_/v1/search",
    json={
        "query": {"query": state.topic, "numberOfResults": 10},
        "schema": {"name": "policy-index"}
    },
    headers={"X-UiPath-FolderKey": folder_key}
)
```

## Development

### Setting Up Development Environment

1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   # or
   uv sync
   ```
4. Configure `.env` file with UiPath credentials
5. Set up Context Grounding index in Orchestrator
6. Test locally:
   ```bash
   uipath run -f input.json
   ```

### Customization

#### Adding New Policy Documents

1. Upload new policy documents to the storage bucket associated with your Context Grounding index
2. Trigger index re-ingestion if needed
3. Agent will automatically retrieve relevant documents based on semantic search

#### Customizing System Prompt

Modify the `system_prompt` in `generate_report()` function to:
- Add organization-specific compliance requirements
- Include custom risk calculation formulas
- Adjust output format to match your reporting standards

#### Extending Functionality

The agent can be extended to:
- Integrate with external tariff databases
- Add real-time currency conversion
- Include historical trend analysis
- Generate compliance checklists automatically

## Troubleshooting

### Context Grounding Not Retrieving Documents

- Verify index name matches in code (`policy-index`)
- Check folder path configuration (`UIPATH_FOLDER_PATH`)
- Ensure documents are ingested in the index
- Verify folder key resolution (check console logs)

### Authentication Errors

- Run `uipath auth` to refresh credentials
- Verify `.env` file has correct `UIPATH_URL` and `UIPATH_ACCESS_TOKEN`
- Check token expiration in Orchestrator

### LLM Gateway Errors

- Verify LLM Gateway is configured in Orchestrator
- Check model availability (GPT-4o recommended)
- Review timeout settings in agent code

## Contributing

This agent is part of the Risk Orbit multi-agent framework. For contributions:
1. Follow UiPath coded agent best practices
2. Maintain structured output format
3. Add comprehensive error handling
4. Include logging for debugging

## License

MIT License

## Author

**Naveen Chatlapalli**  
Ashling Partners  
Solution Architect

---

## Related Resources

- [UiPath LangChain Python SDK Documentation](https://uipath.github.io/uipath-python/langchain/)
- [Context Grounding Documentation](https://uipath.github.io/uipath-python/langchain/context_grounding/)
- [UiPath Coded Agents Guide](https://docs.uipath.com/)
- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)

---

**Built for UiPath Coded Agents Hackathon 2025**

