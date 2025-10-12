print("Welcome to the Daily Expense Tracker!")
print("")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

# Initialize an empty list to store expenses
expenses = []

# This creates the infinite while loop. 
while True:
    choice = input()
    # This is the input of the user for the entirety of the program
    if choice == "1":
        var1 = float(input())
        expenses.append(var1)
        print("Expense added successfully!")

    elif choice == "2":
        # View all expenses
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1}. {expenses[i]}")

    elif choice == "3":
        # Calculate total and average expense
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            tot_expense = 0
            for i in expenses:
                tot_expense += i
                avg_expense = tot_expense / len(expenses)
            print(f"Total expense: {tot_expense}")
            print(f"Average expense: {avg_expense}")

    elif choice == "5":
        # Exit the program
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    
