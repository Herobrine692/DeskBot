import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from modules.file_manager import FileManager


config = Config()

files = FileManager(config)


test_file = "test.txt"


files.write_file(
    test_file,
    "Hello from DeskBot!"
)


print(
    "Exists:",
    files.exists(test_file)
)


print(
    "Contents:",
    files.read_file(test_file)
)


print(
    "Directory:",
    files.list_directory(".")
)