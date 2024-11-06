
def enterDetails():
    global name
    print("Welcome to the Personal Budget Tracker!")
    name = input("Please enter your name: ")
    print(f"Hello, {name.title()}! Let's calculate your monthly savings.\n")

    try:
        monthlyIncome = int(input("Enter your monthly income: "))
        monthlyExpense = int(input("Enter your monthly expenses: "))
        monthlySavings = monthlyIncome - monthlyExpense

        print(f"{name.title()}, your monthly savings are: {monthlySavings:.2f}")

        if monthlySavings > 1000:
            print("Great Job! You are saving a lot!")
        elif 1000 > monthlySavings > 500:
            print("Good Job! Consider saving more!")
        else: 
            print("You might want to reduce your expenses")

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
    
    


def individualExpense():
    print("\nNow let's input individual expenses. Type 'done' when finished")
    totalExpenses = 0
    while True:
        expense = input("Enter an expense: ")
        
        if expense.lower() == "done":
            break
        
        try:
            expense = float(expense)
            totalExpenses += expense
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done' to finish\n")
    print(f"Total individual expenses: {totalExpenses:.2f}")


enterDetails()
individualExpense()
print(f"\nThank you for using the Personal Budget Tracker, {name.title()}")