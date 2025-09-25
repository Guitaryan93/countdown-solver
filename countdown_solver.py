# Countdown solver
import json


def sortLength(word):
    ''' passed as the "key" argument in the sort() function so results can
        be organized by length of the word. '''
    return len(word)


# Import the english word file and make into a list
with open("words_dictionary.json", "r") as file:
    eng_dict = json.load(file)
all_words = [word.lower() for word in eng_dict.keys()]

# Get the Countdown letters from the user
countdown_letters = input("Countdown Letters: ").lower()

# Loop over the list to build another list of words that
# match the 9 letters
matching_words = []
for word in all_words:
    chosen_letters = list(countdown_letters)
    
    # Need to check if first letter is in the list of 9
    # If it is then remove the letter from the list of 9
    # Then check the next letter and repeat
    # If the end of the word is reached then we add it to the
    # matching words list, otherwise just move on to the next word
    for letter in range(0, len(word)):
        # Use a try block because built-in index() method throws
        # an error if no index is found
        try:
            letter_index = chosen_letters.index(word[letter])
            chosen_letters.pop(letter_index)
            if letter == len(word) - 1:
                matching_words.append(word)

        except ValueError:
            break

matching_words.sort(key=sortLength)

for i in matching_words:
    if 3 < len(i) < len(countdown_letters):
        print(str(len(i)) + " - " + i)
    

