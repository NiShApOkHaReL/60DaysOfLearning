class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi",self.name, "your avg score is:", sum/3)


s1 = Student("Nisha",[99,98,97])
s1.avg()
