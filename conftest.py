import pytest

from main import BooksCollector


@pytest.fixture
def books_genre(collector):
    collector.books_genre = {'Дракула': 'Ужасы', 'Сирены Титана': 'Фантастика', 'Оно': 'Ужасы'}
    return collector.books_genre
