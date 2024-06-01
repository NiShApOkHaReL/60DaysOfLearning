class Student:

    def __init__(self, name, marks): # Parameterized Constructor
        self.name = name
        self.marks = marks
        print("Adding new student in Database!")

s1 = Student("Nisha", 100)
print(s1.name, s1.marks)
s2 = Student("ABC", 20)
print(s2.name, s2.marks)








# class Student:
#     name = "Nisha Pokharel"
    
# s1 = Student()
# print(s1.name)


# class Car:
#     color = "blue"
#     brand = "mercedes"

# car = Car()
# print(car.color)
# print(car.brand)