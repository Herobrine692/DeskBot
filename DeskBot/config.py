from pathlib import Path


class Config:

    def __init__(self):

        self.root = Path(__file__).parent

        # Memory directories
        self.memory_dir = self.root / "memory"
        self.logs_dir = self.memory_dir / "logs"
        self.vector_dir = self.memory_dir / "vector_store"

        self.memory_dir.mkdir(exist_ok=True)
        self.logs_dir.mkdir(exist_ok=True)
        self.vector_dir.mkdir(exist_ok=True)

        # Sandbox directories
        self.sandbox_dir = self.root / "sandbox"
        self.sandbox_temp = self.sandbox_dir / "temp"
        self.sandbox_tests = self.sandbox_dir / "tests"

        self.sandbox_dir.mkdir(exist_ok=True)
        self.sandbox_temp.mkdir(exist_ok=True)
        self.sandbox_tests.mkdir(exist_ok=True)

        # AI settings
        self.model = "gpt-5"