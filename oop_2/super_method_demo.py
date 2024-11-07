# program for super()

class Car:

    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started ..")

    @staticmethod
    def stop():
        print("car stopped ..")


class ToyotaCar(Car):

    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()


car1 = ToyotaCar("fortuner", "electric")

print(car1.name)
print(car1.type)     #Accessing base/ parent class's method 