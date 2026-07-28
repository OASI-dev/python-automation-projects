import csv
import os


class ExpenseTracker:
    def __init__(self,filename):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                self.expenses.append(row)

    def add_expense(self,date,category,description,amount):
        new_expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : float(amount),
        }
        self.expenses.append(new_expense)

    def save_expenses(self):
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["date", "category", "description", "amount"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(expense)

    def total_spent(self):
        return sum(expense["amount"] for expense in self.expenses)

    def total_by_category(self):
        totals = {}
        for expense in self.expenses:
            category = expense["category"]
            totals[category] = totals.get(category, 0) + expense["amount"]
        return totals

    def print_report(self):
        print("\n---Expense Report---")
        for expense in self.expenses:
            print(f"{expense['date']} | {expense['category']:<12} | "
                  f"{expense['description']:<25} | ${expense['amount']:.2f}")

        print("\n---Totals by category---")
        for category, total in self.total_by_category().items():
            print(f"{category:<12}: ${total:.2f}")

        print(f"\nTotal Spent: ${self.total_spent():.2f}")


def main():
    tracker = ExpenseTracker("expenses.csv")

    while True:
        print("\n1. Add expense")
        print("2. View Report")
        print("3. Save and exit")
        choice = input("Choose an option ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            category = input("Category: ").strip()
            description = input("Description: ").strip()
            amount = input("Amount: ").strip()
            tracker.add_expense(date, category, description, amount)
            print("Expense Added.")

        elif choice == "2":
            tracker.print_report()

        elif choice == "3":
           tracker.save_expenses() 
           print("Saved.Goodbye!")
           break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()