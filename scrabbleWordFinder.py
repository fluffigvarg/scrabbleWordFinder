#! python3
# scrabbleWordFinder.py - Shows possible words and scores based on a user's rack.
import copy

rack = []
valid_words = []
words_in_rack = []
words_and_points = {}
points = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2,
  	    'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3,
  	    'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1,
  	    'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4,
  	    'x': 8, 'z': 10}
results = {}

def get_user_tiles() -> list:
    """
    Gets user's tiles.

    Returns:
        List containing individual letters in rack.

    """

    total_tiles = 7
    temp_rack = []
    while len(temp_rack) < total_tiles:
        current_tile = input('Input a letter: ').lower()
        try:
            if points[current_tile] > 0:
                temp_rack.append(current_tile)
        except:
            print('Invalid letter! Try again')
    return temp_rack

def load_dictionary() -> list:
    """
    Loads valid word list from text file.

    Returns:
        List containing valid words.
    """

    with open('words.txt', 'r') as f:
        sowpods = f.readlines()
    words = [x.strip() for x in sowpods]
    return words

def check_valid(word: str, rack: list) -> bool:
    """
    Checks to see if a word can be made from rack.

    Parameters:
        word (str): Valid word
        rack (list): Contains user's rack
    """

    temp_rack = copy.deepcopy(rack)
    for letter in word:
        if letter in temp_rack:
            temp_rack.remove(letter)
        else:
            return False
    return True

def calculate_score(word: str) -> int:
    """
    Calculates the point value of valid word.

    Parameters:
        word (str): Valid word we want to calculate point value for
    Returns:
        score (int): Sum of letter's points in word
    """

    score = 0
    for letter in word:
        score += points[letter]
    return score

if __name__ == '__main__':
    rack = get_user_tiles()
    valid_words = load_dictionary()

    for word in valid_words:
        word_status = check_valid(word, rack)
        if word_status:
            words_in_rack.append(word)

    for word in words_in_rack:
        words_and_points[word] = calculate_score(word)

    results = sorted(words_and_points.items(), key=lambda x: x[1], reverse=True)

    print("Here are words and points based on your rack: ")
    for result in results:
        print(result[0], result[1])