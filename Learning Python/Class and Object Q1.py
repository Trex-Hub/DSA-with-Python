class Student:
    def __init__():
        pass
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def hello():
        return "Hello, World!"


s1 = Student("John", [90, 99, 95])
print(s1.average())
print(s1.hello())


class Account:
    def __init__(self, balance):
         self.balance = balance
    
    def credit (self, amount): 
        self.balance = self.balance + amount
        return self.balance
    
    def debit (self , amount):
        self.balance = self.balance - amount
        return self.balance
    
    def getBallance(self):
        print(self.balance)
    
my_acc = Account(5000)

print(my_acc.debit(30))