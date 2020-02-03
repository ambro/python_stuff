from savable import Savable


class User(Savable):
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def login(self):
        return 'Logged in!'

    def __repr__(self):
        return f'<User {self.user}>'

    def to_dict(self):
        return {
            'user': self.user,
            'password': self.password
        }




