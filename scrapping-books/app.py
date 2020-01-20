import logging
import requests

from pages.book_catalogue import BookCatalogue

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

page_content = requests.get('http://books.toscrape.com').content
catalogue = BookCatalogue(5)
books = catalogue.get_books()
