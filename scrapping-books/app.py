import logging

from pages.book_catalogue import BookCatalogue

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

catalogue = BookCatalogue(50)
books = catalogue.get_books()
