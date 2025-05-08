class Calculator:
    """
    A simple Calculator class that provides basic arithmetic operations.

    Methods:
        add(a, b):
            Returns the sum of two numbers.
        subtract(a, b):
            Returns the difference between two numbers.
        multiply(a, b):
            Returns the product of two numbers.
        divide(a, b):
            Returns the quotient of two numbers. Raises a ValueError if the divisor is zero.
    """
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b