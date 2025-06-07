from OOPDemo import Calculator

class ChildDemo(Calculator):
    num2 = 200

    def __init__(self, a, b):
        Calculator.__init__(self, a, b)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

child_obj = ChildDemo(5, 7)
print(child_obj.getCompleteData())
