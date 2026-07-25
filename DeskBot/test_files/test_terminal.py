import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from modules.terminal import Terminal


config = Config()

terminal = Terminal(config)

result = terminal.run_command(
    "echo Hello from DeskBot terminal"
)

print(result)