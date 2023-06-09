import json
with open("move.json", "r") as f:
    flubb = json.loads(f.read())

while True:

    print(flubb["move"])
    print("Answer 1:",(flubb["newPos"][0]))
    print("Answer 2:",(flubb["newPos"][1]))
    print("Answer 3:",(flubb["newPos"][2]))
    print("Answer 4:",(flubb["newPos"][3]))

    b = str(input("\nChoose Move "))

    print(flubb["updtPos"])

    if b == (flubb["Correct"]):
        print("\nCorrect")
        break
    if b != (flubb["Correct"]):
        print("\nIncorrect! Please try again!")