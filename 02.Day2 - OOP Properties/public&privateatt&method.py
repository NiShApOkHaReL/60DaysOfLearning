class Person:

    __name = "anonymous" #private attribute

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello() #private method

p1 = Person()

print(p1.welcome())
