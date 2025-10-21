import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()
        return self.collector
    
    def test_add_new_book_add_two_books(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(self.collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Жареные зеленые помидоры в кафе "Полустанок"', 'Жареные зеленые помидоры в кафе Помидорры'])
    def test_add_new_book_with_invalid_lenght(self, name):
        self.collector.add_new_book(name)
        assert name not in self.collector.books_genre

    def test_set_book_genre_if_book_in_books_genre_and_genre(self):
        self.collector.add_new_book('Дракула')
        self.collector.set_book_genre('Дракула', 'Ужасы')
        assert self.collector.get_books_genre() == {'Дракула': 'Ужасы'}

    def test_get_book_genre_for_name(self, books_genre):
        assert self.collector.get_book_genre('Дракула') == 'Ужасы' 

    def test_get_books_with_specific_genre(self, books_genre):
        assert self.collector.get_books_with_specific_genre('Фантастика') == ['Сирены Титана']

    def test_get_books_genre(self):
        assert self.collector.get_books_genre() == {}

    def test_get_books_for_children(self, books_genre):
        assert self.collector.get_books_for_children() == ['Сирены Титана']

    def test_add_book_in_favorites(self, books_genre):
        self.collector.add_book_in_favorites('Дракула')
        assert 'Дракула' in self.collector.favorites

    def test_delete_book_from_favorites(self, books_genre):
        self.collector.add_book_in_favorites('Дракула')
        self.collector.delete_book_from_favorites('Дракула')
        assert 'Дракула' not in self.collector.favorites

    def test_get_list_of_favorites_books(self):
        assert self.collector.favorites == []

    def test_get_list_of_genre(self):
        assert self.collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_get_list_of_genre_age_rating(self):
        assert self.collector.genre_age_rating == ['Ужасы', 'Детективы']

