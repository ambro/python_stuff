import json

with open('friends_json.txt', 'r') as file:
    file_content = json.load(file)

print(file_content['friends'][0])
print(file_content.__class__.__name__)

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)


