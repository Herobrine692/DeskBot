"""
DeskBot Tool System

Manages tools that DeskBot can use.
"""


class ToolManager:

    def __init__(self):
        self.tools = {}


    def register(self, name, function):
        """
        Add a tool to DeskBot.
        """

        self.tools[name] = function


    def available_tools(self):
        """
        Return a list of available tools.
        """

        return list(self.tools.keys())


    async def run(self, name, *args, **kwargs):
        """
        Run a registered tool.
        """

        if name not in self.tools:
            return f"Tool '{name}' does not exist."

        result = self.tools[name](
            *args,
            **kwargs
        )

        return result