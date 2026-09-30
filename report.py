import data
def show_report():
    print("\n======= MESS BUDGET REPORT =======")
    total_expenses = 0
    for expense in data.expenses:
          total_expenses = total_expenses=expense["amount"]
    remaining_budget = data.budget - total_expenses
    print("Monthly Budget :","rs.",data.budget)
    print("Total Expenses:","rs",total_expenses)
    print("Remaining Budget:","rs",remaining_budget)
    if len(data.expenses) > 0:
          average = total_expenses/len(data.expenses)
          print("Average Expense:","rs",round(average,2))
    else:
        print("Budget Status :Within Budget")
    if remaining_budget >= 0:
        print("Budget Status :Within Budget")
    else:
        print("Budget Status :Budget Exceeded")
    print("====================================")
