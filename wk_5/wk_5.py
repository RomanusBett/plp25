# Assignment 1: Design Your Own Class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def device_info(self):
        return f"{self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model) 
        self.storage = storage
        self.battery = battery
    
    def call(self, contact):
        return f"Calling {contact}..."
    
    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        return f"Battery charged to {self.battery}%"
    
    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}%"


phone1 = Smartphone("Apple", "iPhone 15", 256, 80)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 60)

print(phone1.phone_info())
print(phone1.call("Alice"))
print(phone1.charge(15))

print(phone2.phone_info())


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement move method")


class Car(Vehicle):
    def move(self):
        return "Driving"


class Plane(Vehicle):
    def move(self):
        return "Flying"


class Boat(Vehicle):
    def move(self):
        return "Sailing"

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
