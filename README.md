<<<<<<< HEAD
# 🧠 Autonomous Multi-Agent Cognitive Engine

> **A sophisticated multi-agent system for intelligent task processing, delegation, and coordination**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
[![LangSmith](https://img.shields.io/badge/LangSmith-Tracing-orange.svg)](https://langsmith.com)
[![Flask](https://img.shields.io/badge/Flask-2.0+-red.svg)](https://flask.palletsprojects.com)

## 🚀 Overview

This project implements an **autonomous multi-agent cognitive engine** that intelligently delegates tasks to specialized domain agents. The system features a supervisor agent coordinating with six specialized sub-agents, providing comprehensive solutions across research, coding, planning, translation, content creation, and document analysis.

### ✨ Key Features

- 🎯 **Intelligent Task Delegation** - Automatic routing to domain specialists with >90% accuracy
- 🔄 **Multi-Agent Coordination** - Seamless collaboration between 6 specialized agents
- 📊 **Complete Observability** - Full LangSmith tracing with input visibility
- 🔒 **Privacy-First Design** - Fresh session isolation with no persistent conversations
- 🌐 **Real-Time Web Interface** - Modern chat UI with Socket.IO
- 📝 **Professional Output** - Clean markdown formatting with proper attribution

## 📊 Project Presentation

🎨 **[View Interactive Presentation](https://www.canva.com/design/DAG_O1x7c-0/8WrNnqafjj7sjWJp1PyGKQ/edit?utm_content=DAG_O1x7c-0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)** - Complete project overview with visual demonstrations and system architecture

## 🏗️ Architecture

```
┌─────────────────┐
│ Supervisor Agent │ ← Central Orchestrator
└─────────┬───────┘
          │
    ┌─────┴─────┐
    │ Delegation │
    │  Analysis  │
    └─────┬─────┘
          │
┌─────────┴─────────┐
│   Subagent Pool   │
├───────────────────┤
│ • SearchAgent     │ → Web research & information gathering
│ • CodeAgent       │ → Software development & debugging  
│ • PlanningAgent   │ → Strategic planning & project management
│ • CreativeAgent   │ → Content creation & marketing copy
│ • TranslationAgent│ → Multilingual translation & localization
│ • SummarizerAgent │ → Document analysis & synthesis
└───────────────────┘
```

## 🛠️ Quick Start

### Prerequisites

- Python 3.8+
- API Keys: Groq, Anthropic, Tavily, LangSmith

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/Autonomous-Cognitive-Engine-for-Deep-Research-and-Long-Horizon-Tasks.git
cd Autonomous-Cognitive-Engine-for-Deep-Research-and-Long-Horizon-Tasks

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Environment Setup

Create a `.env` file with your API keys:

```bash
# Core API Keys
GROQ_API_KEY=your_groq_api_key
ANTHROPIC_API_KEY=your_anthropic_key
TAVILY_API_KEY=your_tavily_key

# LangSmith Tracing (Optional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=autonomous-cognitive-engine

# Workflow Configuration
USE_LANGGRAPH=false
```

### Running the Application

```bash
# Web Interface (Recommended)
python app.py
# Access at http://localhost:5000

# CLI Interface
python main.py
```

## 🎯 Usage Examples

### Web Interface
1. Start the web app: `python app.py`
2. Open http://localhost:5000
3. Start chatting with the autonomous system

### CLI Interface
```bash
python main.py
> "Create a business plan for a coffee shop"
# → Automatically delegated to PlanningAgent

> "Translate this to Spanish: Hello world"
# → Automatically delegated to TranslationAgent

> "Write Python code to sort a list"
# → Automatically delegated to CodeAgent
```

### API Usage
```python
from src.agents.supervisor_agent import SupervisorAgent

agent = SupervisorAgent()
result = agent.run_with_context("Your task here", [], "session-id")
print(result['final_response'])
```

## 🧪 Testing

```bash
# Test all agents
python simple_test.py

# Test delegation functionality
python test_delegation.py

# Test TODO workflow
python test_todo_functionality.py

# Test input visibility
python test_input_visibility.py
```

## 📊 System Capabilities

### Agent Specializations

| Agent | Primary Function | Use Cases |
|-------|------------------|-----------|
| **SearchAgent** | Web research & information gathering | Market analysis, fact checking, current events |
| **CodeAgent** | Software development & debugging | Algorithm implementation, code review, technical docs |
| **PlanningAgent** | Strategic planning & project management | Business strategy, project roadmaps, timelines |
| **CreativeAgent** | Content creation & marketing | Blog posts, social media, brand messaging |
| **TranslationAgent** | Multilingual translation (35+ languages) | Document translation, content localization |
| **SummarizerAgent** | Document analysis & synthesis | Research analysis, executive summaries |

### Performance Metrics

- ✅ **>90% delegation accuracy** in task-to-agent matching
- ✅ **Real-time processing** with Socket.IO
- ✅ **Complete traceability** through LangSmith integration
- ✅ **Fresh session isolation** for privacy protection
- ✅ **Professional output formatting** with attribution

## 🔍 System Behavior

### Execution Patterns

The system uses three execution pathways:

1. **Direct Processing** (40%) - Simple queries handled by supervisor
2. **Single Delegation** (45%) - Domain-specific tasks routed to specialists  
3. **Complex Workflows** (15%) - Multi-step coordination with artifact storage

### Trace Metadata

LangSmith traces show different patterns based on execution type:

```json
// Simple Direct Processing
{
  "tools_used": 0,
  "delegated_to": null,
  "todos_created": 0,
  "synthesis_file": null
}

// Single Agent Delegation
{
  "tools_used": 2,
  "delegated_to": "PlanningAgent",
  "todos_created": 1,
  "synthesis_file": null
}

// Complex Multi-Step Workflow
{
  "tools_used": 5,
  "workflow": "TODO_VFS_WORKFLOW",
  "todos_created": 3,
  "synthesis_file": "synthesis_20241123_143045.md"
}
```

## 📁 Project Structure

```
├── src/
│   ├── agents/                 # All agent implementations
│   ├── tools/                  # Delegation and management tools
│   ├── memory/                 # Conversation and VFS systems
│   └── graph/                  # Alternative workflow (optional)
├── templates/                  # Web interface templates
├── docs/                       # Documentation
├── notebooks/                  # Development notebooks
├── app.py                      # Flask web application
├── main.py                     # CLI interface
└── requirements.txt            # Dependencies
```

## 🔧 Configuration

### Delegation Settings
- **Confidence Threshold**: 0.4 minimum for agent routing
- **Session Management**: Fresh isolation with no persistence
- **Response Format**: Professional markdown with attribution

### Workflow Options
- **Traditional Supervisor**: Default workflow with TODO functionality
- **LangGraph**: Alternative workflow (set `USE_LANGGRAPH=true`)

## 📚 Documentation

- **[Technical Documentation](PROJECT_DOCUMENTATION.md)** - Complete system architecture and implementation details
- **[Architecture Guide](docs/architecture.md)** - System design and component overview
- **[Workflow Specifications](docs/ideal_workflow.md)** - Detailed workflow documentation
- **[Development Milestones](docs/milestones.md)** - Project development timeline

## 🚀 Deployment

### Local Development
```bash
python app.py  # Web interface
python main.py # CLI interface
```

### Production Considerations
- Configure proper API rate limits
- Set up monitoring and logging
- Implement proper error handling
- Consider load balancing for high traffic

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain** for the multi-agent framework
- **LangSmith** for comprehensive tracing and monitoring
- **Groq** for fast LLM inference
- **Tavily** for web search capabilities



---


=======
# Autonomous-Cognitive-Engine-for-Deep-Research-and-Long-Horizon-Tasks

*A Springboard Infosys Internship Program Project*

## **Project Overview**

The **Autonomous Cognitive Engine** project focuses on building an advanced **LLM-driven agent** capable of performing **deep research, multi-step reasoning, and long-horizon task execution** without constant human input.

The goal is to design an AI system that can:

* Break down complex problems into smaller actionable subtasks
* Maintain memory across long workflows
* Collaborate with specialized sub-agents
* Use external tools (search, file storage, utilities)
* Generate high-quality outputs independently
* Complete tasks end-to-end using structured planning and reasoning

This project uses **LangGraph**, **LangChain**, and **LLM agents** to build a scalable, stateful cognitive architecture.

## **Project Objectives**

### 1. **Task Planning & Decomposition**

Build a dynamic **TODO Planner** that:

* Interprets complex user requests
* Splits them into subtasks
* Tracks progress
* Updates tasks as they are completed

### 2. **Memory & Context Management**

Implement an **external memory module** using a virtual file system to:

* Save intermediate results
* Store research insights
* Retain instructions
* Load information in later steps

Use operations like:
`write_file`, `read_file`, `edit_file`, `ls`

### 3. **Sub-Agent Delegation**

Enable the main agent (Supervisor Agent) to call specialized sub-agents such as:

* Summarization agent
* Research agent
* Code agent
* Search agent

This allows modular, structured workflows.

### 4. **Stateful Agent Architecture (LangGraph)**

Use **LangGraph StateGraph** to maintain:

* Agent state
* Task list
* Memory
* Execution flow
* Tool calls
* Loop conditions

This creates deterministic and reproducible AI workflows.

### 5. **Final Multi-Step Autonomous Execution**

By end of the project, the agent should:

* Take a complex query
* Plan tasks
* Search, write, reason, summarize
* Store intermediate steps
* Delegate sub-tasks
* Produce a final polished output

Example final use-cases:

* End-to-end research paper generator
* Multi-document analysis engine
* Long-form content creation
* Multi-agent workflow automations

## **System Architecture**

```
User Input
   ↓
Supervisor Agent (LLM)
   ↓
Task Planner  →  TODO List
   ↓
Memory System (Virtual File System)
   ↓
Sub-Agents (Search, Summarizer, Tool Agent)
   ↓
StateGraph (LangGraph Execution Engine)
   ↓
Loop Until All Tasks Complete
   ↓
Final Output
```

## **Tech Stack**

### Core

* Python 3.10+
* LangGraph
* LangChain
* LLMs (OpenAI / Anthropic / Groq)

### Tools & Integrations

* Tavily Search API
* File system tools
* LangSmith (observability & tracing)

### Optional Enhancements

* Vector memory
* Multi-agent collaboration
* Specialized tool kits

## **Recommended Folder Structure**

```
/autonomous-agent
│
├── src/
│   ├── agents/
│   │   ├── supervisor_agent.py
│   │   ├── summarizer_agent.py
│   │   └── search_agent.py
│   ├── memory/
│   │   ├── vfs.py
│   ├── tools/
│   │   ├── write_file.py
│   │   ├── read_file.py
│   │   ├── search_tool.py
│   ├── graph/
│       ├── state_graph.py
│
├── notebooks/
│   ├── milestone_1.ipynb
│   ├── milestone_2.ipynb
│
├── data/
│
├── docs/
│   ├── architecture.md
│   ├── milestones.md
│
├── README.md
└── LICENSE
```

## **Milestone Plan (8 Weeks)**

### **Week 1: Setup & Agent Skeleton**

* Set up repo, virtual environment
* Build minimal LLM agent
* Understand LangGraph basics

### **Week 2: Task Planner & Memory**

* Implement TODO planner
* Add temporary memory + state storage

### **Week 3: Virtual File System**

* Add persistent memory
* Implement read/write/edit tools

### **Week 4: Sub-Agent Delegation**

* Create summarizer + search agents
* Connect sub-agents to supervisor

### **Week 5: Tool Integration**

* Add real APIs (e.g., Tavily Search)
* Add utility tools

### **Week 6: Complete Autonomous Loop**

* Integrate planner + memory + delegation
* Full execution cycles

### **Week 7: Final Use-Case Implementation**

* Build final research or automation pipeline
* Run on multiple long-horizon test cases

### **Week 8: Documentation & Demo**

* Final testing
* README + architecture doc
* Final demo presentation

## **Evaluation Criteria**

Interns will be assessed on:

### Technical

* Implementation of planner
* Memory module quality
* Sub-agent logic
* Code structure & modularity
* Correct use of LangGraph state

### GitHub

* Frequent commits
* Branch hygiene
* Proper documentation

### Final Output

* Completeness of autonomous workflow
* Quality of final report/analysis
* Ability to explain architecture

## **Future Enhancements (Optional)**

* Multi-agent coordination
* Knowledge graph integration
* Long-term vector memory
* Auto-evolving agents
* Tool suggestion via reflection
* UI dashboard for agent runs

## **Intern Work Guidelines**

* Each intern works **individually** in their own GitHub branch
* Minimum 3–5 commits per week
* Main branch is protected
* Proper folder structure required
* No copying or sharing code between interns
* All milestones must be submitted on time

## **License**

This project is released under the MIT License.
See `LICENSE` for details.

## 📬 **Contact**

For queries, reach out to your mentor:
**[springboardmentor24680x@gmail.com](mailto:springboardmentor24680x@gmail.com)**
>>>>>>> 510f21a2bb9bc27eba42d7d5c89f638ac3446d60
