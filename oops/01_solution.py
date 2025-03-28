class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def full_type(self):
        return "Petrol or Disel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transportation"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def full_type(self):
        return "Electric charge"


# Inheritance
my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.model)
# print(my_tesla.full_name())
# encapsulation
# print(my_tesla.brand) # throw error
print(my_tesla.get_brand())
print(my_tesla.full_type())


safari = Car("Tata", "Safari")
print(safari.full_type())
my_car = Car("Tata", "Nexon")
# my_car.model = "City"

print("Total car :", Car.total_car)
print(my_car.model)



# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# my_new_car = Car("Tata", "Safari")
# print(my_new_car.brand)
# print(my_new_car.model)
# print(my_new_car.full_name())
