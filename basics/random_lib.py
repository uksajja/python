import random
#choice()
coin = random.choice(["heads", "tails"])
print(coin)
#randint()
while True:
    x = random.randint(1, 10)
    print(f"x is : {x}")
    if x==5:
        print(f"Fianlly x is 5")
        break
cards = ["jack", "queen", "king"]
#shuffle()
random.shuffle(cards)
print(cards) #prints with list syntax
print("loop:")
for card in cards: #print just each card on a new line without square brackets
    print(card)