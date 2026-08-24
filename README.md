🧠 What I Am Learning

This repository focuses on understanding the fundamentals behind AI Agent systems:

Large Language Models (LLMs)
LLM API integration
Prompting
Environment variables
OpenAI-compatible APIs
Tool calling
Function calling
Tool execution
Passing tool results back to the LLM
Agent decision-making
Multi-step agent workflows
🛠️ Technologies Used
Python
OpenAI Python SDK
Groq API
uv
Git
GitHub
📁 Project Structure
main.py

Contains the main application logic for interacting with the LLM and handling tool calls.

tools.py

Contains custom tools/functions that can be executed when requested by the LLM.

pyproject.toml

Contains project dependencies and Python project configuration.

uv.lock

Locks the exact dependency versions used by the project.

.env

Stores environment variables such as API keys.

.env is excluded from Git using .gitignore and should never be committed to GitHub.

🔐 Environment Setup

Create a .env file in the project root:

Never hard-code API keys directly inside Python source code.

⚙️ Installation

This project uses uv for Python environment and dependency management.

1. Clone the repository
2. Create the virtual environment
3. Activate the environment

Windows PowerShell:

4. Install dependencies
5. Configure environment variables

Create a .env file:

6. Run the application
🔧 Tool Calling Architecture

The current implementation demonstrates the basic tool-calling workflow.

🧮 Example Tool

The calculator tool supports operations such as:

The LLM generates structured arguments such as:

The application executes the corresponding Python function and returns:

The result can then be provided back to the LLM to generate the final response.

📚 Learning Roadmap

This repository will evolve incrementally as I learn more about AI Agents.

Completed
 Python environment setup
 LLM API integration
 Environment variable configuration
 Model discovery
 Basic LLM prompting
 Function/tool definition
 Tool calling
 Tool execution
 Returning tool results
 Final LLM response
Next Steps
 Multiple tools
 Tool selection
 Better tool schemas
 Multi-step agent execution
 Agent loops
 Memory
 Structured outputs
 Error handling
 Web search tool
 Database tool
 RAG integration
 LangChain
 LangGraph
 MCP
 Multi-agent systems
 Production-ready agent architecture
🎯 Goal

The goal of this repository is to build a strong practical understanding of AI Agents by implementing the concepts from the ground up instead of relying entirely on high-level frameworks.

The project will gradually evolve from simple LLM calls into more capable agent systems involving:

📝 Learning Philosophy

Each feature is implemented incrementally and documented through Git commits.

The repository is intended to serve as a practical record of my progress in:

AI Engineering
LLM application development
Agentic AI
Tool calling
RAG
Multi-agent systems
🔒 Security

Never commit:

The .env file is intentionally excluded using .gitignore.

If an API key is accidentally pushed to GitHub, revoke it immediately and generate a new key.
