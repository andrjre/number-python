SECRET_NUMBER = 10
guess = 1

while int(guess) != SECRET_NUMBER:
    guess = input("What is your guess: ")
    if(int(guess) == SECRET_NUMBER):
        print("You got it!")#
        break
    else:
        print("Not quite...")