from multipledispatch import dispatch

class A:
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)

    @dispatch(float,float,int,int)
    def add(self,a,b,c,d):
        print(a+b+c+d)

objadd= A()
objadd.add(1,2)
objadd.add(1.1,1.1,5,5)
