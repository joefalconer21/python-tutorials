import random

# a list of random words
words = ["car", "train", "boat", "bicycle", "motorcycle"]

def game():
    # user gets 10 chances
    chances = 10

    # program chooses one of those words
    rand_word = words[random.randint(0, len(words) - 1)]
    
    # store the number of good letters needed to win
    letters_needed = len(rand_word)

    # create a place holder to add good letters
    good_guesses = ""
    for letter in rand_word:
        good_guesses += "_"
    
    # split good_guesses into an array
    good_letters = list(good_guesses)          

    # format some starting space
    print("""
    =============================== Let's start a new game =================================
    """)

    # the program asks us for letters
    while chances and letters_needed:
        
        # show the word so far
        print("    The word: " + good_guesses)

        letter = raw_input("    Type in a letter: ").lower()
        if len(letter) > 1:
            print("""
    Only one letter!
            """)
        else:
            # for good guesses
            if letter in rand_word:
                print("""
    {} is a good letter!
                """.format(letter))
            
                letters_needed -= 1
                
                # get the position of correct letter
                letter_position = rand_word.index(letter)
                
                # add the good letter to the array
                good_letters[letter_position] = letter
                good_guesses = "".join(good_letters)
            
            # for bad guesses
            else:
                chances -= 1
                print("""
    {} is not in my word. You have {} chances left...
                """.format(letter, chances))
                       
    # display game ending
    if not letters_needed:
        print("    Well done! You guessed my word, which was {}.".format(rand_word))
    else:
        print("    Unlucky. Try brushing up on your vocabulary!") 

    # give the option of starting a new game
    play_again = raw_input ("""
    Do you want to play again? Y/n 
    """)
    if play_again.lower() == 'y':
        game()
    else: 
        print("""
    =============================== Bye! ================================
        """)
              
game()  

