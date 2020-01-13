from utils.database_connection import DatabaseConnection

database = "data.db"


def create_book_table():
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")


def add_book(name, author):
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))


def get_book(name, author):
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute(f'SELECT name, author, read FROM books WHERE name=? and author=?', (name, author))
        row = cursor.fetchone()
        return {'name': row[0], 'author': row[1], 'is_read': row[2]}


def get_books():
    with DatabaseConnection(database) as (connection, cursor):
        cursor.execute(f'SELECT name, author, read FROM books')
        books = [{'name': row[0], 'author': row[1], 'is_read': row[2]} for row in cursor.fetchall()]
        return books


def delete_book(name, author):
    with DatabaseConnection(database) as (connection, cursor):
        rows_affected = cursor.execute(f'DELETE FROM books WHERE name=? and author=?', (name, author))

        if rows_affected.rowcount == 0:
            raise BookNotFoundException(name, author)


def mark_as_read(name, author):
    with DatabaseConnection(database) as (connection, cursor):
        rows_affected = cursor.execute(f'UPDATE books SET read = 1 WHERE name=? and author=?', (name, author))

        if rows_affected.rowcount == 0:
            raise BookNotFoundException(name, author)


class BookNotFoundException(Exception):
    def __init__(self, name, author):
        super().__init__(f'Book "{name}" by {author} was not found on your bookshelf.')
