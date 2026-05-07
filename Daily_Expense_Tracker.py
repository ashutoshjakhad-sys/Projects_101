print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expenses = []
i = 0
def empty():
            print ("No expenses recorded yet.")
while i != 5:
    i = int(input())
    if i == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
    elif i == 1:
        j = float(input())
        expenses.append(j)
        print("Expense added successfully!")
    elif i == 2:
        if expenses == []:
            empty()
        else:
            print("Your expenses:")
            count = 1
            for k in expenses:
                print(count,end=".")
                print (f" {k}")
                count+=1
    elif i == 3:
        if expenses == []:
            empty()
        else:
            total = sum(expenses)
            average = total / len(expenses)
            print("Total expense: ", end= str(total))
            print()
            print("Average expense: ", end = str(average))
            print()
    elif i == 4:
        expenses.clear()
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")


