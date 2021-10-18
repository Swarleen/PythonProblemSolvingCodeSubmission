from ps3a import *
import time
from perm import *

#
#
# Problem #6A: Computer chooses a word
##Name: Swarleen Bhamra
##Time Spent: 5-6 days

def comp_get_valid_words_with_scores(hand, word_list):
    """
    Given a hand and a word_list, returns a list of valid words
        sorted in descending order according to their word scores
    
    return list ( tuple (int,string) ) sorted according to int,
        or None if no valid words are found

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    for word in word_list:
        if is_valid_word (word, hand, word_list):
            score = get_word_score(word, HAND_SIZE)
        else:
            break



def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_list, find a valid word, and return it.
    This word should be calculated by considering all possible permutations
    of lengths 1 to hand length.
    
    Hint: First try to make a legal player, and then worry about making
    the computer player better (if you have time). 

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    # Initiallising a new variable from 0, which will store max score.
    top_score=0
    top_word = []
    # Assigning word_in_wordlist for every word in wordlist.
    word_in_wordlist = set(word_list)
    for word in word_list:
    # If word is made from given hand.
        if is_valid_word (word, hand, word_in_wordlist):
    # Calculate the score by the worth of the word you made.
            score = get_word_score(word, HAND_SIZE)
    # If the score is greater than top score
            if score > top_score:
    # new top score and word shall be updated here.
                top_score=score
                top_word = word
    return top_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO...
    final_score=0
    alphabets_left=len(hand)
    if alphabets_left > 0:
    # Printing the remaining alphabets of the hand.
        print('Leftover Hand: ',display_hand(hand))
        word = comp_choose_word(hand, word_list)
        if not word:
            pass
        else:
    # Showing the player how many hands they have gained.
            final_score += get_word_score(word, HAND_SIZE) 
            print(word + 'earned' + get_word_score(word, HAND_SIZE) +'scores. Final: ' + final_score + 'score.')
    # Giving a new updated hand. 
            hand = update_hand(hand, word)
            alphabets_left = calculate_handlen(hand)
    print(final_score + 'points, are the final score.')


    
#
# Problem #6C: Playing a game
#
#

def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    hand = {}
    while True:
    # It will start by the following line.
        text_input= input ("enter n to play new hand -- r to play the last hand again -- e to exit the game: ")
    # If the user presses n, he'll get a hand.
        if text_input =='n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand, word_list, HAND_SIZE)
    # If he chooses r, he'll get the last hand.
        elif text_input =='r':
            if hand:
                play_hand(hand, word_list, HAND_SIZE)
            else:
                print('Wrong request! no hand is played tillnow.' + 'Please play a new hand')
            pass
     # If presses e, then break and stop (exit)
        elif text_input =='e':
            break
        else:
            print("invalid Input")
            continue
        if text_input== 'n':
            hand = deal_hand(HAND_SIZE)
        while True:
            text_input= input('Press u for a user or c' + 'for a Computer: ').lower()
            if text_input == 'u':
                play_hand(hand, word_list, HAND_SIZE)
                break
            if text_input=='c':
                comp_play_hand(hand, word_list)
                break

#
# Build data structures used for entire session and play game.
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
