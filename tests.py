import pytest

from main import BooksCollector

class TestBooksCollector:
   
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('name', ['', 'Жареные зеленые помидоры в кафе "Полустанок"', 'Жареные зеленые помидоры в кафе Помидорры'])
    def test_add_new_book_with_invalid_lenght(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.books_genre

    def test_set_book_genre_if_book_in_books_genre_and_genre(self, collector):
        collector.add_new_book('Дракула')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.books_genre == {'Дракула':'Ужасы'}

    def test_get_book_genre_for_name(self, collector):
        collector.books_genre['Оно'] = 'Ужасы'
        assert collector.get_book_genre('Оно') == 'Ужасы' 

    def test_get_books_with_specific_genre(self, collector):
        collector.books_genre['Оно'] = 'Ужасы'
        collector.books_genre['Сирены Титана'] = 'Фантастика'
        books = collector.get_books_with_specific_genre('Ужасы')
        assert books == ['Оно']

    def test_get_books_genre(self, collector):
        collector.books_genre['Ребекка'] = 'Детективы'
        assert collector.get_books_genre() == {'Ребекка': 'Детективы'}

    def test_get_books_for_children(self, collector):
        collector.books_genre['Оно'] = 'Ужасы'
        collector.books_genre['Сирены Титана'] = 'Фантастика'
        assert collector.get_books_for_children() == ['Сирены Титана']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Ребекка')
        collector.add_book_in_favorites('Ребекка')
        assert 'Ребекка' in collector.favorites

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Ребекка')
        collector.add_book_in_favorites('Ребекка')
        collector.delete_book_from_favorites('Ребекка')
        assert 'Ребекка' not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Дракула')
        collector.add_book_in_favorites('Дракула')
        assert collector.favorites == ['Дракула']


