from Bicycles import *

# dan = Customer("dan", 200)
# jessie = Customer("jessie", 500)
# brock = Customer("brock", 1000)
#
# shop = Shop("Blannigan's Bikes")
#
# # Create each bike object
# bike1 = Bicycle("Corvair", 20, 150)
# bike2 = Bicycle("Airstream", 18, 200)
# bike3 = Bicycle("Slipstream", 25, 100)
# bike4 = Bicycle("Monty", 16, 400)
# bike5 = Bicycle("Zuul", 10, 800)
# bike6 = Bicycle("Ratman", 13, 650)
#
# shop.initial_inventory(bike1, 1)
# shop.initial_inventory(bike2, 1)
# shop.initial_inventory(bike3, 1)
# shop.initial_inventory(bike4, 1)
# shop.initial_inventory(bike5, 1)
# shop.initial_inventory(bike6, 1)


print("Welcome to {}".format(shop.name))
print("Here the bikes we carry:")
for bicycle in shop.inventory:
    print("Name: {}".format(bicycle.model))
    print("Weight: {} lbs".format(bicycle.weight))
    print("Cost: ${}".format(bicycle.cost))
print("\n")

# Customer 1
print("Dan's budget = ${}".format(dan.money))
for bike in shop.show_inventory():
    dan.bikes_avail(bike)
for item in dan.show_bikes_avail():
    print(item)
dan.purchase()
print("\n")

# Customer 2
print("Jessie's budget = {}".format(jessie.money))
for bike in shop.show_inventory():
    jessie.bikes_avail(bike)
for item in jessie.show_bikes_avail():
    print(item)
jessie.purchase()
print("\n")

# Customer 3
print("Brocks's budget = {}".format(brock.money))
for bike in shop.show_inventory():
    brock.bikes_avail(bike)
for item in brock.show_bikes_avail():
    print(item)
brock.purchase()
