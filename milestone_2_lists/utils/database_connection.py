import sqlite3


class DatabaseConnection:
    def __init__(self, db_file_name):
        print("constructing DatabaseConnection")
        self.file_name = db_file_name
        self.connection = None

    def __enter__(self):
        print("starting context manager scope")
        self.connection = sqlite3.connect(self.file_name)
        return self.connection, self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("leaving context manager")
        if exc_type or exc_val or exc_tb is not None:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()

