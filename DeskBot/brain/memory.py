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

        self.conn = sqlite3.connect(
            self.database
        )

        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                content TEXT
            )
            """
        )

        self.conn.commit()


    def remember(self, content: str):
        """
        Store a memory.
        """

        cursor = self.conn.cursor()

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

        self.conn.commit()


    def recall(self, limit=10):
        """
        Retrieve recent memories.
        """

        cursor = self.conn.cursor()

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


    def search(self, query):
        """
        Search stored memories for related information.
        """

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT content 
            FROM memories
            WHERE content LIKE ?
            """,
            (f"%{query}%",)
        )

        results = cursor.fetchall()

        return [
            row[0]
            for row in results
        ]