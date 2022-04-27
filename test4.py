import pytest
import app
import os.path

def test_sum_clients():  # Тест на наличие 100 строк в Clients
    app.fill_db()
    assert len(app.Clients.select()) > 100