import re
from locators.book_selectors import BookSelectors


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, book_element):
        self.book = book_element
        self.price_pattern = '[0-9.]+'
        self._title = None
        self._price = None
        self._rating = None
        self._in_stock = None

    def __str__(self):
        return f'<BookParser book: {self.title} ' \
               f'has rating of {self.rating * "*"}. ' \
               f'The book is{"" if self.in_stock else " not"} available ' \
               f'and costs £{self.price}>'

    @property
    def title(self):
        return self._title if self._title else self._get_value(BookSelectors.TITLE, self._parse_title, self._set_title)

    @property
    def price(self):
        return self._price if self._price else self._get_value(BookSelectors.PRICE, self._parse_price, self._set_price)

    @property
    def rating(self):
        return self._rating \
            if self._rating \
            else self._get_value(BookSelectors.RATING, self._parse_rating, self._set_rating)

    @property
    def in_stock(self):
        return self._in_stock \
            if self._in_stock \
            else self._get_value(BookSelectors.IN_STOCK, self._parse_in_stock, self._set_in_stock)

    def _get_value(self, selector, parser, setter):
        tag = self.book.select_one(selector)
        value = parser(tag)
        setter(value)
        return value

    def _set_title(self, title):
        self._title = title

    def _set_price(self, price):
        self._price = price

    def _set_in_stock(self, in_stock):
        self._in_stock = in_stock

    def _set_rating(self, rating):
        self._rating = rating

    @classmethod
    def _parse_title(cls, tag):
        return tag.attrs['title']

    def _parse_price(self, tag):
        matcher = re.search(self.price_pattern, tag.string)
        return float(matcher.group(0))

    @classmethod
    def _parse_rating(cls, tag):
        rating = None
        for class_name in tag.attrs['class']:
            if (parsed_rating := cls.RATINGS.get(class_name)) is not None:
                rating = parsed_rating

        if not rating:
            return BookRatingException(f"Unknown rating in: {tag.attrs['class']}")
        else:
            return rating

    @classmethod
    def _parse_in_stock(cls, tag):
        return True if tag.text.strip() == "In stock" else False


class BookRatingException(Exception):
    pass


class GermanBookParser(BookParser):
    RATINGS = {
        'Eins': 1,
        'Zwei': 2,
        'Drei': 3,
        'Vier': 4,
        'Funf': 5
    }
