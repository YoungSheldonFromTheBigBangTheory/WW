#python3 -m pip install --upgrade termcolor
import math, sys, random, json, time
from termcolor import colored, cprint

pos = float(0)

wpm = 65 #wpm
def Type(t): #Word typing control
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/wpm)

def qBasic(q):
    while True:
        print('⇥', end='\r')
        time.sleep(1)
        print(' ', end='\r')
        time.sleep(1)

        temp = input("\n⇥")

while True: #Start Game
    temp = input("start game? y/n: ").lower()

    if temp == "yes" or temp == "y":
        break
    elif temp == "no" or temp == "n":
        sys.exit("Ok then")
    Type("Um what?")

print(pos)

while True:
    if pos == 0:
        Type("You find yourself on a rocky path in front of a slightly weathered, red bricked house")
        Type("\n1)Walk inside\n2)Continue path left\n3)Continue path right")
        
