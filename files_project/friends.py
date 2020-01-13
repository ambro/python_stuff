print('Please provide the names of three friends')
friends = []
people = []
near = []

for i in range(1, 4):
    friend = input(f'Friend {i}: ')
    friends.append(friend)

people_db = open('people.txt', 'r')
while True:
    person = people_db.readline()

    if person:
        people.append(person.strip())
    else:
        break
people_db.close()

for friend in friends:
    if friend in people:
        near.append(friend)


near_db = open('nearby_friends.txt', 'w')

for friend in near:
    near_db.write(friend)

near_db.close()
