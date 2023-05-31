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

def qBasic():
    while True:
        temp = input("\n⇥   ")
        match temp:
            case "1":
                pos = tempPos1
                return pos
            case "2":
                pos = tempPos2
                return pos
            case "3":
                pos = tempPos3
                return pos    
            case "4":
                pos = tempPos4
                return pos
            case _:
                print("\nInvalid")

while True: #Start Game
    temp = input("start game? y/n: ").lower()

    if temp == "yes" or temp == "y":
        break
    elif temp == "no" or temp == "n":
        sys.exit("Ok then")
    Type("Um what?")

while True: #Pos 0
    
    if pos == 0:
        Type("You find yourself on a rocky path in front of a slightly weathered, red bricked house")
        Type("\n1)Walk inside\n2)Continue path left\n3)Continue path right")
        tempPos1 = 1
        tempPos2 = 0.1
        tempPos3 = 0.2
        qBasic()
        pos = qBasic()
    if pos == 1:
        Type("You find yourself at the entrance of the house")
        Type("\n1)Head upstairs\n2)Head straight towards kitchen\n3)Turn right to the living room\n4)Exit the house")
        tempPos1 = 1.2
        tempPos2 = 1.11
        tempPos2 = 1.12
        tempPos4 = 0
        qBasic()
        pos = qBasic()
