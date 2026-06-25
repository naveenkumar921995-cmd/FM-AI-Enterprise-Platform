# 🏢 FM AI Enterprise Platform

### AI-Powered Facility Management & Building Operations Assistant

FM AI Enterprise Platform is an intelligent facility management application that combines traditional maintenance operations with Generative AI.

The platform helps facility teams manage assets, work orders, incidents, vendors, and technical documentation while providing AI-assisted troubleshooting for HVAC, Electrical, and Fire systems.

---

## 🎯 Why I Built This Project

In most facilities, engineers spend significant time searching through manuals, SOPs, maintenance records, and incident reports before resolving issues.

This project demonstrates how Artificial Intelligence can assist facility operations by:

* Centralizing operational data
* Providing AI-powered technical support
* Searching engineering documentation using RAG
* Automating knowledge retrieval
* Improving maintenance decision-making

---

## 🚀 Key Features

### 🤖 AI Facility Assistant

Ask questions in natural language:

**Examples**

* AHU is not cooling properly
* Fire detector showing fault
* Transformer breaker tripped
* Explain preventive maintenance for chillers

The system automatically routes queries to the appropriate specialist agent.

---

### 🏭 Asset Management

Track facility assets with:

* Asset ID
* System Type
* Location
* Status
* Health Score

Current Dataset: **500 Assets**

---

### 📋 Work Order Management

Manage maintenance activities including:

* Open Work Orders
* Closed Work Orders
* Priority Tracking
* Assignment Status

Current Dataset: **1000 Work Orders**

---

### 🚨 Incident Management

Monitor operational incidents with:

* Severity Classification
* Incident Status
* System Impact Tracking

Current Dataset: **300 Incidents**

---

### 🏢 Vendor Management

Maintain vendor information including:

* Vendor Details
* Service Categories
* Contact Information

Current Dataset: **50 Vendors**

---

## 🧠 AI Architecture

```text
User Question
      │
      ▼
Supervisor Agent
      │
 ┌────┼────┐
 ▼    ▼    ▼
HVAC Electrical Fire
Agent  Agent  Agent
      │
      ▼
Document Retrieval (RAG)
      │
      ▼
Groq LLM
      │
      ▼
AI Response + Recommendations
```

---

## 🛠 Technologies Used

### Artificial Intelligence

* Groq Llama 3.3 70B
* LangChain
* Retrieval-Augmented Generation (RAG)
* Multi-Agent Architecture
* Vector Search

### Data & Storage

* ChromaDB
* SQLite
* CSV Datasets
* Pandas

### Frontend

* Streamlit
* Plotly

### Backend

* Python
* SQLAlchemy

---

## 💡 Skills Demonstrated

This project showcases practical skills in:

### AI Engineering

* Multi-Agent Systems
* Prompt Engineering
* RAG Pipelines
* LLM Integration
* Vector Databases

### Software Development

* Python Development
* Backend Architecture
* Data Processing
* Dashboard Development

### Facility Management Domain Knowledge

* HVAC Operations
* Electrical Systems
* Fire & Life Safety
* Work Order Management
* Incident Management
* Vendor Management

---

## 📸 Application Screens

### Executive Dashboard

(Add Screenshot)

### AI Assistant

(Add Screenshot)

### Asset Management

(Add Screenshot)

### Work Orders

(Add Screenshot)

### Incident Management

(Add Screenshot)

### Vendor Management

(Add Screenshot)

---

## 🔮 Planned Enhancements

* SQL Agent for Natural Language Analytics
* Predictive Maintenance
* Asset Failure Prediction
* Energy Management Dashboard
* IoT Sensor Integration
* Digital Twin Integration

---

## 👨‍💻 Author

**Naveen Kumar**

Facility Management Professional transitioning into AI-Powered Building Operations and Enterprise Automation.

### Project Focus

Building practical AI solutions for Facilities Management, Smart Buildings, and Intelligent Operations.
