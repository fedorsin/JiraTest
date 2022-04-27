import pytest
import app
import os.path


def test_create_database():  # Тест на создание БД
    app.init_db()
    assert os.path.exists(app.db_name) == True