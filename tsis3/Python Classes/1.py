class twoMethods:
    def __init__(self):
        self.my_string: ""

    def getString (self):
        self.my_string = input("")

    def printString (self):
        print(self.my_string.upper())

two_method = twoMethods()
two_method.getString()
two_method.printString()
