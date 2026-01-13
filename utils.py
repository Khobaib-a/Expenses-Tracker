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

    

