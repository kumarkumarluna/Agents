Absolutely. The content you provided has a lot of unnecessary empty code fences and repetition. Here is a **clean, GitHub-ready README.md** for Lesson 5, while keeping the technical concepts and learning progression intact.

# 🤖 AI Agent Fundamentals

A step-by-step implementation of **AI Agent fundamentals using Python, LLM APIs, tool calling, and agent loops**.

Each Git branch represents a lesson and introduces an important concept involved in building AI agent systems from the ground up.

---

## 📚 Current Lesson: Lesson 5 — Tool Registry

**Branch:**

```text
lesson-5-tool-registry
```

This lesson improves the agent architecture by introducing a **Tool Registry**.

Instead of using multiple `if/elif` conditions to determine which Python function should execute, the agent maintains a registry that maps **tool names → Python functions**.

---

## 🎯 What I Am Learning

In this lesson, I am learning:

* Tool Registry
* Dynamic tool lookup
* Mapping tool names to Python functions
* Dynamic function execution
* `**kwargs` / dictionary unpacking
* Separation between tool definitions and tool execution
* Improving agent scalability
* Reducing hard-coded tool dispatch logic
* Handling unknown tools
* Integrating the registry into an agent loop

---

# 🧠 What Is a Tool Registry?

A **Tool Registry** is a mapping between a tool's name and the Python function responsible for executing that tool.

For example:

```python
tool_registry = {
    "calculator": calculator,
    "get_weather": get_weather,
    "get_time": get_time
}
```

When the LLM requests a tool by name, the agent can use the registry to dynamically locate the corresponding Python function.

The basic idea is:

```text
LLM Tool Name
      ↓
Tool Registry
      ↓
Python Function
      ↓
Tool Result
```

---

# 🔄 Before Tool Registry

Previously, the agent could use hard-coded conditional logic:

```python
if tool_name == "calculator":
    result = calculator(
        arguments["a"],
        arguments["b"],
        arguments["operation"]
    )

elif tool_name == "get_weather":
    result = get_weather(
        arguments["city"]
    )

elif tool_name == "get_time":
    result = get_time()

else:
    result = "Unknown tool"
```

This works, but it does not scale well.

If the agent has 20 tools, the execution logic can become a large collection of `if/elif` statements.

---

# 🚀 After Tool Registry

The conditional dispatch logic can be replaced with a registry:

```python
tool_registry = {
    "calculator": calculator,
    "get_weather": get_weather,
    "get_time": get_time
}
```

The agent can dynamically look up the requested function:

```python
tool_function = tool_registry.get(tool_name)
```

If the tool exists:

```python
result = tool_function(**arguments)
```

If the tool does not exist:

```python
result = "Unknown tool"
```

This makes the execution mechanism independent of the number of tools.

---

# 🔍 How Dynamic Tool Execution Works

Suppose the LLM requests:

```python
tool_name = "calculator"
```

The agent performs:

```python
tool_function = tool_registry.get("calculator")
```

The registry returns the Python function:

```python
calculator
```

Suppose the LLM also provides:

```python
arguments = {
    "a": 25,
    "b": 40,
    "operation": "multiply"
}
```

The agent can execute:

```python
tool_function(**arguments)
```

This is equivalent to:

```python
calculator(
    a=25,
    b=40,
    operation="multiply"
)
```

The calculator returns:

```text
1000
```

---

# 🏗️ Agent Architecture

The current architecture is:

```text
                         USER
                           │
                           ▼
                    ┌─────────────┐
                    │     LLM     │
                    └──────┬──────┘
                           │
                           │ Tool Call
                           ▼
                  ┌─────────────────┐
                  │  Tool Registry  │
                  └────────┬────────┘
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
        calculator    get_weather    get_time
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                     Tool Result
                           │
                           ▼
                          LLM
                           │
                           ▼
                     Final Answer
```

---

# 🧩 Available Tools

