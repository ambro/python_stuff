import logging
import requests
from pages.books_page import BooksPage

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

page_content = requests.get('http://books.toscrape.com').content
books_page = BooksPage(page_content)
for book in books_page.books:
    print(book)

