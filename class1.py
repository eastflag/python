class Calculator:
    def __init__(self):
        self.result = 0;

    def adder(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.adder(3))
print(cal1.adder(4))

print(cal2.adder(4))
print(cal2.adder(5))

print(cal1.result)
print(type(cal1))