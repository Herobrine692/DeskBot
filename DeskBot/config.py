from pathlib import Path


class Config:
    def __init__(self):
        self.root = Path(__file__).parent

        self.memory_dir = self.root / "memory"
        self.logs_dir = self.memory_dir / "logs"
        self.vector_dir = self.memory_dir / "vector_store"

        self.memory_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)
        self.vector_dir.mkdir(exist_ok=True)

        self.model = "gpt-5"