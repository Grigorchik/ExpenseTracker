expenses = []

def add_expense(amount, category, date):
    expense = {
        "сумма": amount,
        "категория": category,
        "дата": date
    }
    expenses.append(expense)
    return expense

def find_expense(category):
    result = []
    for expense in expenses:
        if expense["category"] == category:
            result.append(expense)
    return result
