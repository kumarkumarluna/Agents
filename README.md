# 🤖 AI Agent Fundamentals

A hands-on learning repository for understanding and building **AI Agents from the ground up** using Python, LLM APIs, and tool calling.

Instead of starting directly with frameworks such as LangChain or LangGraph, this project focuses on understanding the **core mechanics behind agentic AI systems** by implementing them step by step.

---

## 🧠 What I Am Learning

This repository focuses on understanding the fundamentals behind AI Agent systems:

* Large Language Models (LLMs)
* LLM API integration
* Prompt engineering
* Environment variables
* OpenAI-compatible APIs
* Model selection and discovery
* Function calling
* Tool calling
* Tool schemas
* Tool execution
* Passing tool results back to the LLM
* Agent decision-making
* Multi-step agent workflows
* Agent loops
* Structured outputs
* Memory
* RAG
* Multi-agent systems

---

## 🎯 Project Objective

The objective of this project is to understand **how AI agents actually work internally** rather than treating frameworks as black boxes.

The project starts with a simple LLM API call and gradually evolves into an agent capable of:

```text
User
  ↓
LLM
  ↓
Understand User Request
  ↓
Decide Whether a Tool Is Required
  ↓
Generate Tool Call
  ↓
Application Executes Tool
  ↓
Tool Result
  ↓
LLM
  ↓
Final Response
```

This provides a foundation for understanding frameworks such as:

* LangChain
* LangGraph
* CrewAI
* AutoGen
* MCP
* RAG-based agents
* Multi-agent architectures

---

## 🛠️ Technologies Used

* **Python**
* **OpenAI Python SDK**
* **Groq API**
* **uv**
* **python-dotenv**
* **Git**
* **GitHub**

---

## 📁 Project Structure

```text
ai-agent-fundamentals/
│
├── main.py
├── tools.py
├── pyproject.toml
├── uv.lock
├── .env
├── .gitignore
└── README.md
```

### `Main_folder/main.py`

Contains the main application logic for:

* Connecting to the LLM
* Sending user prompts
* Defining available tools
* Receiving tool calls
* Executing requested tools
* Sending tool results back to the LLM
* Generating the final response

### `tools/tools.py`

Contains custom Python functions that can be exposed to the LLM as tools.

Example:

```python
def calculator(a, b, operation):
    ...
```

### `pyproject.toml`

Contains project metadata, dependencies, and Python configuration.

### `uv.lock`

Locks the exact versions of project dependencies to ensure reproducible environments.

### `.env`

Stores sensitive environment variables such as API keys.

> `.env` should never be committed to GitHub.

### `.gitignore`

Prevents sensitive and unnecessary files such as `.env` and virtual environments from being committed.

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

The application loads the API key through environment variables.

Never hard-code API keys directly inside Python source code.

### Example

❌ Do not do this:

```python
api_key = "gsk_xxxxxxxxxxxxxxxxx"
```

✅ Use this instead:

```python
import os

api_key = os.getenv("GROQ_API_KEY")
```

---

# ⚙️ Installation

This project uses **uv** for Python environment and dependency management.

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate into the project:

```bash
cd ai-agent-fundamentals
```

---

## 2. Create the Virtual Environment

```bash
uv venv
```

---

## 3. Activate the Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 4. Install Dependencies

If dependencies are already defined in `pyproject.toml`:

```bash
uv sync
```

---

## 5. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## 6. Run the Application

```bash
uv run main.py
```

---

# 🔧 Tool Calling Architecture

The current implementation demonstrates the fundamental tool-calling workflow.

```text
                    ┌─────────────────┐
                    │      User       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │       LLM       │
                    │                 │
                    │ Understands     │
                    │ user request    │
                    └────────┬────────┘
                             │
                    Tool required?
                       /          \
                     No            Yes
                     │              │
                     │              ▼
                     │       ┌───────────────┐
                     │       │  Tool Call    │
                     │       │               │
                     │       │ name + args   │
                     │       └───────┬───────┘
                     │               │
                     │               ▼
                     │       ┌───────────────┐
                     │       │ Python Tool   │
                     │       │ Execution     │
                     │       └───────┬───────┘
                     │               │
                     │               ▼
                     │       ┌───────────────┐
                     │       │ Tool Result   │
                     │       └───────┬───────┘
                     │               │
                     └───────┬───────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │       LLM       │
                    │                 │
                    │ Generate final  │
                    │ response        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Response    │
                    └─────────────────┘
```

The important concept is that the **LLM does not directly execute Python code**.

Instead:

