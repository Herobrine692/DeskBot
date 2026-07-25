"""
DeskBot File Manager

Handles safe file operations.
"""

from pathlib import Path


class FileManager:

    def __init__(self, config):
        self.config = config


    def exists(self, path):
        """
        Check if a file or folder exists.
        """

        return Path(path).exists()


    def list_directory(self, path):
        """
        List items inside a directory.
        """

        directory = Path(path)

        if not directory.exists():
            return []

        return [
            item.name
            for item in directory.iterdir()
        ]


    def read_file(self, path):
        """
        Read text from a file.
        """

        file = Path(path)

        if not file.exists():
            return None

        return file.read_text(
            encoding="utf-8"
        )


    def write_file(self, path, content):
        """
        Write text to a file.
        """

        file = Path(path)

        file.write_text(
            content,
            encoding="utf-8"
        )

        return True