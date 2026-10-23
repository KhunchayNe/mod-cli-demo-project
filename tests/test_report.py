import unittest

from expenses.report import by_category, in_month, total
from expenses.store import Expense

EXPENSES = [
    Expense("2026-10-01", "food", 120.0),
    Expense("2026-10-02", "food", 80.0),
    Expense("2026-10-03", "travel", 45.5),
    Expense("2026-09-30", "food", 60.0),
]


class ReportTest(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total(EXPENSES), 305.5)

    def test_by_category_adds_up(self):
        self.assertEqual(by_category(EXPENSES), {"food": 260.0, "travel": 45.5})

    def test_in_month(self):
        self.assertEqual(len(in_month(EXPENSES, "2026-10")), 3)


if __name__ == "__main__":
    unittest.main()
