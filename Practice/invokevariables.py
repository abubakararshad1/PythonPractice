a,b=10,20
class superkeyword:


    class car:
        a,b=100,200
        print("Car is BMW")
        print("Car is Toyota ")

    class mobile(car):
        a,b=1000,2000
        def total(self,a,b):
            print(a+b)
            print(self.a+self.b)
            print(super().a +super().b)
            print(globals()['a'] + globals()['b'])


myobj = superkeyword.mobile()
myobj.total(2,3)

