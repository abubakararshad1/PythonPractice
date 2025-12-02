class myclass:

    num1= 1000
    def printname(self):
        print("Hello, i am testing")

    def printrank(self, email,  id="9"):
        print("Rank is",    email,  id)
        self.num1=2000

    def addition(self,a,b):
        return (a+b)

    def argtest(self,x,y=100):
        print(x+y)

    def numsum(self,x=5,y=10):
        return (x+y)


p1 = myclass()
p1.printname()
p1.printrank("abubakar.arshad@gmail.com")
total=p1.addition(5,6)
print(total)
p1.argtest(200)

p2 = myclass()
total=p2.numsum()
print(total)

p3= myclass()
p3.printrank("gamil.com")
num2= p3.num1
print(num2)