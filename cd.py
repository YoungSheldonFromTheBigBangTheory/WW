import time, json, sys, random, glob
from termcolor import colored, cprint
from Inventory import *

print(Inventory.inventory)

x = Items.Spoon
Inventory.inventory.append(x)

print(*Inventory.inventory, sep = "\n")

#x = input(str("input: "))
#Inventory.inventory.append(x)

#for item in Inventory.inventory:
    #item:Item
    #print(item, item.Check(Items.Spoon))

for item in Inventory.inventory:
    item:Item
    if item.Check(Items.Spoon) is True:
        print("a")
   