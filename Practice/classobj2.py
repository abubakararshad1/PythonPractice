class testclass:
    num1= 100

    def sumofnum(self,a=10, b=5):
        print(a+b)
    def sumofnum2(self,a=10, b=5):
        self.a=1
        self.b=2
        print(a+b)
    def printname(self ,c,a=5,b=10):
        print("Hello my name is abubakar")
        self.a=1000
        self.b=5000
        print (a+b+3)

    def printname2 (self,c,a=5,b=10):
        a = 6
        b = 2
        c = 8
        print(c+a+b)

    def returntotal (self,x,y):
        return(x+y)

obj2= testclass()
obj2.printname2(1,2,5)



'''    
obj1 = testclass()
obj1.sumofnum2()
print(obj1.a)
print(obj1.b)
obj1.sumofnum2()
obj1.printname(21)
print(obj1.a+obj1.b)
obj1.printname(22)

'''
