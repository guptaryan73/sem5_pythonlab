class Adder:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
addition = Adder(5, 7)
result = addition.add()
print(f"The sum of {addition.num1} + {addition.num2} is {result}")
