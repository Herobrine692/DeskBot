"""
DeskBot Memory System

Handles storing and retrieving information.
"""

import sqlite3
from pathlib import Path
from datetime import datetime


class Memory:

    def __init__(self, config):
        self.config = config

        self.database = (
            Path(config.memory_dir)
            / "memory.db"
        )

        self.connection = sqlite3.connect(
            self.database
        )

        self.create_tables()

    def create_tables(self):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                content TEXT
            )
            """
        )

        self.connection.commit()


    def remember(self, content: str):
        """
        Store a memory.
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            INSERT INTO memories
            (timestamp, content)
            VALUES (?, ?)
            """,
            (
                datetime.now().isoformat(),
                content
            )
        )

        self.connection.commit()


    def recall(self, limit=10):
        """
        Retrieve recent memories.
        """

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT content
            FROM memories
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return [
            row[0]
            for row in cursor.fetchall()
        ]