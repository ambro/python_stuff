import requests
from pages.quotes_page import QuotesPage

html = requests.get('http://quotes.toscrape.com').content
page = QuotesPage(html)

for quote in page.quotes:
    print(quote.content)