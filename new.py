import random 
# low = 1
# high = 100
# options = ("rock", "paper", "scissors")
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
# num = random.randint(low, high)
# num = random.random()
# option = random.choice(options)
random.shuffle(cards)
print(cards)