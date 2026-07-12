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

# ##step 5

# class MenuItem:
#     def __init__(self, name, price, in_stock):
#         self.name = name
#         self.price = price
#         self.in_stock = in_stock

#     def sell(self):
#         self.in_stock = False

#     def restock(self):
#         self.in_stock = True

#     def status(self): 
#         if self.in_stock:
#            print(f"{self.name} is in stock.") 
#         else:
#              print(f"{self.name} is sold out  ")

# clint2 = MenuItem("Muffin", 2.5, True)
# clint2.status()    
# clint2.sell() 
# clint2.status()     
# clint2.restock()
# clint2.status() 

# ##step 6
# class CoffeeShop:
#     def __init__(self, name, city, capacity):
#         self.name = name 
#         self.city = city
#         self.capacity = int(capacity)

#     def open_shop(self):
#             print(f"{self.name}is now open in {self.city}! Capacity: {self.capacity} seats")

#     def close_shop(self):
#          print(f"{self.name} is now closed. See you tomorrow!") 

        
# client = CoffeeShop("Brew House", "Tel Aviv", 40)
# client.open_shop()
# client.close_shop() 

# ##step 7
# class MenuItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         self.order_count = 0

#     def order(self):
#         self.order_count += 1
#         print(f"{self.name} ordered. Total orders: {self.order_count}")

# invitation =MenuItem("Cappuccino", 4.0)
# invitation.order()
# invitation.order()
# invitation.order()

# ##step 8
# class Order:
#     def __init__(self, customer_name, items):
#         self.customer = customer_name
#         self.items = items

#     def item_count(self):
#         print(f"items: {len(self.items)}")

#     def print_order(self):
#         print(f"Order for: {self.customer} ")
#         for self.item in self.items:
#             print(f"- {self.item}")

# order = Order("Dana", ["Latte", "Croissant", "OJ"])
# order.item_count()
# order.print_order()

# ##step 9
# class Barista:
#     def __init__(self, name, specialty ):
#         self.name = name 
#         self.specialty = specialty
#         self.drinks_made = 0

#     def make_drink(self, drink_name):
#         print(f"{self.name} made a {drink_name} ")
#         self.drinks_made += 1

#     def is_specialty(self, drink_name):
#         return self.is_specialty == drink_name
#         # self.drink = drink_name
#         # if drink_name == self.specialty:
#         #     return True
#         # else:
#         #     return False

#     def shift_summary(self):
#         print(f"{self.name} made {self.drinks_made} drinks today. ")

# waiter=Barista("Yossi", "Espresso")
# waiter.make_drink("cappuccino")
# waiter.make_drink("espresso")
# waiter.make_drink("americano")
# waiter.make_drink("coffe")


# print(waiter.is_specialty("Espresso"))

# waiter.shift_summary()




# ##step 10
# class Receipt:
#     def __init__(self, tax_rate):
#         self.tax = tax_rate
#         self.items = []

#     def add_item(self, name, price):
#         self.items.append((name,price))

#     def subtotal(self):
#         total_sum = 0
#         for item in self.items:
#             total_sum += item[1]
#         return total_sum

#     def tax_amount(self):
#         total = self.subtotal()
#         tax_total = total * self.tax
#         return tax_total

#     def total(self):
#         return self.subtotal() * 100/100 + self.tax_amount()

#     def print_receipt(self): 
#         for item in self.items:
#             name = item[0]
#             price = item[1]
#         print(f"- {name} ${price}")

#         print(f"Subtotal: ${self.subtotal()}")
#         print(f"tax ({int(self.tax * 100)}%)  ${self.tax_amount()}")
#         print(f"Total: ${self.total()}")

# receipt = Receipt(0.17)
# receipt.add_item("Latte", 4.5)
# receipt.add_item("Croissant", 2.0)
# receipt.add_item("Water", 1.5)

# receipt.print_receipt()



###Extra Exercises

# Extra 1. Category Filtering
class MenuItem:
    def __init__(self, name, price, category ):
        self.name = name
        self.price = price 
        self.category = category

    def is_drink(self): 
        return "drink" in self.category

    def is_cheap(self, limit):
        return self.price < limit

item1=MenuItem("Espresso", 3.5, "hot drink") 
print(item1.is_drink())
print(item1.is_cheap(3.0)) 

item2=MenuItem("Muffin", 2.0, "food")
print(item1.is_drink())
print(item1.is_cheap(3.0))

item3=MenuItem("coffe", 2.5, "hot drink")
print(item1.is_drink())
print(item1.is_cheap(3.0))

item4=MenuItem("sandwich", 5.0, "food")
print(item1.is_drink())
print(item1.is_cheap(3.0))



        


