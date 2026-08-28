import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from tools.ToolRegistry import ToolRegistry
from tools.calculator import calculator
from tools.weather import get_weather
from tools.time import get_time







load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


calculator_schema = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Perform basic arithmetic calculations.",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {
                    "type": "number"
                },
                "b": {
                    "type": "number"
                },
                "operation": {
                    "type": "string",
                    "enum": [
                        "add",
                        "subtract",
                        "multiply",
                        "divide"
                    ]
                }
            },
            "required": ["a", "b", "operation"]
        }
    }
}

get_weather_schema = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                }
            },
            "required": ["city"]
        }
    }
}

get_time_schema = {
    "type": "function",
    "function": {
        "name": "get_time",
        "description": "Get the current local time.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
}

registry = ToolRegistry()
registry.register("calculator",calculator,calculator_schema)
registry.register("get_weather",get_weather,get_weather_schema)
registry.register("get_time",get_time,get_time_schema)


messages = [
    {
        "role": "user",
         #"content": "What is the weather in Chennai?"
        # "content": "Calculate 125 * 48"
        # "content": "What time is it?"
        # "content": "Calculate 25 * 40 and tell me the weather in Chennai."
        # "content": "What is an AI agent?"
        # "content": "What time is it?"
        # "content": "What is the weather in Chennai and what time is it?"
        # "content": "Calculate 125 * 48 and then tell me the weather in Chennai."
        "content": "Calculate 25 * 40 and tell me the weather in Chennai and the current time."

    }
]

max_iterations = 10

for iteration in range(max_iterations):

    print(f"\n--- Agent iteration {iteration + 1} ---")

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools= registry.get_schemas()
    )

    message = response.choices[0].message

    print("Model response:")
    print(message)

    if not message.tool_calls:
        print("Final answer:")
        print(message.content)
        break

    messages.append(message)

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        tool = registry.get(tool_name)
        if(tool is None):
            result = "Unknown tool"

        else:
            tool_function = tool["function"]
            result = tool_function(**arguments)

        print("Tool executed!")
        print("Tool:", tool_name)
        print("Result:", result)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": str(result)
        })
else:
    print("Agent stopped: maximum iterations reached.")
