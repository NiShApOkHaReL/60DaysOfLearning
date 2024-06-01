class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def set_age(self, new_age):
        self.age = new_age

# Create an instance of the Student class
s1 = Student("Nisha Pokharel", 21)

# Call instance methods
s1.display_info()  # Output: Name: Nisha Pokharel, Age: 21
s1.set_age(22)
s1.display_info()  # Output: Name: Nisha Pokharel, Age: 22
