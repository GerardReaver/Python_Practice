print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
# Variables outside the problems will be held here
expenses = []
total_expense = 0
average_amount = 1

while True:
    user_input = int(input())
    
    if user_input == 1:
        amount_added = float(input())
        expenses.append(amount_added)
        print("Expense added successfully!")

    elif user_input == 2:
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, amounts in enumerate(expenses):
                print(f"{index + 1}. {amounts}")

    elif user_input == 3:
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            for index, amounts in enumerate(expenses):
                total_expense += amounts
                average_amount = total_expense / (index + 1)
            print(f"Total expense: {total_expense}")
            print(f"Average expense: {average_amount}")

    elif user_input == 4:
        expenses = []
        print("All expenses cleared.") 

    elif user_input == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
