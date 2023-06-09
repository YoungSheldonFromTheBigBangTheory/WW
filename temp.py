#python3 -m pip install --upgrade termcolor
import math, sys, random, json, time, glob
from termcolor import colored, cprint

with open('textFile.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip() == "":
            print("emptyLine")
        else:
            print("Line")
f.close()