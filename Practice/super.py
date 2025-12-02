class A:
    def m1(self):
        print("We are inside method m1 of class A")

class B(A):
    def m1(self):
        print("We are inside method m2 of class B")
        super().m1()

myobj = B()
myobj.m1()
