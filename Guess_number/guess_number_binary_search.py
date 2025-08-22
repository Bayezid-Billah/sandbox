
def guess(low,high):

    status = ""
    feedback =""
    print(f"Welcome! I'll be guessing your number between {low} and {high} ! ")

    while status != "c":
        status = input(f"Is your number "+str(round(((high - low)/2+low)))+"\n (Higher: H, Lower: L, Correct: C):").lower()
        if status == "h":
            low = (high - low)/2 +  low
        elif status == "l":
            high = (high - low)/2 + low

    print("Yay! I guessed the number  Correctly!")
    
guess(int(input("Enter Lower Limit: ")),int(input("Enter Upper Limit: ")))
