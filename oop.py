# ## step 1

# class Menultem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def describe(self):
#         print(f"item: {self.name}| price: {self.price}$")

# m1 = Menultem("espresso", 3.5)
# print(m1.__dict__)
# m1.describe()




# ## step 2
# class Customer:
#     def __init__(self, name, favorit_drink):
#         self.name = name
#         self.drink = favorit_drink

#     def greet(self):
#         print(f"Hi! I am {self.name} and I would like a {self.drink}.")

# coustimr1 =  Customer("alice","latte" )
# coustimr1.greet()

# ## step 3
# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name 
#         self.price = price

#     def describe(self):
#         print(f"item: {self.name} | price:  ${self.price}")

# cousumer1 = MenuItem("latte", 4.5)
# cousumer2 = MenuItem("Croissant", 2.0)
# cousumer3 = MenuItem("Cold Brew", 5.0)

# cousumer1.describe()
# cousumer2.describe()
# cousumer3.describe()

##step 4

class Customer:
    def __init__(self, name, balance):
        self.name = name 
        self.balance = balance

    def can_afford(self,price):
        if price <= self.balance:
            return True
        else:
            return False

clint1 = Customer("Bob", 10.0)
print(clint1.can_afford(8.0))
print(clint1.can_afford(12.0))

    

        