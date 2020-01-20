import logging
from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''

books_gen = (book for book in books)


def print_best_books():
    best_books = sorted(books, key=lambda b: (b.rating * -1, b.price))[:10]
    for i, book in enumerate(best_books):
        print(f'Ranking {i + 1}: {book}')


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda b: b.price)[:10]
    for i, book in enumerate(cheapest_books):
        print(f'Ranking {i + 1}: {book}')


def get_next_book():
    print(next(books_gen))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        try:
            logger.debug('User did not choose to exit program.')
            if user_input in ('b', 'c', 'n'):
                user_choices[user_input]()
            else:
                print('Please choose a valid command.')
            user_input = input(USER_CHOICE)
        except Exception as ex:
            logger.exception("Unhandled exception")
    logger.debug('Terminating program...')


menu()
