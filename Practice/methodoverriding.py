class shape():

    def draw(self):
        print("This is generic draw method")

class circle(shape):
    def draw(self):
        print("This is circle method")

class rectangle(shape):
    def draw(self):
        print("This is rectangle")

class square(shape):
    def draw(self):
        print("This is square")

cirobj= circle()
cirobj.draw()

sqrobj=square()
sqrobj.draw()

