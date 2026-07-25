import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).parent.parent)
)

from config import Config
from modules.code_runner import CodeRunner


config = Config()

runner = CodeRunner(config)


result = runner.run_python(
    """
print("Hello from DeskBot sandbox!")
"""
)


print(result)