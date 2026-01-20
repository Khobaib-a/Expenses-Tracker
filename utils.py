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


def get_all_days(year, month):
    expenses = load_expenses()
    relevant_days = []
    for x in expenses:
        date = x["date"]
        if date[:4] == year and date[5:7] == month:
            relevant_days.append(date)
    relevant_days.sort()
    return relevant_days




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


def get_report_date():
    expenses = load_expenses()
    year = year_prompt()
    month = month_prompt()
    relevant_expenses = []
    for x in expenses:
        date = x["date"]
        if date[:4] == year and date[5:7] == month:
            relevant_expenses.append(date)
    if not relevant_expenses:
        return relevant_expenses
    else:
        relevant_expenses.sort()
        return relevant_expenses

def get_report_expenses():
    expenses = load_expenses()

    all_relevant_expenses = []
    report_date = get_report_date()
    if not report_date:
        return[]
    
    for date in report_date:
        for expense in expenses:
            if date == expense["date"]:
                all_relevant_expenses.append(expense)
    return all_relevant_expenses