The current agent contains three tools.

## 1. Calculator

**Tool name:**

```text
calculator
```

**Purpose:**

Performs basic arithmetic calculations.

**Supported operations:**

```text
add
subtract
multiply
divide
```

Example:

```text
25 × 40
```

Result:

```text
1000
```

---

## 2. Weather

**Tool name:**

```text
get_weather
```

**Purpose:**

Returns the weather information for a city.

Example:

```text
What's the weather in Chennai?
```

The LLM can generate a tool call containing:

```python
{
    "city": "Chennai"
}
```

The registry then maps `get_weather` to the corresponding Python function.

---

## 3. Time

**Tool name:**

```text
get_time
```

**Purpose:**

Returns the current local time.

This tool does not require arguments.

Example:

```text
What is the current time?
```

---

# 🔗 Tool Definitions vs Tool Registry

One of the most important concepts in this lesson is the distinction between **tool definitions** and the **tool registry**.

They serve different purposes.

## Tool Definitions

The `tools` configuration tells the LLM what tools are available.

It describes:

* Tool name
* Tool purpose
* Parameters
* Parameter types
* Required arguments

For example:

```python
tools = [
    # Tool definitions
]
```

The LLM uses these definitions to decide:

```text
Which tool should I call?
What arguments should I provide?
```

---

## Tool Registry

The `tool_registry` tells the Python application which function should actually execute.

```python
tool_registry = {
    "calculator": calculator,
    "get_weather": get_weather,
    "get_time": get_time
}
```

Therefore:

```text
Tool Definitions
        ↓
Tell the LLM WHAT tools are available


Tool Registry
        ↓
Tell Python WHICH function to execute
```

This separation is an important architectural concept.

---

# 🔄 Agent Execution Flow

For example, consider the user request:

```text
Calculate 25 * 40 and tell me the weather in Chennai and the current time.
```

The agent may execute multiple iterations.

## Iteration 1 — Calculator

The LLM requests:

```text
calculator
```

Arguments:

```json
{
    "a": 25,
    "b": 40,
    "operation": "multiply"
}
```

Registry lookup:

```python
tool_registry.get("calculator")
```

Execution:

```python
calculator(**arguments)
```

Result:

```text
1000
```

---

## Iteration 2 — Weather

The LLM requests:

```text
get_weather
```

Arguments:

```json
{
    "city": "Chennai"
}
```

The registry finds the corresponding Python function:

```python
get_weather
```

Execution:

```python
get_weather(**arguments)
```

Result:

```text
32°C, sunny
```

> The exact weather result depends on the implementation of the weather tool.

---

## Iteration 3 — Time

The LLM requests:

```text
get_time
```

The tool requires no arguments.

Execution:

```python
get_time()
```

Result:

```text
Current local time
```

---

## Iteration 4 — Final Answer

Once the LLM has all the required tool results, it produces the final response to the user.

```text
Tool Calls
    ↓
Tool Results
    ↓
LLM
    ↓
Final Answer
```

---

# 💡 Why Tool Registry Matters

Without a registry:

```text
Tool 1 → if
Tool 2 → elif
Tool 3 → elif
Tool 4 → elif
Tool 5 → elif
...
```

With a registry:

```text
Tool Name
    │
    ▼
Tool Registry
    │
    ▼
Python Function
```

The registry provides a cleaner separation between:

1. **What tool the LLM requested**
2. **Which Python function implements that tool**
3. **How that function is executed**

---

# ➕ Adding a New Tool

Suppose a new `search` tool is added:

```python
from tools.search import search
```

The registry can be extended:

```python
tool_registry = {
    "calculator": calculator,
    "get_weather": get_weather,
    "get_time": get_time,
    "search": search
}
```

The core execution logic does not need another `elif`.

This is the main scalability advantage of the registry pattern.

---

# 🛡️ Handling Unknown Tools

The registry also provides a simple way to handle invalid or unknown tool names.

