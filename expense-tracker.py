expenses = []
 # this try block code is to load existing expenses; previously saved expesnses are loaded when the program starts
try:
    with open("expenses.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line or "," not in line:
                continue
            parts = line.split(",")

            if len(parts) != 2:
                continue
            expense_name, amount = parts
            
            expenses.append({"name":expense_name, "amount":float(amount)})
except FileNotFoundError:
    pass

def menu_page():
    print("----- Expense Tracker App ---- ")
    print("Press 1 to Add Expense")
    print("Press 2 to View Expenses")
    print("Press 3 to Exit")


while True:
    menu_page()
    choice = input("Enter an option: ")

    if choice == "1":
        expense_name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expense = {"name": expense_name,
                   "amount": amount}
        expenses.append(expense)

        with open("expenses.txt", "a") as file:
            file.write(f"{expense_name} - {float(amount):.2f}\n")  # to save to file

        print("Expense added successfully")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded")
        else:
            total = 0
            for expense in expenses:
                print(f"{expense['name']} - #{expense['amount']}")
                total += expense["amount"]
            print(f"Total Spent: #{total}")

    elif choice == "3":
        print("App exited")
        break
    else:
        print("Invalid choice")

        
