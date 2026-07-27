"""
DeskBot Planner

Controls what DeskBot does in the background.
"""

import asyncio
from datetime import datetime


class Planner:

    def __init__(self, config, ai, memory):
        self.config = config
        self.ai = ai
        self.memory = memory

        self.last_tick = None


    async def tick(self):
        """
        Runs repeatedly while DeskBot is active.

        Later this will handle:
        - scheduled tasks
        - reminders
        - self-improvement checks
        - background monitoring
        """

        now = datetime.now()

        # Only print once every 10 seconds
        if (
            self.last_tick is None
            or (now - self.last_tick).seconds >= 10
        ):
            print(
                f"DeskBot heartbeat: {now.strftime('%H:%M:%S')}"
            )

            self.last_tick = now

        await asyncio.sleep(0)


    def create_plan(self, task):
        """
        Create a simple task plan.
        """

        return [
            f"Understand: {task}",
            "Process information",
            "Provide response"
        ]