# Classes are user defined blueprints or prototypes for objects
# sum, multiplication, addition, subtraction, constant
# methods, class variables, instance variables, constructor, etc.

class Calculator:
    num = 100
    # Default Constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("I am called automatically when an object is created")

    def get_data(self):
        print(self.num)
        return self.num

    def summation(self):
        return self.a + self.b + self.num

#my_calculator = Calculator(2,3)
#my_calculator.get_data()
#print(my_calculator.summation())

#my_calculator1 = Calculator(4,5)
#my_calculator1.get_data()
#print(my_calculator1.summation())
