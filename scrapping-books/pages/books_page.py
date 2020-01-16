from bs4 import BeautifulSoup
from locators.books_page_selectors import BooksPageSelectors
from parsers.book_parser import BookParser
import logging


class BooksPage:
    def __init__(self, html):
        self.logger = logging.getLogger('BooksPage')
        self.page = BeautifulSoup(html, 'html.parser')
        self._books = []

    @property
    def books(self):
        return self._books if self._books else self._get_books()

    def _get_books(self):
        selector = BooksPageSelectors.BOOKS
        book_elements = self.page.select(selector)
        self._books = [BookParser(book) for book in book_elements]
        self.logger.info(f"Found {len(self._books)} books on page.")
        return self._books


