"""
DeskBot AI Core

Handles reasoning, memory, planning, and tools.
"""


class AI:

    def __init__(self, memory, planner, tools):
        self.memory = memory
        self.planner = planner
        self.tools = tools


    async def ask(self, prompt):
        """
        Process a user request.
        """

        # Retrieve previous context
        memories = self.memory.search(prompt)

        # Create a plan
        plan = self.planner.create_plan(prompt)

        # Generate response
        response = self.generate_response(
            prompt,
            memories,
            plan
        )

        return response


    def generate_response(self, prompt, memories, plan):
        """
        Temporary response generator.
        This will later be replaced with an LLM.
        """

        response = f"You said: {prompt}"

        if memories:
            response += "\nI found related memories."

        if plan:
            response += "\nI created a plan."

        return response