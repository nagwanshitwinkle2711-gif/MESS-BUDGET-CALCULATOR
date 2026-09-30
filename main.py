from budget import budget_menu
from expenses import expense_menu
from report import show_report
def main():
    while True:
        print("\n")
        print("========================")
        print(" MESS BUDGET CALCULATOR ")
        print("========================")

        print("1. Budget Management")
        print("2. Expense Management")
        print("3. Budget Report")
        print("4. Exit")

        choice = input("enter your chhoice:")
        if choice == "1":
             budget_menu()
        elif choice == "2":
             expense_menu()
        elif choice == "3":
            show_report()
        elif choice == "4":
            print("Thank you for using Mess Budget Calculator!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
