# logic.py
from storage import load_expenses, save_expenses
import json
from utils import validate_integer

def add_expense(expense):
    expenses = load_expenses()
    # Assign an auto-incrementing numeric id (max existing id + 1)
    if expenses:
        max_id = max((e.get("id", 0) for e in expenses))
        new_id = max_id + 1
    else:
        new_id = 1
    expense["id"] = new_id
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully! (id={new_id})")

def view_all_expenses():
    expenses = load_expenses()
    print(json.dumps(expenses, indent=4, ensure_ascii=False, sort_keys=True))


def get_the_id_to_delete():
    expenses = load_expenses()
    print(json.dumps(expenses, indent=4, ensure_ascii=False, sort_keys=True))
    valid_ids = [e["id"] for e in expenses]
    id_to_delete = 0
    tries = 0
    
    while tries < 3:
        try:
            id_to_delete = int(input("Enter the expense ID, that you want to delete!"))
            if id_to_delete in valid_ids:
                return id_to_delete
                
            else:
                print("ID not found in expenses. Please try again.")
                tries += 1

        except ValueError:
            print("The input is invalid!, please try again ")
            tries += 1
    return None

def delete_expense():
    updated_DB = []
    expenses = load_expenses()
    id_to_delete = get_the_id_to_delete()

    if id_to_delete is None:
        print("deletion is aborted, you tried more than 3 times")
        return
    try:

        for e in expenses:
            if e["id"] != id_to_delete:
                updated_DB.append(e)
        save_expenses(updated_DB, "expenses.json")
        print("The Database has been successfully updated")

    except ValueError:
        print("there is no valid id to delete! ")
        return

def total_spent():
    expenses = load_expenses()
    total_spent = 0

    for amount in expenses:
        total_spent += amount["amount"]

    print(f"=============================\nThe Total spent is: {total_spent}$\n=============================")

def get_all_cat():
    expenses = load_expenses()
    categories = []
    for i in expenses:
        if i["category"] not in categories:
            categories.append(i["category"])
        if i["category"] in categories:
            continue
    return categories

def filter_by_cat():
    expenses = load_expenses()
    categories = get_all_cat()
    print("Here is all the categories you have!")
    print("=====================================")
    print(categories)
    try:
        filtered_by_cat = []
        cat_to_find= input("What category are you looking for?")
        if cat_to_find not in categories:
            print("=" * 30)
            print("=" * 30)
            print("Invalid Input, or the category doesn't exist")
            print("=" * 30)
            print("=" * 30)

            return
        else:
            for cat in expenses:
                if cat["category"] == cat_to_find:
                    filtered_by_cat.append(cat)
        pretty_format(filtered_by_cat) 
        return 
    except ValueError:
        print("something went wrong")



        
    


        
