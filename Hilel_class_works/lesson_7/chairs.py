class Chair:
    def __init__(self, x, y):
        self.value = x

        if y not in [3, 7]:
            raise ValueError("y could be only 3 or 7")
        self.width = y

    def show_details(self):
        print(f"Chair(x: {self.value}, y: {self.width})")


chair_1 = Chair(x=10, y=3)
chair_2 = Chair(x=5, y=7)
chair_3 = Chair(x=5, y=2)


chair_1.show_details()
chair_2.show_details()


def foo(x):
    print(x)


foo(x=2)
foo(2)


data = [2]

foo(*data)


data = {"x": 2}

foo(**data)
