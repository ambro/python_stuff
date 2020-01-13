csv = open('csv_data.txt', 'r')
lines = [line.strip() for line in csv.readlines()]
csv.close()

lines = lines[1:]

for line in lines:
    name, age, university, degree = line.split(',')
    print(f'{name.title()} is {age}, studying {degree.capitalize()} at {university.title()}')
