import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from ui.tray import Tray


config = Config()

tray = Tray(config)

print(tray.status())

tray.start()

print(tray.status())

tray.stop()

print(tray.status())