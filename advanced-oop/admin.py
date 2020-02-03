from user import User
from savable import Savable


class Admin(User):
    def __init__(self, user, password, access):
        super(Admin, self).__init__(user, password)
        self.access = access

    def __repr__(self):
        return f'<Admin {self.user} access {self.access}'

    def to_dict(self):
        return {
            'user': self.user,
            'password': self.password,
            'access': self.access
        }

    # searching self.save() in
    # 1. Admin
    # 2. User
    # 3. Savable

