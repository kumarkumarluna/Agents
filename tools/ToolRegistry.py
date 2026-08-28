from json import tool


class ToolRegistry:

    def __init__(self):
        self.tools = {}
        self.tool_schema = {}

    def register(self, name, function, schema):
        self.tools[name] = {
            "function": function,
            "schema": schema
        }

    def get(self, name):
        return self.tools.get(name)

    def get_schemas(self):
        return [
            tool["schema"]
            for tool in self.tools.values()
        ]