class Car:
    # Class attribute
    wheels = 4

    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

    # Instance method
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Wheels: {Car.wheels}")

    # Class method
    @classmethod
    def set_wheels(cls, num_wheels):
        cls.wheels = num_wheels

# Create instances of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Display initial information
car1.display_info()  # Output: Brand: Toyota, Model: Corolla, Wheels: 4
car2.display_info()  # Output: Brand: Honda, Model: Civic, Wheels: 4

# Modify class attribute using class method
Car.set_wheels(6)

# Display updated information
car1.display_info()  # Output: Brand: Toyota, Model: Corolla, Wheels: 6
car2.display_info()  # Output: Brand: Honda, Model: Civic, Wheels: 6
