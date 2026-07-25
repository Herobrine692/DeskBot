"""
DeskBot Self Improvement System

Handles tracking and planning improvements.
"""


class SelfImprover:

    def __init__(self, config, memory):
        self.config = config
        self.memory = memory

        self.improvements = []


    def suggest(self, idea):
        """
        Add an improvement suggestion.
        """

        self.improvements.append(idea)


    def list_suggestions(self):
        """
        Return current suggestions.
        """

        return self.improvements


    def record_change(self, change):
        """
        Record a completed improvement.
        """

        self.memory.remember(
            f"Self improvement completed: {change}"
        )