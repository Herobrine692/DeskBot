"""
DeskBot Terminal Module

Handles command-line operations.
"""

import subprocess


class Terminal:

    def __init__(self, config):
        self.config = config


    def run_command(self, command):
        """
        Run a terminal command.
        """

        try:
            result = subprocess.run(
                command,
                shell=True,
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
                "error": "Command timed out."
            }