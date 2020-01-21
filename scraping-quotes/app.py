from selenium import webdriver
from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path='C:\workdir\python\chromedriver.exe')
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotesPage(chrome)


author = input("Enter author:")
page.select_author(author)
tags = page.get_available_tags()
print("Select one of tags[{}]".format(" | ".join(tags)))
selected_tag = input("Enter selected tag: ")
page.select_tag(selected_tag)
page.search_button.click()
