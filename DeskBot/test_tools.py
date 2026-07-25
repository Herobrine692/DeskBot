import asyncio

from brain.tools import ToolManager


def hello(name):
    return f"Hello, {name}!"


async def main():

    tools = ToolManager()

    tools.register(
        "hello",
        hello
    )

    print(tools.available_tools())

    result = await tools.run(
        "hello",
        "Clark"
    )

    print(result)


asyncio.run(main())