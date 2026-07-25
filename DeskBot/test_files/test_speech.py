import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from modules.speech import Speech


config = Config()

speech = Speech(config)

speech.speak(
    "Hello, this is DeskBot."
)

print(
    speech.listen()
)