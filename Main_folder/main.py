# # import os
# #
# # from dotenv import load_dotenv
# # from openai import OpenAI
# #
# # load_dotenv()
# #
# # client = OpenAI(
# #     api_key=os.getenv("XAI_API_KEY"),
# #     base_url="https://api.x.ai/v1",
# # )
# #
# # response = client.responses.create(
# #     model="grok-4.6",
# #     input="Explain what an AI agent is in one sentence."
# # )
# #
# # print(response.output_text)
#
# # import os
# # from dotenv import load_dotenv
# #
# # load_dotenv()
# #
# # key = os.getenv("XAI_API_KEY")
# #
# # if key:
# #     print("API key found")
# #     print("Starts with:", key[:4])
# #     print("Key length:", len(key))
# # else:
# #     print("API key NOT found")
#
#
# # import os
# #
# # from dotenv import load_dotenv
# # from openai import OpenAI
# #
# # load_dotenv()
# #
# # client = OpenAI(
# #     api_key=os.getenv("GROQ_API_KEY"),
# #     base_url="https://api.groq.com/openai/v1",
# # )
# #
# # response = client.chat.completions.create(
# #     model="llama-3.3-70b-versatile",
# #     messages=[
# #         {
# #             "role": "user",
# #             "content": "Explain what an AI agent is in one sentence."
# #         }
# #     ]
# # )
#
# #print(response.choices[0].message.content)
#
# # import os
# # from dotenv import load_dotenv
# # from openai import OpenAI
# #
# # load_dotenv()
# #
# # client = OpenAI(
# #     api_key=os.getenv("GROQ_API_KEY"),
# #     base_url="https://api.groq.com/openai/v1"
# # )
# #
# # models = client.models.list()
# #
# # for model in models.data:
# #     print(model.id)
#
#
# # import os
# #
# # from dotenv import load_dotenv
# # from openai import OpenAI
# #
# # load_dotenv()
# #
# # client = OpenAI(
# #     api_key=os.getenv("GROQ_API_KEY"),
# #     base_url="https://api.groq.com/openai/v1",
# # )
# #
# # response = client.chat.completions.create(
# #     model="openai/gpt-oss-20b",
# #     messages=[
# #         {
# #             "role": "user",
# #             "content": "Explain what an AI agent is in one sentence."
# #         }
# #     ]
# # )
# #
# # print(response.choices[0].message.content)
#
#
# # from tools import calculator
# #
# # result = calculator(25,37,"multiply")
# # print(result)
#
# import os
# import json
#
# from dotenv import load_dotenv
# from openai import OpenAI
#
# from tools.tools import calculator
#
# load_dotenv()
#
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY"),
#     base_url="https://api.groq.com/openai/v1",
# )
#
#
# tools = [
#     {
#         "type": "function",
#         "function": {
#             "name": "calculator",
#             "description": "Perform basic arithmetic calculations.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "a": {
#                         "type": "number",
#                         "description": "First number"
#                     },
#                     "b": {
#                         "type": "number",
#                         "description": "Second number"
#                     },
#                     "operation": {
#                         "type": "string",
#                         "enum": [
#                             "add",
#                             "subtract",
#                             "multiply",
#                             "divide"
#                         ],
#                         "description": "Mathematical operation to perform"
#                     }
#                 },
#                 "required": ["a", "b", "operation"]
#             }
#         }
#     }
# ]
#
#
# messages = [
#     {
#         "role": "user",
#         "content": "Calculate 125 * 48 and then tell me whether the result is even or odd."
#     }
# ]
#
#
# response = client.chat.completions.create(
#     model="openai/gpt-oss-20b",
#     messages=messages,
#     tools=tools
# )
#
#
# message = response.choices[0].message
#
# print("Model response:")
# print(message)
#
# # if message.tool_calls:
# #     for tool_call in message.tool_calls:
# #
# #         tool_name = tool_call.function.name
# #
# #         arguments = json.loads(
# #             tool_call.function.arguments
# #         )
# #
# #         if tool_name == "calculator":
# #             result = calculator(
# #                 arguments["a"],
# #                 arguments["b"],
# #                 arguments["operation"]
# #             )
# #
# #             print("Tool executed!")
# #             print("Result:", result)
#
# message = response.choices[0].message
#
# if message.tool_calls:
#
#     messages.append(message)
#
#     for tool_call in message.tool_calls:
#
#         tool_name = tool_call.function.name
#
#         arguments = json.loads(
#             tool_call.function.arguments
#         )
#
#         if tool_name == "calculator":
#
#             result = calculator(
#                 arguments["a"],
#                 arguments["b"],
#                 arguments["operation"]
#             )
#
#             messages.append({
#                 "role": "tool",
#                 "tool_call_id": tool_call.id,
#                 "content": str(result)
#             })
#
#
#     final_response = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=messages,
#         tools=tools
#     )
#
#     print("Final answer:")
#     print(final_response.choices[0].message.content)
#
# else:
#
#     print("Final answer:")
#     print(message.content)












import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from tools.tools import calculator

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)


tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform basic arithmetic calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "First number"
                    },
                    "b": {
                        "type": "number",
                        "description": "Second number"
                    },
                    "operation": {
                        "type": "string",
                        "enum": [
                            "add",
                            "subtract",
                            "multiply",
                            "divide"
                        ],
                        "description": "Mathematical operation to perform"
                    }
                },
                "required": ["a", "b", "operation"]
            }
        }
    }
]


messages = [
    {
        "role": "user",
        "content": "Calculate 125 * 48 and then tell me whether the result is even or odd."
    }
]


response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=messages,
    tools=tools
)


message = response.choices[0].message

print("Model response:")
print(message)


if message.tool_calls:

    # Add the assistant's tool-call message
    messages.append(message)

    for tool_call in message.tool_calls:

        tool_name = tool_call.function.name

        arguments = json.loads(
            tool_call.function.arguments
        )

        if tool_name == "calculator":

            result = calculator(
                arguments["a"],
                arguments["b"],
                arguments["operation"]
            )

            print("Tool executed!")
            print("Result:", result)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })


    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        tools=tools
    )

    print("Final answer:")
    print(final_response.choices[0].message.content)

else:

    print("Final answer:")
    print(message.content)