```text
LLM
 ↓
Requests a tool
 ↓
Application receives request
 ↓
Application executes Python function
 ↓
Application sends result to LLM
 ↓
LLM generates final answer
```

This separation between **reasoning/decision-making and tool execution** is fundamental to agent architecture.

---

# 🧮 Example Tool: Calculator

The current project contains a simple calculator tool.

It can perform operations such as:

```text
Addition
Subtraction
Multiplication
Division
```

For example, the user might ask:

```text
What is 25 × 4?
```

The LLM can determine that a calculator tool is required.

It may generate a structured tool call similar to:

```json
{
  "name": "calculator",
  "arguments": {
    "a": 25,
    "b": 4,
    "operation": "multiply"
  }
}
```

The Python application receives this request and executes:

```python
calculator(25, 4, "multiply")
```

The tool returns:

```text
100
```

The result is then passed back to the LLM.

The LLM can finally generate:

```text
25 × 4 = 100
```

---

# 🔄 Basic Agent Workflow

The current implementation can be understood as:

```text
1. Receive user input
        ↓
2. Send input + available tools to LLM
        ↓
3. LLM analyzes the request
        ↓
4. LLM decides whether a tool is required
        ↓
5. LLM generates structured tool call
        ↓
6. Application executes the tool
        ↓
7. Tool returns result
        ↓
8. Result is sent back to LLM
        ↓
9. LLM generates final response
        ↓
10. Return response to user
```

This is the foundation on which more advanced agent loops are built.

---

# 🧩 Important Concepts

## LLM

A Large Language Model processes natural-language input and generates responses based on its learned patterns and the context provided to it.

In an agent system, the LLM acts as the **decision-making component**.

---

## Tool

A tool is an external capability that the LLM can request the application to execute.

Examples:

```text
Calculator
Web Search
Database Query
Weather API
File Reader
Email Sender
Code Executor
```

---

## Tool Calling

Tool calling allows an LLM to generate a structured request for a specific function.

For example:

```json
{
  "name": "calculator",
  "arguments": {
    "a": 10,
    "b": 20,
    "operation": "add"
  }
}
```

The application then executes the requested function.

---

## Function Calling vs Tool Calling

Function calling generally refers to the model requesting execution of a defined function.

Tool calling is the broader concept of allowing the model to interact with external capabilities.

In modern LLM APIs, the terminology may vary between providers.

---

## Agent

A basic agent can be thought of as:

```text
LLM + Tools + Execution Loop
```

A more capable agent may additionally include:

```text
LLM
+
Tools
+
Memory
+
Planning
+
State
+
Observation
+
Execution
```

---

# 📚 Learning Roadmap

## Phase 1 — LLM Fundamentals

* [x] Python environment setup
* [x] LLM API integration
* [x] Environment variable configuration
* [x] Model discovery
* [x] Basic LLM prompting

## Phase 2 — Tool Calling

* [x] Function definition
* [x] Tool definition
* [x] Tool schema
* [x] Tool calling
* [x] Tool execution
* [x] Returning tool results
* [x] Final LLM response

## Phase 3 — Agent Fundamentals

* [ ] Multiple tools
* [ ] Tool selection
* [ ] Better tool schemas
* [ ] Tool validation
* [ ] Agent loops
* [ ] Multi-step execution
* [ ] Error handling
* [ ] Retry mechanisms
* [ ] State management

## Phase 4 — Advanced Agent Capabilities

* [ ] Structured outputs
* [ ] Memory
* [ ] Planning
* [ ] Reflection
* [ ] Web search
* [ ] Database tools
* [ ] File tools
* [ ] API integrations

## Phase 5 — RAG

* [ ] Document loading
* [ ] Text extraction
* [ ] Chunking
* [ ] Embeddings
* [ ] Vector databases
* [ ] Similarity search
* [ ] Retrieval
* [ ] Context injection
* [ ] RAG-powered agents

## Phase 6 — Agent Frameworks

* [ ] LangChain
* [ ] LangGraph
* [ ] CrewAI
* [ ] AutoGen
* [ ] MCP
* [ ] Multi-agent systems

## Phase 7 — Production Agents

* [ ] Authentication
* [ ] Authorization
* [ ] Observability
* [ ] Logging
* [ ] Evaluation
* [ ] Guardrails
* [ ] Rate limiting
* [ ] Error recovery
* [ ] Cost optimization
* [ ] Deployment
* [ ] Monitoring

---

# 🚀 Evolution of the Project

The repository is intentionally designed to evolve incrementally.

### Stage 1

