import random

# create a list of random words
words = ["car", "train", "boat", "bicycle", "motorcycle"]

def game():
    # user gets 10 chances
    chances = 10

    # program chooses a word at random
    secret_word = words[random.randint(0, len(words) - 1)]
    
    # store number of letters to solve
    letters_to_solve = len(secret_word)

    # create a representation of the word with underscores
    solved_word = ""
    for letter in secret_word:
        solved_word += "_"
    
    # split that representation into an array
    solved_letters = list(solved_word)          

    # format some starting space
    print("""
    ========================== Try to guess my word! ============================
    """)

    # the game ends in the event of success or failure
    while chances and letters_to_solve:
        
        # show the representation of the word
        print("    The word: " + solved_word)
        
        # get a letter from the user
        guess = raw_input("    Type in a letter: ").lower()
        
        # make sure it's a single letter
        if len(guess) > 1:
            print("""
    Enter just one letter!
            """)
        elif len(guess) < 1:
            print("""
    Enter at least one letter!
            """)
        else:
            # for good guesses
            if guess in secret_word:
                print("""
    {} is a good letter!
                """.format(guess))

                # create a new list to store positions
                solved_letter_positions = []
            
                # get the positions of correct letter
                solved_letter_positions = [i for i, letter in enumerate(secret_word) if letter == guess]
                
                # add the good letter to solved_letters list in all correct positions
                for position in solved_letter_positions:
                    solved_letters[position] = guess
                    letters_to_solve -= 1               
                
                # rebuild the representation to display
                solved_word = "".join(solved_letters)
            
            # for bad guesses
            else:
                chances -= 1
                print("""
    {} is not in my word. You have {} chances left...
                """.format(guess, chances))
                       
    # display game ending
    if not letters_to_solve:
        # remove the solved word from program        
        words.remove(secret_word)
        print("""
    Well done! You guessed my word, which was {}.
        """.format(secret_word))
    else:
        print("""
    Unlucky. Try brushing up on your vocabulary!
        """) 

    # give the option of starting a new game
    if words:
        play_again = raw_input ("    Do you want to play again? Y/n ")
        if play_again.lower() == 'y':
            game()
        else: 
            print("""
    ========================== Bye! ===========================
            """)
    else: 
        print("""
    ========================== You guessed all my words!  ===========================
        """)
                      
game()  

