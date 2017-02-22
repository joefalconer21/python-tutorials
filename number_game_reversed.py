import random

def game():
    upper = 10
    lower = 1

    # get a number from the user
    number = int(raw_input ("Tell me a number between {} and {}: ".format(lower, upper)))

    guesses = []
    successful = False

    while len(guesses) < 5:
        # the program makes a random guess between 1-10
        guess = random.randint(lower, upper)
        
        # keep making new guesses if repeats occur
        while guess in guesses:
            guess = random.randint(1, 10)
            
        # compare the program's guess to user's number
        if guess == number:
            successful = True
            print("I guessed your number! It was {}".format(number))
            break
        elif guess > number:
            print("{} is too high".format(guess))
            upper = guess - 1
        else:
            print("{} is too low".format(guess))
            lower = guess + 1

        guesses.append(guess)
        
    if not successful:
        print("Unlucky, I couldn't guess your number!")

    play_again = raw_input("Play again? Y/n ")
    if play_again.lower() == 'y':
        game()
    else:
        print("Bye!")

game()        
