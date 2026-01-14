# utils.py
from datetime import datetime
from storage import load_expenses

def validate_amount(amount):
    try:
        amt = float(amount)
        return amt
    except ValueError:
        print("Invalid amount.")
        return None

def validate_category(category):
    if category.strip():
        return category.strip()
    print("Invalid category.")
    return None

def validate_description(description):
    if description.strip():
        return description.strip()
    print("Invalid description.")
    return None

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return date_str
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")
        return None
    

def validate_integer(integer):
    try:
        number = int(integer)
        return number
    except ValueError:
        print("invalid Input")
  

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

    

""" def get_all_dates():
    expenses = load_expenses()
    dates = []
    for i in expenses:
        if i["date"] not in dates:
            dates.append(i["date"])
        if i["date"] in dates:
            continue
    return dates

def filter_by_date():
    expenses = load_expenses()
    dates = get_all_dates()
    print("Here is all the dates where you have spent something!")
    print("=====================================")
    print(dates)
    try:
        filtered_by_date = []
        date_to_find= input("What Date are you looking for?")
        if date_to_find not in dates:
            print("=" * 30)
            print("=" * 30)
            print("Invalid Input, or the Date doesn't exist")
            print("=" * 30)
            print("=" * 30)

            return
        else:
            for date in expenses:
                if date["date"] == date_to_find:
                    filtered_by_date.append(date)
        pretty_format(filtered_by_date) 
        return 
    except ValueError:
        print("something went wrong")
        
    """

def current_year():
    current_year = datetime.now().year
    return[ e for e in range(0, current_year)]

def get_all_days_of_expenses():
    expenses = load_expenses()

    DAYS = []
    for i in expenses:
        if i["date"] not in DAYS:
            DAYS.append(i["date"])
        if i["date"] in DAYS:
            continue
    dd_date = []        
    for i in DAYS:
        dd_date.append(i[8]+i[9])
    return dd_date



