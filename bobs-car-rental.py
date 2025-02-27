class Vehicle:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__rental_price_per_day = rental_price_per_day #Private attribute
        
    def display_info(self):  #Vehicle info
        print(f"{self.brand} {self.model}, Year: {self.year}, Rental Price: ${self.__rental_price_per_day}/day")
        
    def calculate_rental_cost(self, days):
        return days * self.__rental_price_per_day
    
    def get_rental_price_per_day(self):   #getter
        return self.__rental_price_per_day
    
    def set_rental_price_per_day(self, new_price):  #setter
        self.__rental_price_per_day = new_price
        
class Car(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, seating_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.seating_capacity = seating_capacity  # new attribute
        
    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}, Seats: {self.seating_capacity}, Rentsl Price: ${self.get_rental_price_per_day()}/day")
        
class Bike(Vehicle):
    def __init__(self, brand, model, year, rental_price_per_day, engine_capacity):
        super().__init__(brand, model, year, rental_price_per_day)
        self.engine_capacity = engine_capacity   # new attribute
        
    def display_info(self):
        print(f"Bike: {self.brand} {self.model}, Year: {self.year}, Engine: {self.engine_capacity}cc, Rental Price: ${self.get_rental_price_per_day()}/day")

def show_vehicle_info(vehicle):
    vehicle.display_info()
    
car = Car("Toyota", "Corolla", 2020, 50, 5)
bike = Bike("Yamaha", "R1", 2019, 30, 998)

# display vehicle details
show_vehicle_info(car)
show_vehicle_info(bike)

# calculate rental costs
car_rental_cost = car.calculate_rental_cost(3)
bike_rental_cost = bike.calculate_rental_cost(5)

print(f"Rental cost for {car.brand} {car.model} for 3 days: ${car_rental_cost}")
print(f"Rental cost for {bike.brand} {bike.model} for 5 days: ${bike_rental_cost}")

car.set_rental_price_per_day(55)
print(f"Updated rental price for {car.brand} {car.model}: ${car.get_rental_price_per_day()}/day")


