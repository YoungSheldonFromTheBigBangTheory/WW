import time, json, sys, random, glob
from termcolor import colored, cprint
from Inventory import *

print(Inventory.inventory)

x = Items.Spoon
Inventory.inventory.append(x)

#x = input(str("input: "))
#Inventory.inventory.append(x)

for item in Inventory.inventory:
    item:Item
    print(item, item.Check(Items.Spoon))
   