class parent:
    def abc(self):
        print("Hello this is abc")

class child(parent):
    def abc(self):
        print("Hello this is xyx")
        super().abc()

obj = child()
obj.abc()