```python
tool_function = tool_registry.get(tool_name)

if tool_function:
    result = tool_function(**arguments)
else:
    result = "Unknown tool"
```

For example:

```text
LLM requests:
"send_email"

        ↓

Registry lookup

        ↓

No matching function

        ↓

"Unknown tool"
```

This prevents the agent from attempting to execute a function that does not exist in the registry.

---

# 🛠️ Technologies Used

* Python 3.13
* OpenAI Python SDK
* Groq API
* OpenAI-compatible API
* uv
* python-dotenv
* Git
* GitHub

---

# 📁 Project Structure

```text
Agents/
│
├── Main_folder/
│   ├── agent_loop.py
│   ├── main.py
│   └── multi_agent_call_Main.py
│
├── tools/
│   ├── calculator.py
│   ├── weather.py
│   └── time.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── README.md
└── uv.lock
```

> Keep `.env` out of Git. API keys and other secrets should never be committed to the repository.

---

# ▶️ Running the Agent

## 1. Install Dependencies

Synchronize the project environment using `uv`:

```bash
uv sync
```

## 2. Configure Environment Variables

Create a `.env` file and add the required API credentials.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit the `.env` file.

---

## 3. Run the Agent

```bash
uv run python Main_folder/agent_loop.py
```

The agent will:

1. Send the user request to the LLM.
2. Allow the LLM to select a tool.
3. Extract the requested tool name.
4. Look up the function in the tool registry.
5. Execute the function.
6. Send the tool result back to the LLM.
7. Continue the agent loop.
8. Stop when the LLM produces a final answer or the iteration limit is reached.

---

# 🧠 Key Learning

The main lesson from this branch is:

> **The LLM decides which tool should be used, while the Tool Registry allows the Python agent to dynamically locate and execute the corresponding function.**

The registry separates **tool selection** from **tool execution** and makes the agent easier to extend.

The important mental model is:

```text
                    LLM
                     │
                     │ decides
                     ▼
                 Tool Name
                     │
                     ▼
              Tool Registry
                     │
                     │ lookup
                     ▼
              Python Function
                     │
                     │ execute
                     ▼
                Tool Result
                     │
                     ▼
                    LLM
```

---

# 📈 Learning Roadmap

```text
Lesson 1
│
├── LLM API Basics
│
▼
Lesson 2
│
├── Tool Calling
│
▼
Lesson 3
│
├── Multiple Tool Calling
│
▼
Lesson 4
│
├── Agent Loop
│
▼
Lesson 5 ← CURRENT
│
├── Tool Registry
│
▼
Next Lessons
│
├── Dynamic Tool Registration
├── Better Agent Architecture
├── Error Handling
├── Structured Tool Execution
├── Memory
├── Planning
├── RAG
├── Multi-Agent Systems
└── Production AI Agents
```

---

# 🚀 Long-Term Goal

The goal of this repository is to understand how modern AI agent systems work **under the hood**, rather than simply using an agent framework without understanding its internal mechanisms.

The core architecture being developed is:

```text
LLM
 ↓
Decision Making
 ↓
Tool Selection
 ↓
Tool Calling
 ↓
Tool Registry
 ↓
Tool Execution
 ↓
Tool Results
 ↓
Agent Loop
 ↓
Final Answer
```

These fundamentals will later be used to build more advanced systems involving:

* RAG
* Memory
* Planning
* Multi-Agent Systems
* MCP
* Production-oriented AI applications

---

## ⭐ Key Takeaway

A Tool Registry is a simple architectural pattern, but it solves an important problem:

```text
Hard-coded dispatch logic
            ↓
     Tool Registry
            ↓
Dynamic tool execution
```

Instead of teaching the agent loop how to execute every individual tool, the registry provides a **central mapping between tool names and executable Python functions**.

That makes the system easier to extend, maintain, and reason about as the number of tools grows.
