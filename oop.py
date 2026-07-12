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
# # cousumer3.describe()

# ##step 4

# class Customer:
#     def __init__(self, name, balance):
#         self.name = name 
#         self.balance = balance

#     def can_afford(self,price):
#         if price <= self.balance:
#             return True
#         else:
#             return False

# clint1 = Customer("Bob", 10.0)
# print(clint1.can_afford(8.0))
# print(clint1.can_afford(12.0))

##step 5

class MenuItem:
    def __init__(self, name, price, in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock

    def sell(self):
        self.in_stock = False

    def restock(self):
        self.in_stock = True

    def status(self): 
        if self.in_stock:
           print(f"{self.name} is in stock.") 
        else:
             print(f"{self.name} is sold out  ")

clint2 = MenuItem("Muffin", 2.5, True)
clint2.status()    
clint2.sell() 
clint2.status()     
clint2.restock()
clint2.status() 

##step 6
class CoffeeShop:
    def __init__(self, name, city, capacity):
        self.name = name 
        self.city = city
        self.capacity = int(capacity)

    def open_shop(self):
            print(f"{self.name}is now open in {self.city}! Capacity: {self.capacity} seats")

    def close_shop(self):
         print(f"{self.name} is now closed. See you tomorrow!") 

        
client = CoffeeShop("Brew House", "Tel Aviv", 40)
client.open_shop()
client.close_shop()   

        