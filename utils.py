# utils.py
from datetime import datetime

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

