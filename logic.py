# logic.py
from storage import load_expenses, save_expenses
import json
from formatting import show_days, pretty_format
from utils import day_prompt, year_prompt,month_prompt, get_all_days

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
    print("=" * 30)
    for x in expenses:
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




def filter():
    year = year_prompt()
    month = month_prompt()
    relevant_days =get_all_days(year, month)
    show_days(year, month)
    filtered_dates = []
    if relevant_days:
        day = day_prompt()
        for x in relevant_days:
            if day == x[8:]:
                filtered_dates.append(x)
    return filtered_dates
    


def filter_by_date():
    expenses = load_expenses()
    filtered_dates = filter()
    for d in filtered_dates:
        for t in expenses:
            if t["date"] == d:
                print(f"amout: {t["amount"]}")
                print(f"category: {t["category"]}")
                print(f"description: {t["description"]}")
                print(f"date: {t["date"]}")
                print(f"id: {t["id"]}")
                print("=" * 30)

