"""
DeskBot Code Runner

Runs code inside the sandbox environment.
"""

import subprocess
from pathlib import Path


class CodeRunner:

    def __init__(self, config):
        self.config = config


    def run_python(self, code):
        """
        Run Python code inside the sandbox.
        """

        file_path = (
            Path(self.config.sandbox_temp)
            / "temp_script.py"
        )

        file_path.write_text(
            code,
            encoding="utf-8"
        )

        try:
            result = subprocess.run(
                [
                    "python",
                    str(file_path)
                ],
                capture_output=True,
                text=True,
                timeout=10
            )

            return {
                "success": result.returncode == 0,
                "output": result.stdout,
                "error": result.stderr
            }

        except subprocess.TimeoutExpired:

            return {
                "success": False,
                "output": "",
                "error": "Program timed out."
            }