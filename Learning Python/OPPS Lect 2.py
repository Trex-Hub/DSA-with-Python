class Person:
    name = "Anon"

    def changeName( self, newName ):
    
        self.name = newName
    # This creates a attribute name in the object and assigns the value of newName to it
    # To change the attribute of the class, we need to use the class name

    def changeNameClassOne( newName ):
        # Person.name = newName
        self.__class__.name = newName
        # This changes the attribute of the class
    

    # For better understanding, we can use the following code
    @classmethod
    def changeNameClass( cls, newName ):
        cls.name = newName
        # This changes the attribute of the class


p1 = Person()
print(Person.name)
print(p1.name)
p1.changeNameClass("John")
print(Person.name)
print(p1.name)


    