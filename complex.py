import math
from math import sqrt

class Complex():

    def _init_(self, real, imag=0.0):
        self.real = real
        self.imag = imag
    def display(self):
        if(self.imag>0):
            print(str(self.real) +' + '+ str(self.imag)+"i")
        else:
            print(str(self.real) +' - '+ str(abs(self.imag))+"i")

    def add(self, other):
        
        return Complex(self.real + other.real, self.imag + other.imag)

    def sub(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    
    def mul(self, other):
        return Complex((self.real * other.real) - (self.imag * other.imag),
            (self.imag * other.real) + (self.real * other.imag))

    def div(self, other):
        r = (other.real*2 + other.imag*2)
        return Complex((self.real*other.real - self.imag*other.imag)/r,
            (self.imag*other.real + self.real*other.imag)/r)
    def conjugate(self):
        return Complex(self.real,self.imag*-1)
        
    def mag(self):
        new = (self.real*2 + (self.imag2)-1)
        return Complex(sqrt(new.real))
    def inv(self):
        r = (self.real*2 + self.imag*2)
        return Complex(self.real/r,-1*self.imag/r)