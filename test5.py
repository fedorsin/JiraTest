import pytest
import app
import os.path

def test_sum_orders():  # Тест на наличие 100 строк в Orders
    app.fill_db()
    assert len(app.Orders.select()) > 100