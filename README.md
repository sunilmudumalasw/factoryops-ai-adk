<p align="center">

# 🏭 FactoryOps AI

### Multi-Agent Manufacturing COO using Google ADK, MCP & Gemini

Enterprise AI Decision Support System for Manufacturing Operations

</p>

---

> **Capstone Project**  
> Google AI Agents: Intensive Vibe Coding (Kaggle)

---

### Demonstrated AI Concepts

- ✅ Google Agent Development Kit (ADK)
- ✅ Multi-Agent Systems
- ✅ Model Context Protocol (MCP)
- ✅ Agent Skills
- ✅ Executive Decision Intelligence
- ✅ Human-in-the-Loop Approval
- ✅ Responsible AI

---

## Executive Summary

FactoryOps AI is an enterprise-grade AI decision support system that helps manufacturing leaders monitor factory health, assess operational risks, and make executive decisions using a coordinated team of AI agents.

The system combines Google Agent Development Kit (ADK), Model Context Protocol (MCP), reusable manufacturing skills, and an Executive Decision Engine to transform production, inventory, and quality analytics into actionable business recommendations with human approval.

---

## Key Features

- 🤖 Multi-Agent Manufacturing COO
- 🏭 Operations Agent
- 📦 Inventory Agent
- 🔍 Quality Agent
- 🧠 Executive Decision Engine
- ✅ Human Approval Workflow
- 🔒 Audit Logging
- 🔗 Model Context Protocol (MCP)
- ⚙ Manufacturing Analytics Skills
- 📊 Executive Dashboard

---

## Architecture

FactoryOps AI follows a layered enterprise architecture.

```text
Streamlit Dashboard
        │
        ▼
Manufacturing COO Agent (Google ADK)
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Operations  Inventory  Quality
   Agent      Agent      Agent
        │
        ▼
Factory Health Tool
        │
        ▼
Executive Decision Engine
        │
        ▼
Human Approval Workflow
        │
        ▼
Audit Logging

──────────────────────────────

FactoryOps MCP Server

production_summary()
inventory_summary()
quality_summary()
factory_health_summary()
```

---

---

## Technologies

| Layer | Technology |
|---------|---------|
| Frontend | Streamlit |
| AI Framework | Google Agent Development Kit (ADK) |
| LLM | Gemini 2.5 Flash |
| Agent Protocol | Model Context Protocol (MCP) |
| Programming Language | Python |
| Analytics Engine | Pandas |
| Manufacturing Skills | Custom Manufacturing Skills |
| Business Layer | Executive Decision Engine |
| Governance | Human Approval Workflow & Audit Logging |

---

## AI Concepts Demonstrated

This project demonstrates the following concepts from the Google AI Agents Capstone:

- Multi-Agent Systems using Google ADK
- Agent Delegation and Coordination
- Model Context Protocol (MCP)
- Reusable Agent Skills
- Executive Decision Intelligence
- Human-in-the-Loop Approval
- Responsible AI Practices
- Enterprise AI Architecture

---

## Project Structure

```text
factoryops-ai-adk/
│
├── app/                  # ADK agents
├── business/             # Executive decision engine & audit logging
├── datasets/             # Manufacturing datasets
├── docs/                 # Architecture and design documentation
├── mcp/                  # MCP server and client
├── skills/               # Manufacturing analytics skills
├── tools/                # ADK tools
├── ui/                   # Streamlit dashboard
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Project Documentation

Detailed design documentation is available in the **docs/** folder.

| Document | Description |
|----------|-------------|
| Problem_Statement.md | Business problem and proposed solution |
| System_Architecture.md | Overall system architecture |
| Agent_Design.md | Multi-agent design and responsibilities |
| Data_Model.md | Application data model |
| User_Workflow.md | End-to-end user workflow |

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/sunilmudumalasw/factoryops-ai-adk.git
cd factoryops-ai-adk
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Launch the dashboard

```bash
streamlit run ui/app.py
```

### 6. Run the MCP client

```bash
python mcp/client.py
```