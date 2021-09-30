# Program Solving with Python/Intro to Competitive Programming, Fall 2021
# Eternal University, Baru Sahib
# Cite: John Guttag. 6.00SC Introduction to Computer Science and Programming. Spring 2011. Massachusetts Institute of Technology: MIT OpenCourseWare, https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011. License: Creative Commons BY-NC-SA.
#
#
# Problem Set 2
# Hangman
# Name: Swarleen Bhamra
# Time spent: 3-4 days



# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
print("Welcome to the game, Hangman!")

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
##    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
##    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!
                
def hangman(): 
    x = choose_word(wordlist)
    y = ['a b c d e f g h i j k l m n o p q r s t u v w x y z']
    # Printing the length of random word with the help of choose_word function above.
    print('I am thinking of a word that is ' + str(len(x)) +' letters long.')
    # Setting number of guesses double as the length.
    num_of_guess = len(x) * 2
    # Making an empty list in which the words which are guessed will be stored.
    guess = ''
    while(num_of_guess !=0):
        print('----------------------------')
        print('You have '+ str(num_of_guess) +' guesses left.')
        print('Available letters:',''.join(y))
        letter = input("Please guess a letter: ")
        # Appending the guessed word in the guess list and using (.lower) for bring each letter in small.
        guess = guess +letter.lower()
        word = ''
        for char in x:
            # If the guessed letter matches any of the letter in the sceret word, the will be shown in the panel.
            if char in guess:
               word = word + char + ' '
            # Else panel will be shown same as it it was last filled.   
            else:
                word = word + ' ' 
        print('')           
        if letter in x:
           # If letter matches, it will show: good guess
           print('Good guess:',word)
           if letter in y:
              y.remove(letter) 
           if word.replace(' ','') == x:
               return True    
        else:
            # If not then this:
            print('Oops! That letter is not in my word:' ,word)
            if letter in y:
                y.remove(letter)
            num_of_guess = num_of_guess - 1  
    print("You loose")
    print('Word was',x)        

# When all letter are filled then it will reach here.
if hangman():
    print("Congratulation, you won!")  
        
        
    
    
    


    
