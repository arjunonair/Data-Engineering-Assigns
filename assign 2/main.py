from db import *
from expense import Expense

#Function to add expense
def add_expense(expenses):
    expense_id = int(input('Enter the expense id: '))
    date = input('Enter the date(yyyy-mm-dd): ')
    category = input('Enter the category: ')
    description = input('Enter the description: ')
    amount = int(input('Enter the amount: '))

    expenses.append(Expense(expense_id,date,category,description,amount))
    print('\nNew Expense added!')

#Function to update expense
def update_expense(expense_id,new_expense):
    for expense in expenses:
        if expense.expense_id == expense_id:
            expense.date = new_expense.date if new_expense.date else expense.date
            expense.category = new_expense.category if new_expense.category else expense.category
            expense.description = new_expense.description if new_expense.description else expense.description
            expense.amount = new_expense.amount if new_expense.amount else expense.amount
    print('\nExpense updated !')

#Function to delete expense
def delete_expense(expense_id):
    for exp in expenses:
        if exp.expense_id == expense_id:
            expenses.remove(exp)
            print('\nExpense had been removed!')

#Function to display expense
def display_expenses():
    print('''\nExpenseID\tDate\t\tCategory\tDescription\tAmount''')
    print("*********\t*****\t\t*********\t***********\t*******")
    for exp in expenses:
        print(f'''{exp.expense_id}\t\t{exp.date}\t{exp.category}\t\t{exp.description}\t\t{exp.amount}''')

#Function to authenticate the user
def authenticate_user(username,password):
    for name,pwd in users.items():
        if name == username and password == pwd:
            print('\nLogin successfull!')
            return True
    print('\nLogin failed!')
    return False

# Function which returns a dictionary of category and its amount
def catergorize_expenses():
    categories = {}
    for expense in expenses:
        if expense.category not in categories:
            categories[expense.category] = expense.amount
        else:
            categories[expense.category] += expense.amount
    return categories

#Function which gives total expenditure
def summarize_expenses():
    total_amount = 0
    for expense in expenses:
        total_amount += expense.amount
    return total_amount

#Function which gives total expenditure
def calculate_total_expenses():
    total_amount = 0
    for expense in expenses:
        total_amount += expense.amount
    return total_amount

#Function to generate report based on the amount.
def generate_report():
    category = catergorize_expenses()
    print('\n-----------------------------------------------------')
    print('\n------------- Expense Summary Report  ---------------')
    for cgy,amount in category.items():
        print(f"- {cgy} -> \t\t\t\t$ {amount}")
    print('\n-----------------------------------------------------')
    print(f"- Final Amount -> \t\t\t$ {calculate_total_expenses()}")


#Main function with user CLI
print('-------------WELCOME TO EXPENSE TRACKER-------------')
print("\nEnter Login Details :: ")
username = input("\nEnter username : ")
password = input("\nEnter password : ")
if(authenticate_user(username,password)):
    while True:
        print('\n-----------------------------------------------------')
        print('''
            1 -> Add Expense
            2 -> Update Expense
            3 -> Delete Expense
            4 -> Display Expense
            5 -> Generate Report
            6 -> Quit
            ''')
        print('-----------------------------------------------------\n')
        choice = input("Enter your choice")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            expense_id = int(input('Enter the expense id: '))
            date = input('Enter the date(yyyy-mm-dd): ')
            category = input('Enter the category: ')
            description = input('Enter the description: ')
            amount = input('Enter the amount: ')
            if date == '' or amount == '':
                print('\nDate and Amount Cannot be empty.')
                continue
            update_expense(expense_id,Expense(expense_id,date,category,description,int(amount)))
        elif choice == '3':
            expense_id = int(input('Enter the expense id: '))
            delete_expense(expense_id)
        elif choice == '4':
            display_expenses()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            print('\nThank you. Have a nice day :)\n')
            break
        else:
            print('\nInvalid choice!')
else:
    print('\n*You are not Authorized to seee this Page. Please Restart and Login!')
