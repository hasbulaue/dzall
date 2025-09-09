class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
class Bike:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
Dog1 = Dog("Max", 3, "Labrador")
Cat1 = Cat("Whiskers", 5, "Black")
Car1 = Car("Toyota", "Camry", 2020)
Bike1 = Bike("Harley-Davidson", "Sportster", 2021)

print(Dog1.name, Dog1.age, Dog1.breed)
print(Cat1.name, Cat1.age, Cat1.color)
print(Car1.make, Car1.model, Car1.year)
print(Bike1.make, Bike1.model, Bike1.year)
