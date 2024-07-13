class Complex: 

    def __init__ (self, real, imag):
        self.real = real
        self.imag = imag
    
    def showNumber(self):
        print(f"{self.real}i + {self.imag}j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal, newImag)
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImag = self.imag - num2.imag
        return Complex(newReal, newImag)
    



c1 = Complex(2, 3)
c2 = Complex(4, 5)

c3 = c1 + c2
c3.showNumber()