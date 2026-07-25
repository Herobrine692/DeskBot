"""
DeskBot AI interface.
"""

class AI:
    def __init__(self, config, memory):
        self.config = config
        self.memory = memory

    async def ask(self, prompt: str) -> str:
        """
        Placeholder AI response.
        """
        return f"You said: {prompt}"