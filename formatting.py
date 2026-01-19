
from utils import get_all_days

def print_menu():
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. Delete an Expense")
    print("4. Total Balance")    
    print("5. filter by category")
    print("6.filter by date")
    print("7. Exit")

def show_days(year,month):
    relevant_days = get_all_days(year ,month)
    print(f"\nThe Day {" " * 10 }, The Date")
    print("=============================\n"
    "=============================")
    if not relevant_days:
        print("################################")
        print("There is no expenses at this date")
        print("################################")
        return 
    for x in relevant_days:
        print(f"{x[8:]} {" " * 10} {x} \n")
    
def pretty_format(filtered_by_cat):
    print("=" * 30)
    for x in filtered_by_cat:
        if x["amount"]:
            print(f"amout: {x["amount"]}")
        if x["category"]:
            print(f"category: {x["category"]}")
        if x["description"]:
            print(f"description: {x["description"]}")
        if x["date"]:
            print(f"date: {x["date"]}")
        if x["id"]:
            print(f"id: {x["id"]}")
            print("=" * 30)
            print("=" * 30)
