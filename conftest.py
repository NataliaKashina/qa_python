import pytest
from main import BooksCollector
@pytest.fixture
def books_collector():
    books_collector = BooksCollector()
    books_collector.add_new_book('Война и мир')
    books_collector.add_new_book('Преступление и наказание')
    books_collector.add_new_book('Мастер и Маргарита')
    books_collector.set_book_rating('Война и мир', 8)
    books_collector.set_book_rating('Преступление и наказание', 9)
    books_collector.set_book_rating('Мастер и Маргарита', 8)
    return books_collector

