import pytest
import app
import os.path

def test_orders():  # Тест на наличие столбцов в Orders
    assert app.Orders.clients == False
    assert app.Orders.amount == False
    assert app.Orders.date == False
    assert app.Orders.description == False