import random
secretword="secret","pie","apple","hi","supercalifragisticsuperalidoshish"
x= random.choice(secretword)
wordToGuess="-"*len(x)
attempt= 1
while(1):
    print wordToGuess
    guess=raw_input("what is your guess? has to be a letter")
    if guess in x:
        for i in range(len(x)):
            if x[i]==guess:
                wordToGuess=wordToGuess[:i]+guess+wordToGuess[i+1:]
    else:
        print "Wrong try again"
        attempt+=1
    if wordToGuess==x:
        print "Congrates you win"
        print "Now it's your opponent's turn"
        print "run this again for the next turn"
        quit()
    if attempt >=6:
        print "you lose"
        print "The secret word was "+ x
        print "Try again next time"
        quit()
