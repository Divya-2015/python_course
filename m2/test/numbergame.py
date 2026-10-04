print("WELLCOME TO MY NUMBER GUESSING GAME")

print("the rules are that u have five guesses to gess my secret number")

print("you will get hints")

secret = 32
secret = int(input("choose a number"))
guess = 5
while guess > 0:
    if secret == 32:
        print("well done you chose the correct number")
        break
    else:
    
        guess = guess - 1
        print("hint1: it is an even number")
        secret = int(input("choose a number"))
    if guess == 1:
        print("is divisible by 4")
        