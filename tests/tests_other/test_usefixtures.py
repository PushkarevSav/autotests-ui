import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")


@pytest.fixture
def fill_books_database():
    print("[FIXTURES] Создаем данные в базе данных")


@pytest.mark.usefixtures("clear_books_database",
                         "fill_books_database")  # Использовать когда фикстура не возвращает каких-либо данных
def test_read_all_book_in_library():
    pass
