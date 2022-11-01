class Calculator():
    def __ini__(self):
        pass

    def Calculate(self, a, b, sign):
        if sign == '+':
            result = a + b
            return result
        elif sign == '-':
            result = a - b
            return result
        elif sign == '*':
            result = a * b
            return result
        elif sign == '/':
            result = a / b
            return result
