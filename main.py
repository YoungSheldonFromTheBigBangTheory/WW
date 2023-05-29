import math, json

p = int(1000)

cards = []
cardsTemp = []

with open("cards.json", "r") as cards, open("cardsTemp.json", "w") as cardsTemp:
    cardsTemp.write(cards.read())