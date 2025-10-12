# This will be a mini project to keep track of Daily Expenses. 

print("Welcome to the Daily Expense Tracker!")
print("")
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expenses = []

while True:
  choice = input()
  if choice == "5":
    print("Exiting the Daily Expense Tracker. Goodbye!")
    break
  elif choice == "1":
    var1 = float(input())
    expenses.append(var1)
    print("Expense added successfully!)
