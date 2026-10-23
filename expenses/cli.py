"""Command line: python -m expenses.cli add|list|report ..."""
import argparse
from datetime import date
from pathlib import Path

from .report import by_category, in_month, total
from .store import Expense, Store

DEFAULT_FILE = Path("expenses.json")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="expenses")
    parser.add_argument("--file", type=Path, default=DEFAULT_FILE)
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add")
    add.add_argument("category")
    add.add_argument("amount", type=float)
    add.add_argument("--note", default="")
    add.add_argument("--date", default=date.today().isoformat())

    sub.add_parser("list")

    report = sub.add_parser("report")
    report.add_argument("--month", help="YYYY-MM")

    args = parser.parse_args(argv)
    store = Store(args.file)

    if args.command == "add":
        store.add(Expense(args.date, args.category, args.amount, args.note))
        print(f"added {args.amount:.2f} to {args.category}")
    elif args.command == "list":
        for e in store.load():
            print(f"{e.date}  {e.category:<12} {e.amount:>10.2f}  {e.note}")
    elif args.command == "report":
        expenses = store.load()
        if args.month:
            expenses = in_month(expenses, args.month)
        for category, amount in sorted(by_category(expenses).items()):
            print(f"{category:<12} {amount:>10.2f}")
        print(f"{'TOTAL':<12} {total(expenses):>10.2f}")


if __name__ == "__main__":
    main()
