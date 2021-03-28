from OopsDemo import calculator # importing parent class

class ChildImp(calculator): # # to get properties of parent claddd
    num2  = 200

    def __init__(self):
        calculator.__init__(self, 2, 4)
        
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChildImp()
print(obj.getCompleteData())