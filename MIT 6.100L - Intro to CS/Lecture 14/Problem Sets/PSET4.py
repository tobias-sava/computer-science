# 23/03/2025

song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"

def generate_word_dict(song):
    
    # Cleaning the string.

    song_words = song.lower()

    words_list = song_words.split() # Splits the string into a list at every space.

    word_dict = {} # Init empty dict that will store str:int values.

    for w in words_list: # Iterating through the words list.
        if w in word_dict: # If we already have the value in the dict:
            word_dict[w] += 1 # Adding +1 to value.
        else:
            word_dict[w] = 1 # Otherwise, adding the key with value 1.
    
    return word_dict

print(generate_word_dict(song)) # Prints {'rah': 2, 'ah': 3, 'rom': 1, 'mah': 3, 'ro': 1}

def find_frequent_word(word_dict):

    words = []

    highest = max(word_dict.values()) # Storing the highest value in dict by grabbing values.

    for k, v in word_dict.items(): # Iterating through the k, v items.
        if v == highest:
            words.append(k)
    
    return (words, highest)