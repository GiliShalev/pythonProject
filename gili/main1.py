from gili.Car import Car, MotorCycle

volvo = MotorCycle(4)
volvo.pr()
volvo.pr1()
volvo.pr1(12)
volvo.static_func()
Car.static_func()
Car.pr(volvo)

