from typing import overload
from typing_extensions import override

class Car1:
    def __init__(self, x):
        self.x = x + 1

    def pr(self):
        print(self.x)

class Car:
    d = 88

    @staticmethod
    def static_func():
        print(Car.d)
        Car.d = 99
        print(Car.d)

    def __init__(self, x):
        self.x = x + 1

    def pr(self):
        print(self.x * 2)

    def pr1(self, y = 10):
        print(self.x * 2 + y)

class MotorCycle(Car, Car1):
    def __init__(self, x):
        Car.__init__(self, x)
        Car1.__init__(self, x)
        self.x = x

    @override
    def pr1(self, y = 13):
        super().pr1()
        Car.pr1(self)
        Car1.pr(self)
        print("More: " + str(y))

# def ttt():
#     print("frfr")
#
# ttt()