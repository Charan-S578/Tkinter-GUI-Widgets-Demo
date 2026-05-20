def add(*args):
    print(args)

add(3, 5, 6)

def add(*args):
    print(type(args))

add(3, 5, 6)

def add(*args):
    for n in args:
        print(n)
add(3, 5, 6)

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
print(add(3, 5, 6))


def calculate(n, **Kwargs):
    # for key, value in Kwargs.items():
    #     print(key)
    #     print(value)
    n += Kwargs["add"]
    n *= Kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="Lamborgini", color="purple", seats=24)
print(my_car.color)