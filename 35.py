class Car:
    def __init__(self, model, year):
        self.__model = model
        self.set_year(year)
    
    def get_model(self):
        return self.__model
    
    def set_model(self, model):
        self.__model = model
    
    def get_year(self):
        return self.__year
    
    def set_year(self, year):
        from datetime import datetime
        current_year = datetime.now().year
        if 1886 <= year <= current_year:
            self.__year = year
        else:
            raise ValueError(f"Год должен быть между 1886 и {current_year}")
    
    def __str__(self):
        return f"Автомобиль: {self.__model}, {self.__year} год"

class Truck(Car):
    def __init__(self, model, year, load_capacity):
        super().__init__(model, year)
        self.__load_capacity = load_capacity
    
    def get_load_capacity(self):
        return self.__load_capacity
    
    def set_load_capacity(self, load_capacity):
        self.__load_capacity = load_capacity
    
    def __str__(self):
        return f"Грузовик: {self.get_model()}, {self.get_year()} год, грузоподъемность: {self.__load_capacity}т"

class Garage:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def list_all_cars(self):
        for car in self.cars:
            print(car)
    
    def list_trucks_by_capacity(self, min_capacity):
        for car in self.cars:
            if isinstance(car, Truck) and car.get_load_capacity() > min_capacity:
                print(car)


garage = Garage()

car1 = Car("Toyota Camry", 2020)
truck1 = Truck("Volvo FH", 2022, 20)
truck2 = Truck("MAN TGX", 2021, 15)

garage.add_car(car1)
garage.add_car(truck1)
garage.add_car(truck2)

print("Все машины в автопарке:")
garage.list_all_cars()

print("\nГрузовики с грузоподъемностью более 16т:")
garage.list_trucks_by_capacity(16)