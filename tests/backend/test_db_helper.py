from backend import db_helper

def test_fetch_expenses_for_date_valid():
    expenses = db_helper.fetch_expenses_for_date("2024-08-15")

    assert len(expenses) == 1
    assert expenses[0]['amount'] == 10.0
    assert expenses[0]['category'] == "Shopping"
    assert expenses[0]["notes"] == "Bought potatoes"

def test_fetch_expenses_for_date_invalid():
    expenses = db_helper.fetch_expenses_for_date("9999-08-15")

    assert len(expenses) == 0

#def test_delete_expenses_for_date(expense_date):
 #   pass

#def test_insert_expense(expense_date,amount,category,notes):
 #   pass

#def test_fetch_expense_summary(start_date,end_date):
 #   pass
