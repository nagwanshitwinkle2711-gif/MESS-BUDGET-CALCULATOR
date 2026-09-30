import data
from validation import get_amount

def set_budget():
    print("\n===== SET MONTHLY BUDGET =====")
    data.budget = get_amount()
    print("Monthly budget set succesfully!")
    
def view_budget():
    print("\n===== MONTHLY BUDGET =====")
    print("Your monthly mess budget is: rs",data.budget)
    
def budget_menu():
    while True:
        print("\n===== BUDGET MANAGEMENT =====")
        print("1. Set Monthly Budget")
        print("2. View Budget")
        print("3. Back")

        choice = input("enter your choice:")
        if choice == "1":
            set_budget()

        elif choice == "2":
            view_budget()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please try again.")
