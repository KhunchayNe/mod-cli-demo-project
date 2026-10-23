"""Summaries of expenses."""
from collections import defaultdict

from .store import Expense


def total(expenses: list[Expense]) -> float:
    return sum(e.amount for e in expenses)


def by_category(expenses: list[Expense]) -> dict[str, float]:
    sums: dict[str, float] = defaultdict(float)
    for e in expenses:
        sums[e.category] = e.amount  # BUG (deliberate, for the demo): overwrites instead of adding
    return dict(sums)


def in_month(expenses: list[Expense], month: str) -> list[Expense]:
    """Expenses whose date falls in `month` (YYYY-MM)."""
    return [e for e in expenses if e.date.startswith(month)]
