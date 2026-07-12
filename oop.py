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


## step 2
class Customer:
    def __init__(self, name, favorit_drink):
        self.name = name
        self.drink = favorit_drink

    def greet(self):
        print(f"Hi! I am {self.name} and I would like a {self.drink}.")

coustimr1 =  Customer("alice","latte" )
coustimr1.greet()
        