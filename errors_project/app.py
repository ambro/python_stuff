class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Argument {car} is not of type Car, instead it's {car.__class__.__name__}")

        self.cars.append(car)


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'


ford = Garage()
car = Car('Ford', 'Fiesta')
car = "car"
try:
    ford.add_car(car)
except TypeError:
    print('Argument is not a car')
finally:
    print(f'The garage has now {len(ford)} cars')