```text
User
 ↓
LLM
 ↓
Response
```

### Stage 2

```text
User
 ↓
LLM
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Response
```

### Stage 3

```text
User
 ↓
Agent
 ↓
Tool Selection
 ↓
Tool Execution
 ↓
Observation
 ↓
Next Decision
 ↓
Tool / Response
```

### Stage 4

```text
                ┌──────────────┐
                │     User     │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │    Agent     │
                └──────┬───────┘
                       ↓
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Search       Database     Calculator
          ↓            ↓            ↓
          └────────────┼────────────┘
                       ↓
                    Result
                       ↓
                    Agent
                       ↓
                  Final Answer
```

### Final Goal

Eventually, the project will evolve toward:

```text
                    ┌─────────────┐
                    │    User     │
                    └──────┬──────┘
                           ↓
                    ┌─────────────┐
                    │ AI Agent    │
                    └──────┬──────┘
                           ↓
              ┌────────────┴────────────┐
              │                         │
              ↓                         ↓
          Planning                   Memory
              │                         │
              └────────────┬────────────┘
                           ↓
                    Tool Selection
                           ↓
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
       Web Tool        DB Tool          RAG Tool
          ↓                ↓                ↓
          └────────────────┼────────────────┘
                           ↓
                       Observation
                           ↓
                    Next Agent Step
                           ↓
                     Final Response
```

---

# 📝 Learning Philosophy

This repository follows a **build-from-first-principles** approach.

Instead of immediately using high-level abstractions, each concept is implemented and understood individually.

The learning progression is:

```text
LLM
 ↓
Prompting
 ↓
API Integration
 ↓
Tools
 ↓
Tool Calling
 ↓
Tool Execution
 ↓
Agent Loop
 ↓
Memory
 ↓
RAG
 ↓
Frameworks
 ↓
Multi-Agent Systems
 ↓
Production Architecture
```

Each major feature is implemented incrementally and documented through Git commits.

This repository serves as a practical record of my progress in:

* AI Engineering
* LLM Application Development
* Agentic AI
* Tool Calling
* RAG
* Agent Architecture
* Multi-Agent Systems

---

# 🎯 Goal

The ultimate goal is to develop a strong practical understanding of **agentic AI architecture** and be able to build AI agents both:

1. **From scratch**, using LLM APIs and custom Python logic.
2. **Using modern frameworks**, such as LangChain and LangGraph.

The project will eventually progress from a simple LLM application into a complete agentic system capable of:

```text
Reasoning
+
Tool Usage
+
Multi-Step Execution
+
Memory
+
RAG
+
External APIs
+
Database Interaction
+
Planning
+
Multi-Agent Collaboration
```

---

# 🔒 Security

Never commit sensitive information such as:

```text
.env
API Keys
Access Tokens
Passwords
Database Credentials
Private Keys
Cloud Credentials
```

The `.env` file should be included in `.gitignore`.

Example:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

If an API key is accidentally pushed to GitHub:

1. Revoke the exposed key immediately.
2. Generate a new key.
3. Remove the secret from the repository history if necessary.
4. Update the local `.env` file.
5. Verify that the new key is not exposed.

---

# 📌 Current Status

**Status:** 🚧 Active Development

The project currently focuses on:

```text
LLM API
   ↓
Tool Definition
   ↓
Tool Calling
   ↓
Tool Execution
   ↓
Tool Result
   ↓
Final LLM Response
```

Future commits will progressively introduce more advanced agent capabilities.

---

## ⭐ Key Takeaway

The purpose of this project is not simply to **use an AI agent framework**.

The purpose is to understand:

> **What actually happens inside an AI agent when it decides to use a tool, executes that tool, observes the result, and continues the task.**

Understanding these fundamentals makes higher-level agent frameworks significantly easier to learn and debug.

---

## 📈 Learning Progress

```text
[████████░░░░░░░░░░░░] AI Agent Fundamentals

Completed:
✓ LLM API Integration
✓ Prompting
✓ Tool Definition
✓ Tool Calling
✓ Tool Execution
✓ Tool Result Handling

Upcoming:
→ Multiple Tools
→ Agent Loops
→ Memory
→ RAG
→ LangChain
→ LangGraph
→ MCP
→ Multi-Agent Systems
```

---

## 👨‍💻 Author

**Hari Prakash**

Computer Science & Engineering Student

Focused on:

* Java Backend Development
* AI Engineering
* Generative AI
* Agentic AI
* RAG
* Problem Solving
* System Design

---

⭐ This repository is continuously evolving as I learn and implement new AI Agent concepts.
