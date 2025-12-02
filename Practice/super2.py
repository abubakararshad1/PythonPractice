
# Global variables
a, b = 10, 20

class A:
    a, b = 50, 60
    def add(self, a, b):
        print(self.a + self.b)  # Class A variables
        print(a + b)            # Local (method) variables

class B(A):
    a, b = 40, 80
    def add(self, a, b):
        print(self.a + self.b)               # Accessing class B variables
        print(super().a + super().b)         # Accessing class A variables
        print(globals()['a'] + globals()['b'])  # Accessing global variables
        print(a - b)                         # Local (method) variables

# Create object of class B
myobj = B()
myobj.add(5, 4)
