# Expenses Tracker Project

from datetime import date


expenses = []
print("Welcome to the Expenses Tracker!")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        expense_date = input("Enter the date (YYYY-MM-DD): ")
        expense_name = input("Enter the expense name: ")
        expense_amount = float(input("Enter the expense amount: "))

        expense = {
            "date": expense_date,
            "name": expense_name,
            "amount": expense_amount,
        }
        expenses.append(expense)
        print(f"Expense '{expense_name}' of amount {expense_amount} added successfully!")

    elif choice == '2':
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("Expenses:")
            for expense in expenses:
                print(f"Date: {expense['date']}, Name: {expense['name']}, Amount: {expense['amount']}")

    elif choice == '3':
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total Expenses: {total}")

    elif choice == '4':
        print("Exiting the Expenses Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")