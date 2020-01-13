import utils.database as db
from utils.database import BookNotFoundException
import sqlite3

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def add_book():
    author, name = get_book_details()
    db.add_book(name, author)
    print(f'Added book "{name}" by {author} to the bookshelf.')


def get_book_details():
    name = input("Book title: ")
    author = input("Book author: ")
    return author, name


def show_book(book):
    print(f'"{book["name"]}" by {book["author"]} is {"read" if book["is_read"] else "not read"}.')


def show_books():
    bookshelf = db.get_books()
    print(f'You have {len(bookshelf)} books on your bookshelf.')
    for book in bookshelf:
        show_book(book)

    bookshelf.clear()


def mark_read_book():
    author, name = get_book_details()
    try:
        db.mark_as_read(name, author)
    except BookNotFoundException as missing:
        print(missing)
    else:
        print(f'Book "{name}" by {author} is marked as read.')


def delete_book():
    author, name = get_book_details()
    try:
        db.delete_book(name, author)
    except BookNotFoundException as missing:
        print(missing)
    else:
        print(f'Book "{name}" by {author} was deleted.')


def menu():
    db.create_book_table()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        try:
            if user_input == 'a':
                add_book()
            elif user_input == 'l':
                show_books()
            elif user_input == 'r':
                mark_read_book()
            elif user_input == 'd':
                delete_book()
            else:
                print('Unknown command')
        except Exception as x:
            print(f"Unexpected exception: type: {x.__class__.__name__}, content: {x}")
        finally:
            user_input = input(USER_CHOICE)


menu()
