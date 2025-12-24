import random

result = ["win", "loss"]
i = 1
goal = int(input("Enter the goal"))

def play_gambling(result, i):
    while(i >= 1):
        if(random.choice(result) == "win"):
            i *= 2
            print("Win ", i)
        else:
            i /= 2
            print("Loss ", i)
play_gambling(result, i)