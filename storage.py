# storage.py
import json

def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses, filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(expenses, f, indent=4)


