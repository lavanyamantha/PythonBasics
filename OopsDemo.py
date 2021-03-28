#self keyword is mandatorry for calling varable names into method
#instance and class variables have whole different purpose
#constructor name should be __init
#new keyword is not required when you create object
class calculator:
    num = 100 # class variables

    #defalult constructor
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("I am constructor called automatically when object initialized")

    def getData(self):
        print("I am now executing as method in class")


    def Summation(self):
        return self.a + self.b + calculator.num

#this is way to create object without new operator

obj = calculator(2,3)
obj.getData()
print(obj.num)

obj1 = calculator(4,5)
obj.getData()
