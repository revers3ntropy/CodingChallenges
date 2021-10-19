class myClass():
    def __init__(self, property1):
        self.property1 = property1

    def myFunc(self):
        print(self.property1)

myObj = myClass(1)
myObj.myFunc()
