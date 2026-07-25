import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

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

    print("Available tools:")
    print(tools.available_tools())

    result = await tools.run(
        "hello",
        "Clark"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())