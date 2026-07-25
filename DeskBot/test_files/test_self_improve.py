from brain.self_improve import SelfImprover
from config import Config
from brain.memory import Memory


config = Config()
memory = Memory(config)

ai = SelfImprover(
    config,
    memory
)

ai.suggest(
    "Improve file handling"
)

print(ai.list_suggestions())