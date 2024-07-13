class Student: 

    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
    
    @property
    # This is a decorator 
    # This is used to make the method behave like an attribute
    def percentage(self):
        return str((self.phy + self.chem + self.maths )/3) + " %"
    

s1 = Student(50, 40, 70)
print(s1.percentage)

s1.phy = 80
print(s1.percentage)
