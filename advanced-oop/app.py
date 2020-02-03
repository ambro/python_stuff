from admin import Admin
from database import Database

a = Admin('jen', '123', 3)
a.save()

print(Database.find(lambda u: u['user'] == 'jen'))

