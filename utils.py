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
    
"""
def validate_integer(integer):
    try:
        number = int(integer)
        return number
    except ValueError:
        print("invalid Input")
 """    

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

def get_all_days(year, month):
    expenses = load_expenses()
    relevant_days = []
    for x in expenses:
        date = x["date"]
        if date[:4] == year and date[5:7] == month:
            relevant_days.append(date)
    relevant_days.sort()
    return relevant_days

def show_days(year,month):
    relevant_days = get_all_days(year ,month)
    print(f"\nThe Day {" " * 10 }, The Date")
    print("=============================\n"
    "=============================")
    for x in relevant_days:
        print(f"{x[8:]} {" " * 10} {x} \n")



def year_prompt():
    current_year = datetime.now().year
    while True:
        searched_year = input("Enter the Year  (YYYY): ")
        if searched_year.isdigit() and len(searched_year) == 4 and 1<= int(searched_year) <= current_year:
            return searched_year
        else:
            print("Invalid year, try again with this format(YYYY)")

def month_prompt():
    
    while True:
        searched_month = input("Enter the Month  (MM): ")
        if 1<= int(searched_month) <= 12 and len(searched_month) == 2 and searched_month.isdigit():
            return searched_month
        else:
            print("Invalid month, try again with this format(MM)")

def day_prompt():
    
    while True:
        searched_day = input("Enter the Day  (DD): ")
        if 1<= int(searched_day) <= 31 and len(searched_day) == 2 and searched_day.isdigit():
            return searched_day
        else:
            print("Invalid Day, try again with this format(DD)")

def filter():
    year = year_prompt()
    month = month_prompt()
    relevant_days =get_all_days(year, month)
    show_days(year, month)
    day = day_prompt()
    filtered_dates = []
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
                print(t)






