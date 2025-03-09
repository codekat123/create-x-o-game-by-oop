class calculator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operation = ""

    def numbers(self):
        while True:
            try:
                self.num1 = int(input("enter your first number: "))
                self.num2 = int(input("enter your second number: "))
                self.operation = input("what type your operation: ")
                if self.operation in ["+", "-", "*", "/"]:
                    break
            except ValueError:
                print("invalid value")

    def operation1(self):
        if self.operation == "+":
            print(self.num1 + self.num2)
        elif self.operation == "*":
            print(self.num1 * self.num2)
        elif self.operation == "-":
            print(self.num1 - self.num2)
        elif self.operation == "/":
            print(self.num1 / self.num2)

# Create an instance of the calculator class
object = calculator()
# Call the numbers method to get input from the user
object.numbers()
# Call the operation1 method to perform the calculation and print the result
object.operation1()



