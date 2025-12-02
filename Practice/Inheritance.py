class employee:
    a,b = 10,20

    def total(self):
        print(self.a+self.b)

class employee2:
    x,y=10,10

    def multi(self):
        print(self.x*self.y)

class employee3(employee2):
    m,n =5,10
    def divide(self,a):
        print (self.n/self.m)
        print(a)

emp= employee3()
print(emp.x)
emp.multi()
print(emp.m)
emp.divide(10)

