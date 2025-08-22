import random

def iswin(user,computer):
    
    if (user == "r" and computer == "s") or (user == "p" and computer =="r") or (user == "s" and computer =="p"):
        return f"You picked {user} and Computer picked {computer} You Win"
    if (user == "r" and computer == "p") or (user == "p" and computer =="s") or (user == "s" and computer =="r"): 
        return f"You picked {user} and Computer picked {computer} You Lose"
    else:
        return f"You both picked {user} It's a draw"
    print("CHECK!")

def play():

    computer = random.choice(["r","p","s"])
    user = str(input("press 'r' for Rock, 'p' for paper and 's' for sissor :"))
    
    print(iswin(user,computer))

play()
