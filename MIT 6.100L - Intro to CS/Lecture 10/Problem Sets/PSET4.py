# 18/03/2025

def count_words(sen):
    """ sen is a string representing a sentence
    Returns how many words are in s (i.e. a word is a 
    sequence of characters between spaces)
    """

    split_sen = sen.split(' ') # Splitting sen into a new index every space encountered.
    
    return len(split_sen) # Returns the length of the list (counts each index).

print(count_words("Hello it's me"))

# Solved.