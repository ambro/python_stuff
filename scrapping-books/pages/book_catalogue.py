import requests
import logging

from pages.books_page import BooksPage


class BookCatalogue:
    def __init__(self, count):
        self.pages = []
        self.books = []
        self.logger = logging.getLogger('BookCatalogue')
        self.count = count

    def get_books(self):
        return self.books if self.books else self._get_all_books()

    def _get_all_books(self):
        for i in range(1, self.count):
            books_page = self.get_page(i)
            self.pages.append(books_page)
            self.books += books_page.books

        return self.books

    def get_page(self, page):
        url = self._get_url(page)
        self.logger.info(f"Downloading page content for {url}")
        page_content = requests.get(url).content
        books_page = BooksPage(page_content)
        return books_page

    @classmethod
    def _get_url(cls, page):
        return f"http://books.toscrape.com/catalogue/page-{page}.html"

