# Mess Budget Calculator

## 1. Project Title

**Mess Budget Calculator**

## 2. Project Overview

Mess Budget Calculator is a simple Python-based project designed to help students manage and calculate their monthly mess expenses.

Students can enter their monthly mess budget, add their daily expenses, view their expenses, and check whether they are staying within their budget.

The project is designed using basic Python concepts, making it simple and easy to understand for beginners.

## 3. Problem Statement

Students living in hostels often have to manage their monthly mess expenses. It can be difficult to keep track of how much money has been spent and how much budget is still available.

This project provides a simple way to record mess expenses and calculate the remaining budget.

## 4. Objectives

The main objectives of this project are:

* To help students manage their mess budget.
* To record different mess expenses.
* To calculate total expenses.
* To calculate the remaining budget.
* To show whether the student is within or over the budget.
* To provide a simple and easy-to-use interface.

## 5. Functional Modules

The project contains three main functional modules.

### Module 1: Budget Management

This module allows the user to:

* Set a monthly mess budget.
* View the current monthly budget.

### Module 2: Expense Management

This module allows the user to:

* Add an expense.
* View all recorded expenses.
* Delete an expense.
* Calculate total expenses.

### Module 3: Budget Report

This module displays:

* Monthly budget.
* Total expenses.
* Remaining budget.
* Average expense.
* Budget status.

The budget status shows whether the user's expenses are within the budget or the budget has been exceeded.

## 6. Features

* Simple menu-based interface.
* Set monthly mess budget.
* Add food/mess expenses.
* View recorded expenses.
* Delete expenses.
* Calculate total expenses.
* Calculate remaining budget.
* Calculate average expense.
* Check budget status.
* Basic input validation.
* Beginner-friendly Python implementation.

## 7. Technologies Used

* **Programming Language:** Python
* **Development Environment:** Visual Studio Code
* **Version Control:** Git and GitHub

## 8. Python Concepts Used

The project uses basic Python concepts such as:

* Variables
* Input and output
* `if-else` statements
* `while` loops
* `for` loops
* Functions
* Lists
* Dictionaries
* Basic input validation
* Arithmetic operations

## 9. Requirements

To run this project, you need:

* Python 3.x
* Any Python code editor such as Visual Studio Code

No external Python libraries are required.

## 10. How to Run the Project

### Step 1

Install Python 3.x on your computer.

### Step 2

Download or clone this project from GitHub.

### Step 3

Open the project folder in Visual Studio Code.

### Step 4

Open the Python file:

```text
mess_budget_calculator.py
```

### Step 5

Run the program.

The main menu will appear:

```text
========================================
         MESS BUDGET CALCULATOR
========================================

1. Budget Management
2. Expense Management
3. Budget Report
4. Exit

Enter your choice:
```

## 11. How to Use

### Set Budget

Select:

```text
1. Budget Management
```

Then choose:

```text
1. Set Monthly Budget
```

Enter the monthly mess budget.

Example:

```text
Enter amount: 5000
```

### Add Expense

Select:

```text
2. Expense Management
```

Then choose:

```text
1. Add Expense
```

Enter the expense name and amount.

Example:

```text
Enter expense name: Lunch
Enter amount: 80
```

### View Expenses

Choose:

```text
2. View Expenses
```

The program will display all recorded expenses and their total.

### Delete Expense

Choose:

```text
3. Delete Expense
```

Enter the number of the expense you want to remove.

### View Budget Report

From the main menu, choose:

```text
3. Budget Report
```

The program displays the budget summary.

Example:

```text
========== MESS BUDGET REPORT ==========

Monthly Budget  : ₹ 5000
Total Expenses  : ₹ 3200
Remaining Budget: ₹ 1800
Average Expense : ₹ 106.67
Budget Status   : Within Budget

========================================
```

## 12. Testing

The following cases can be used to test the project:

| Test Case             | Input                        | Expected Result                         |
| --------------------- | ---------------------------- | --------------------------------------- |
| Set budget            | ₹5000                        | Budget becomes ₹5000                    |
| Add expense           | Lunch, ₹80                   | Expense is added                        |
| Add multiple expenses | Breakfast, Lunch, Dinner     | All expenses are displayed              |
| Delete expense        | Expense number 1             | Selected expense is removed             |
| View report           | Existing budget and expenses | Correct budget calculation is displayed |
| Invalid amount        | `abc`                        | Program asks for a valid number         |
| Empty expense name    | Empty input                  | Program displays an error message       |
| Exceed budget         | Expenses greater than budget | Shows "Budget Exceeded"                 |

## 13. Project Structure

```text
Mess_Budget_Calculator/
│
├── mess_budget_calculator.py
│
├── README.md
│
└── statement.md
```

## 14. Advantages

* Easy to use.
* Simple menu-based system.
* Helps students track their mess spending.
* Uses basic Python concepts.
* Easy to modify and improve.
* Does not require external libraries.

## 15. Limitations

* The current version stores data only while the program is running.
* Data is lost when the program is closed.
* It does not use a database.
* It does not have a graphical user interface.

## 16. Future Enhancements

The project can be improved in the future by adding:

* Permanent data storage using files.
* Monthly expense history.
* Different expense categories.
* Graphs and charts.
* A graphical user interface.
* Login functionality.
* Database support.
* Exporting reports to files.

## RESULTS SCREENSHOT
# MAIN PROGRAM
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/aa1c0ce7-4a5d-4d53-aef1-ca773f970cac" />
# FUNCTIONAL MODULE 1 
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/e72ca7b4-4954-46f2-8556-794458d03db2" />
# FUNCTIONAL MODULE 2
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/6077afab-b2aa-4224-95cc-027eade31fbd" />
FUNCTIONAL MODULE 3 
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/885f9266-283b-4322-bc2f-15e010307ca5" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/c499cd7f-e649-4f0a-8a6c-c0c5e720fbcb" />
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/f534e5f2-3f69-4022-b03e-db5a2ee18f42" />
# RESULTS
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/7f0fbcbe-29e9-4bc8-8900-b17b90f60101" />


## 17. Conclusion

The Mess Budget Calculator is a simple Python project that helps students manage their monthly mess expenses.

The project demonstrates the use of basic Python programming concepts such as variables, conditions, loops, functions, lists, dictionaries, and input validation.

It provides three main modules: Budget Management, Expense Management, and Budget Report. The project can also be expanded in the future with additional features such as file storage, graphs, and database support.
