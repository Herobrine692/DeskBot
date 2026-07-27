"""
DeskBot Chat Interface

Simple terminal chat for interacting with DeskBot.
"""


class Chat:

    def __init__(self, ai, memory):
        self.ai = ai
        self.memory = memory


    async def start(self):

        print("\nDeskBot Chat")
        print("Type 'exit' to quit.\n")

        while True:

            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            response = await self.ai.ask(user_input)

            print(f"\nDeskBot: {response}\n")

            self.memory.remember(
                f"User: {user_input}\nDeskBot: {response}"
            )