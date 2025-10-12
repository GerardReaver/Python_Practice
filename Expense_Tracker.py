print("Welcome to the Daily Expense Tracker!")
print("")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

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
        if expenses == []:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(len(expenses)):
                print(f"{i + 1} {expense[i]}")

    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    
