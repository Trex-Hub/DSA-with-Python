class Student:
    # Type Definition will always be an issue in python class as there is no strict type checking
    def __init__ (self, name, age, marks):
        self.name = name or 20
        self.age = age
        self.marks = marks

s1 = Student("John", 20, [90, 80, 70, 60, 50])

print(s1.name)
print(s1.age)
print(s1.marks)


