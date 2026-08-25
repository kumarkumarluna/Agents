def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."


def calculate(a: float, b: float, operation: str) -> float:
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

    raise ValueError("Unknown operation")