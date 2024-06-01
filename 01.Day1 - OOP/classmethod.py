class Student:
    school_name = "XYZ School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_school):
        cls.school_name = new_school

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, School: {Student.school_name}")

# Create instances of the Student class
s1 = Student("Nisha Pokharel", 21)
s2 = Student("John Doe", 22)

# Call instance method
s1.display_info()  # Output: Name: Nisha Pokharel, Age: 21, School: XYZ School

# Call class method
Student.change_school("ABC School")

# Call instance method again to see the updated class attribute
s1.display_info()  # Output: Name: Nisha Pokharel, Age: 21, School: ABC School
s2.display_info()  # Output: Name: John Doe, Age: 22, School: ABC School
