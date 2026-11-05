expenses = []

def add_expense(amount, category, date):
    expense = {
        "сумма": amount,
        "категория": category,
        "дата": date
    }
    expenses.append(expense)
    return expense