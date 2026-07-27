"""
DeskBot
Main entry point.

This file initializes and starts every subsystem.
"""

import asyncio
import traceback

from config import Config

from brain.ai import AI
from brain.memory import Memory
from brain.planner import Planner
from brain.tools import Tools


class DeskBot:
    def __init__(self):
        print("=" * 50)
        print("              DeskBot")
        print("=" * 50)

        print("[1/3] Loading configuration...")
        self.config = Config()

        print("[2/3] Loading memory...")
        self.memory = Memory(self.config)

        print("[3/3] Initializing AI...")

        self.tools = Tools()

        self.ai = None

        self.planner = Planner(
            self.config,
            self.ai,
            self.memory
        )

        self.ai = AI(
            self.memory,
            self.planner,
            self.tools
        )

        self.planner.ai = self.ai

        print("\nDeskBot is online.\n")

    async def run(self):

        from ui.chat import Chat

        chat = Chat(
            self.ai,
            self.memory
        )

        await chat.start()

async def main():
    bot = DeskBot()

    try:
        await bot.run()

    except KeyboardInterrupt:
        print("\nShutting down...")

    except Exception:
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())