import math, sys, random, json

pos = str(0)

while True:
    temp = input("start game? y/n: ").lower()

    if temp == "yes" or temp == "y":
        break
    elif temp == "no" or temp == "n":
        sys.exit("Ok then")
    print("Um what?")

while True:
    if pos == 0:
        print("You find yourself on a rocky path in front of a slightly weathered, red bricked house")
