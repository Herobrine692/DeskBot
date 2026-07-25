import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from brain.memory import Memory
from brain.self_improve import SelfImprover


config = Config()

memory = Memory(config)

improver = SelfImprover(
    config,
    memory
)

improver.suggest(
    "Improve file handling"
)

print(
    improver.list_suggestions()
)