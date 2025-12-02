class A:

    def __init__(self):
        print("Class A constructor")

class B(A):
    def __init__(self):
        print("Class B constructor")
        super().__init__()
obj= B()