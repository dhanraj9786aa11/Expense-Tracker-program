# Expense Tracker Project.

ExpensesList = []
# List of Expenses in form of Dictionary.

print("WELCOME TO EXPENSE TRACKER")

while True:
    print("...........MENU...........")
    
    print("1. Add Expense")
    
    print("2. View All Expenses")
    
    print("3. view Total Spending")
    
    print("4. EXIT.")


    choice = int(input("Please enter your choice : "))

    #1. Add Expense.
    if choice == 1:
        date = input("enter the date : ")
        
        category = input("enter the category (ex: food, travel, makeup, books, etc.) :")
        
        description = input("detail about the product in the category :")
        
        amount = float(input("enter the amount :"))

        expense = {
            "Date": date,
            "Category": category,
            "Description": description,
            "Amount": amount,
        }

        ExpensesList.append(expense)
        print("expense is added successfully")

        # 2. View all expenses
    elif choice == 2:
        if len(ExpensesList) == 0:
            print("no expenses added.")
        else:
            print("...........YOUR'S EXPENSE...........")
            count = 1
            for eachexpense in ExpensesList:
                print(f"expense number {count} -> {eachexpense['Date']},  {eachexpense['Category']}, {eachexpense['Description']}, {eachexpense['Amount']}")
                count = count + 1
         # 3. View Total Spending
    elif choice == 3:
        total=0

        for eachexpense in ExpensesList:
            total=total+eachexpense["Amount"]

        print("Total Expense=",total)

        # 4. EXIT
    elif choice == 4:
        print("thankyou have a good day")
        break
    else:
        print("invalid choice. try  again")