import pytest
import app
import os.path

def test_clients():  # Тест на наличие столбцов в Clients
    assert app.Clients.name == False
    assert app.Clients.city == False
    assert app.Clients.address == False