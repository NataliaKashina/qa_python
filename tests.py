import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_book_rating('Война и мир') == 1
    def test_add_new_book_adding_the_same_books(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.books_rating.keys()) == 1

    def test_set_book_rating_for_nonexistent_book(self):
        books = BooksCollector()
        books.set_book_rating("The Great Gatsby", 8)
        assert books.get_book_rating("The Great Gatsby") == None

    @pytest.mark.parametrize('name, rating', [['Book1', 11], ['Book2', 15]])
    def test_set_book_rating_greater_than_ten(self, name, rating):
        books = BooksCollector()
        books.books_rating = {'Book1': 5, 'Book2': 8}
        books.set_book_rating(name, rating)
        assert books.get_book_rating(name) != rating

    def test_set_book_rating_zero_value(self):
        collector = BooksCollector()
        collector.books_rating = {'Book1': 5}
        collector.set_book_rating('Book1', 0)
        assert collector.books_rating['Book1'] == 5

    def test_get_book_rating_by_name(self):
        books = BooksCollector()
        books.add_new_book('Война и Мир')
        books.set_book_rating('Война и Мир', 8)
        assert books.get_book_rating('Война и Мир') == 8

    def test_get_books_with_specific_rating_multiple_books(self, books_collector):
        assert books_collector.get_books_with_specific_rating(8) == ['Война и мир', 'Мастер и Маргарита']

    def test_get_books_with_specific_rating_no_books(self, books_collector):
        assert books_collector.get_books_with_specific_rating(7) == []

    def test_get_books_rating(self, books_collector):
        expected_book_rating = {'Война и мир': 8, 'Мастер и Маргарита': 8, 'Преступление и наказание': 9}
        assert books_collector.get_books_rating() == expected_book_rating

    def test_add_book_in_favorites(self, books_collector):
        books_collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in books_collector.favorites
        books_collector.add_book_in_favorites('Новая книга')
        assert 'Новая книга' not in books_collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Анна Каренина')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Преступление и наказание')
        assert collector.get_list_of_favorites_books() == ['Война и мир', 'Преступление и наказание']
        collector.delete_book_from_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == ['Преступление и наказание']

    def test_get_list_of_favorites_books(self):
        books = BooksCollector()
        books.add_new_book('Book1')
        books.add_new_book('Book2')
        books.add_new_book('Book3')
        books.add_book_in_favorites('Book1')
        books.add_book_in_favorites('Book3')
        assert books.get_list_of_favorites_books() == ['Book1', 'Book3']