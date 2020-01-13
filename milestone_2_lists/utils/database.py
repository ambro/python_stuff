from typing import List, Dict, Union

from utils.database_connection import DatabaseConnection

database = "data.db"
Book = Dict[str, Union[str, int]]  # alias for type hint of dict where key is a string and value can be str or int


def create_book_table() -> None:
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def add_book(name: str, author: str) -> None:
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_book(name: str, author: str) -> Book:
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute(f'SELECT name, author, read FROM books WHERE name=? and author=?', (name, author))
        row = cursor.fetchone()
        return {'name': row[0], 'author': row[1], 'is_read': row[2]}


def get_books() -> List[Book]:
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute(f'SELECT name, author, read FROM books')
        books = [{'name': row[0], 'author': row[1], 'is_read': row[2]} for row in cursor.fetchall()]
        return books


def delete_book(name: str, author: str) -> None:
    with DatabaseConnection(database) as (connection, cursor):
        rows_affected = cursor.execute(f'DELETE FROM books WHERE name=? and author=?', (name, author))

        if rows_affected.rowcount == 0:
            raise BookNotFoundException(name, author)


def mark_as_read(name: str, author: str) -> None:
    with DatabaseConnection(database) as (connection, cursor):
        rows_affected = cursor.execute(f'UPDATE books SET read = 1 WHERE name=? and author=?', (name, author))

        if rows_affected.rowcount == 0:
            raise BookNotFoundException(name, author)


class BookNotFoundException(Exception):
    def __init__(self, name, author):
        super().__init__(f'Book "{name}" by {author} was not found on your bookshelf.')
