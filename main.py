# main.py
from utils import validate_amount, validate_category, validate_description, validate_date
from logic import add_expense, view_all_expenses, delete_expense, total_spent, filter_by_cat, filter_by_date
import json


def get_expense_input():
    while True:
        amount = validate_amount(input("Enter Amount: "))
        if amount is not None:
            break
    while True:
        category = validate_category(input("Enter Category: "))
        if category is not None:
            break
    while True:
        description = validate_description(input("Enter Description: "))
        if description is not None:
            break
    while True:
        date = validate_date(input("Enter Date (YYYY-MM-DD): "))
        if date is not None:
            break
    return {
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

def main():
    print("Expenses Tracker CLI")
    print("====================")
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. Delete an Expense")
    print("4. Total Balance")
    print("5. filter by category")
    print("6.filter by date")
    print("7. Exit")
    
    while True:
        choice = input("Select an option: ")

        if choice == "1":
            expense = get_expense_input()
            add_expense(expense)
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6.filter by date")
            print("7. Exit")
        elif choice == "2":
            view_all_expenses()
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6.filter by date")
            print("7. Exit")         
        elif choice == "3":
            delete_expense()
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6.filter by date")
            print("7. Exit") 

        elif choice == "4":
            total_spent()
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6.filter by date")
            print("7. Exit") 
        elif choice == "5":
            filter_by_cat()
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6.filter by date")
            print("7. Exit") 
        elif choice == "6":
            filter_by_date()
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6.filter by date")
            print("7. Exit") 
        elif choice == "7":
            print("Good bye")
            break
        
            
        else:
            print("Invalid option")
            print("you need to choose exit to end the program")
            print("1. Add Expense")
            print("2. View all Expenses")
            print("3. Delete an Expense")
            print("4. Total Balance")
            print("5. filter by category")
            print("6. Exit")
            
if __name__ == "__main__":
    main()
