#! python3
# scrabbleWordFinder.py - Shows possible words and scores based on a user's rack.
import copy

RACK = []
VALIDWORDS = []
WORDSINRACK = []
WORDSANDPOINTS = {}
POINTS = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2,
  	    'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3,
  	    'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1,
  	    'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4,
  	    'x': 8, 'z': 10}
RESULTS = {}

def getUserTiles():
    """
    Gets user's tiles.

    Returns:
        Dictionary containing individual letters in rack.

    """

    totalTiles = 7
    rack = []
    for i in range(totalTiles):
        currentTile = input('Input a letter: ')
        rack.append(currentTile)
    return rack

def loadDictionary():
    """
    Loads valid word list from text file.

    Returns:
        Dictionary containing valid words.
    """

    with open('words.txt', 'r') as f:
        sowpods = f.readlines()
    words = [x.strip() for x in sowpods]
    return words

def checkValid(word, rack):
    """
    Checks to see if a word can be made from rack.

    Parameters:
        word (str): Valid word
        rack (dict): Contains user's rack
    """

    tempRack = copy.deepcopy(rack)
    for letter in word:
        if letter in tempRack:
            tempRack.remove(letter)
        else:
            return False
    return True

def calculateScore(word):
    """
    Calculates the point value of valid word.

    Parameters:
        word (str): Valid word we want to calculate point value for
    Returns:
        score (int): Sum of letter's points in word
    """

    score = 0
    for letter in word:
        score += POINTS[letter]
    return score

if __name__ == '__main__':
    RACK = getUserTiles()
    VALIDWORDS = loadDictionary()

    for word in VALIDWORDS:
        wordStatus = checkValid(word, RACK)
        if wordStatus:
            WORDSINRACK.append(word)
        else:
            continue

    for word in WORDSINRACK:
        WORDSANDPOINTS[word] = calculateScore(word)

    RESULTS = sorted(WORDSANDPOINTS.items(), key=lambda x: x[1], reverse=True)

    print("Here are words and points based on your rack: ")
    for result in RESULTS:
        print(result[0], result[1])