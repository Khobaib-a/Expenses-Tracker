# Expenses-Tracker
This is my first project in python, where i tried to devide my code in different modules and use the coding principles, that i learned so far.

# Expense Tracker CLI ✅

A simple command-line expense tracker that stores expenses in a local JSON file (`expenses.json`). Use it to add, view, delete, and total your expenses from the terminal.

---

## Features 🔧
- **Add Expense** (amount, category, description, date)
- **View all Expenses** (prints JSON list)
- **Delete an Expense** (by auto-assigned numeric `id`, 3 attempts)
- **Show Total** of all expenses
- **filter by category** filter the output based on the category chosen

---

## Requirements 💡
- Python 3.6+
- No external packages (uses the standard library)

---

## Quick start — Install & Run ⚙️
1. Clone or copy the project files.

2. Run the program:
   - `python main.py`

> Note: `expenses.json` is created automatically if it doesn't exist.
        `you can use any json formatted data as a database, that meets the requirements`.

---

## Usage — Interactive Menu 🖱️
When you run `python main.py` you will see a menu:

1. Add Expense
2. View all Expenses
3. Delete an Expense
4. Total Balance
5.filter by category
6. Exit

- **Add Expense:** enter amount (float), category, description and date (YYYY-MM-DD).
- **Delete:** enter the expense `id` shown in the listing (you get 3 tries).
- **Total Balance:** prints the summed `amount` of all saved expenses.

---

## Data format (stored in `expenses.json`) 📁
Each expense is a JSON object with:
- `id` (int) — auto-incremented
- `amount` (float)
- `category` (string)
- `description` (string)
- `date` (YYYY-MM-DD)

Example:

```json
{
    "id": 1,
    "amount": 12.5,
    "category": "Food",
    "description": "Lunch",
    "date": "2025-12-31"
}
```

---

## Validation & Behavior ⚠️
- Amount must be convertible to float.
- Date must match `YYYY-MM-DD`.
- Category and description cannot be blank.
- IDs are assigned automatically; deleting rewrites the JSON file.

---

## Contributing 🤝
- Fork, make small focused changes, and open a PR.
- Add tests and update the README if you add features.



