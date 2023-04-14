import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_success(self):  # 1.Проверка добавления книг.
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        for key, value in collector.books_rating.items():
            assert (key, value) == ('Война и мир', 1)

    def test_add_new_book_add_the_same_books_impossible(self):  # 2.Нельзя добавить одну книгу дважды
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.books_rating.keys()) == 1

    @pytest.fixture # Фикстура создает словарь с одной книгой и рейтингом 1
    def books(self):
        books = BooksCollector()
        books.books_rating['Тихий Дон'] = 1
        return books

    def test_set_book_rating_for_not_added_book_impossible(self, books):  # 3.Нельзя выставить рейтинг книге, которой нет в списке
        books.set_book_rating('Му-Му', 5)  # пытаемся выставить рейтинг книге, которой нет в словаре
        assert books.books_rating == {'Тихий Дон': 1}  # проверяем, что словарь не изменился в пред шаге

    def test_set_book_rating_value_less_than_one_impossible(self, books):  # 4.Нельзя выставить рейтинг меньше 1
        books.set_book_rating('Тихий Дон', 0)  # Пробуем выставить 0 рейтинг книге из словаря
        assert books.books_rating == {'Тихий Дон': 1}  # проверяем, что словарь не изменился в пред шаге

    def test_set_book_rating_value_more_than_ten_impossible(self, books):  # 5.Нельзя выставить рейтинг больше 10
        books.set_book_rating('Тихий Дон', 11)  # Пробуем выставить рейтинг = 11 книге из словаря
        assert books.books_rating == {'Тихий Дон': 1}  # проверяем, что словарь не изменился в пред шаге

    @pytest.fixture  # Фикстура создает словарь с несколькими книгами с разным рейтингом
    def several_books(self):
        several_books = BooksCollector()
        several_books.books_rating = {
            'Тихий Дон': 1,
            'Колобок': 5,
            'Красная Шапочка': 5,
            'Мцыри': 3,
            'Левша': 7,
            'Три товарища': 10
        }
        several_books.expected_books_rating = {  # Переменная для проверки верного вывода словаря в тесте номер 8
            'Тихий Дон': 1,
            'Колобок': 5,
            'Красная Шапочка': 5,
            'Мцыри': 3,
            'Левша': 7,
            'Три товарища': 10
        }
        return several_books

    def test_get_books_rating_by_name_get_correct_rating(self, several_books):  # 6.Проверяем, что возвращается верный рейтинг по названию книги
        assert several_books.get_book_rating('Тихий Дон') == 1
        assert several_books.get_book_rating('Три товарища') == 10
        assert several_books.get_book_rating('Война и мир') is None

    def test_get_books_with_specific_rating_by_rating_get_correct_books(self, several_books):  # 7.Проверяем, что возвращаются верные книги по вводимому рейтингу
        assert several_books.get_books_with_specific_rating(5) == ['Колобок', 'Красная Шапочка']
        assert several_books.get_books_with_specific_rating(7) == ['Левша']

    def test_get_books_rating_get_books_dictionary(self, several_books):  # 8.Проверяем, что возвращается словарь с книгами верно
        assert several_books.get_books_rating() == several_books.expected_books_rating

    def test_add_book_in_favorites_via_name_success(self, several_books):  # 9.Проверяем что книги попадают в изранное
        several_books.add_book_in_favorites('Тихий Дон')
        assert 'Тихий Дон' in several_books.favorites
        several_books.add_book_in_favorites('Новая книга')
        assert 'Новая книга' not in several_books.favorites

    @pytest.fixture # Фикстура создает словарь избранных книг
    def favorite_books(self):
        favorite_books = BooksCollector()
        favorite_books.favorites = ['Book1', 'Book2', 'Book3']
        return favorite_books

    def test_delete_book_from_favorites_via_name_success(self, favorite_books): # 10.Проверяем удаление из избраного
        favorite_books.delete_book_from_favorites('Book2')
        assert favorite_books.favorites == ['Book1', 'Book3']
        favorite_books.delete_book_from_favorites('Book4')
        assert favorite_books.favorites == ['Book1', 'Book3']

    def test_get_list_of_favorites_books(self, favorite_books): # 11.Проверяем что верно возвращается словарь Избранного
        assert favorite_books.get_list_of_favorites_books() == ['Book1', 'Book2', 'Book3']