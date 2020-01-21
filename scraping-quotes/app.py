from selenium import webdriver
from pages.quotes_page import QuotesPage
from pages.quotes_page import InvalidTagForAuthorError

try:
    chrome = webdriver.Chrome(executable_path='C:\workdir\python\chromedriver.exe')
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    author = input("Enter author:")
    tag = input("Enter selected tag: ")

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("Unknown error. Try again.")
