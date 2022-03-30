class functionDemo:
    def calculate(self, a, b):
        self.a=a
        self.b=b
        return a+b, a-b
    def calculation(self):
        a = int(input("\nEnter a number 'a':"))
        b = int(input("\nEnter a number 'b':"))
        print("\nThe Sum is:", a+b, "\nThe difference is:", a-b)
obj=functionDemo()
obj.calculation()
print("\n The sum and difference:", obj.calculate(5, 2))
