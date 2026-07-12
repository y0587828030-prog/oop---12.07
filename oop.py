## step 1

class Menultem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"item: {self.name}| price: {self.price}$")

m1 = Menultem("espresso", 3.5)
print(m1.__dict__)
m1.describe()


