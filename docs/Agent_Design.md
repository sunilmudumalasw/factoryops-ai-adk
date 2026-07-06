# FactoryOps AI Agent Design

## 1. Manufacturing COO Agent

### Responsibility

- Primary user interface
- Understand user requests
- Delegate work to specialist agents
- Consolidate factory health results
- Present executive recommendations

Uses

- Operations Agent
- Inventory Agent
- Quality Agent

---

## 2. Operations Agent

### Responsibility

Analyze

- Production
- Throughput
- Machine Performance
- Manufacturing Efficiency

Uses

- Production Tool
- Production Skill

---

## 3. Inventory Agent

### Responsibility

Analyze

- Inventory Levels
- Low Stock Materials
- Lead Time
- Reorder Risk

Uses

- Inventory Tool
- Inventory Skill

---

## 4. Quality Agent

### Responsibility

Analyze

- Defects
- Critical Defects
- Repair Cost
- Quality Trends

Uses

- Quality Tool
- Quality Skill

---

## Business Layer (Not an Agent)

### Executive Decision Engine

Responsibility

- Evaluate overall factory health
- Assess business risk
- Determine business priority
- Recommend executive actions
- Determine whether human approval is required

Uses

- Factory Health Report

Produces

- Executive Decision
- Risk Level
- Business Priority
- Recommended Action
- Approval Required

---

## Overall Collaboration

User

        │

        ▼

Manufacturing COO Agent

        │

───────────────

│         │         │

▼         ▼         ▼

Operations Inventory Quality

───────────────

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

Final Executive Recommendation