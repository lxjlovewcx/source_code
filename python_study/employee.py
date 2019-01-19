class Employee():
    def __init__(self,secondName,firstName,salery):
        self.secondName = secondName
        self.firstName = firstName
        self.salery = salery
    def give_raise(self,increase = 5000):
        self.salery += increase



