import data
from validation import get_amount

def add_expense():
    print("\n===== ADD EXPENSE =====")
    name = input("Enter expense name: ")
    if name == "":
        print("Expense name cannot be empty.")
        return

    amount = get_amount()
    expense = {
        "name": name,
        "amount": amount
    }

    data.expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    print("\n===== MY EXPENSES =====")
    if len(data.expenses) == 0:
        print("No expenses found.")
    else:
        total = 0
        for i in range(len(data.expenses)):
            print(
                i + 1,
                ".",
                data.expenses[i]["name"],
                "- ₹",
                data.expenses[i]["amount"]
            )

            total = total + data.expenses[i]["amount"]
        print("-------------------------")
        print("Total Expenses: ₹", total)

def delete_expense():
    view_expenses()
    if len(data.expenses) == 0:
        return
    number = input("\nEnter expense number to delete: ")
    if number.isdigit():
        number = int(number)
        if number >= 1 and number <= len(data.expenses):
            deleted = data.expenses.pop(number - 1)
            print(deleted["name"], "deleted successfully.")
        else:
            print("Invalid expense number.")
    else:
        print("Please enter a valid number.")

def expense_menu():
    while True:

        print("\n===== EXPENSE MANAGEMENT =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")
