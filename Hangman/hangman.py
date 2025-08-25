from words import words
import random
import string


def select_word():
    word = random.choice(words).upper()
    while ' ' in word or '-' in word:
        word = random.choice(words).upper()
    return word


def hangman():
    word = select_word()
    word_letters = set(word)
    used_letters = [] 
    all_letters = set(string.ascii_uppercase)

    lives = int(input("How many lives do you want ? \n"))

    print(" _"*len(word))
    
    while lives > 0 and not word_letters.issubset(used_letters):
        
        print("Hangman!! you have" ,lives," Lives left, You have used the letters: "," ".join(used_letters))
        shown_word = ("_ "*len(word))

        print("\n")
        letter = input("insert letter: ").upper()
        
        if letter in used_letters:
            print("You already guessed ",letter,"Guess again!")
        elif letter in word_letters:
            used_letters.append(letter)
            print("You guessed ",letter," Correctly!")
        else:
            print(letter," is incorrect, you lost one life. ")
            lives -= 1
        shown_word = " ".join([letter if letter in used_letters else "_" for letter in word])
        print("\n",shown_word,"\n")
                
    if lives == 0:
        print("You Died, The word was ",word)
    else:
        print("Congratulations, You win!")
        
        


hangman()
