"""Keeps expenses in a JSON file."""
import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Expense:
    date: str  # YYYY-MM-DD
    category: str
    amount: float
    note: str = ""


class Store:
    def __init__(self, path: Path):
        self.path = Path(path)

    def load(self) -> list[Expense]:
        if not self.path.exists():
            return []
        return [Expense(**row) for row in json.loads(self.path.read_text(encoding="utf-8"))]

    def save(self, expenses: list[Expense]) -> None:
        self.path.write_text(
            json.dumps([asdict(e) for e in expenses], ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add(self, expense: Expense) -> None:
        expenses = self.load()
        expenses.append(expense)
        self.save(expenses)
