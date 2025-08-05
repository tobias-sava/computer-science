# 17/04/2025

class SecretNote:
    def __init__(self, message, author, level):
        self.message = message
        self.author = author
        self.level = level

    def __str__(self):

        words = self.message.split() # creating list of words

        if self.level == 1:
            for i in range(len(words)): # looping through words list
                if (i + 1) % 3 == 0: # if third word
                    words[i] = "***" # replace with ***
                
            censored_message = " ".join(words) # joining list back into str

        elif self.level == 2:

            first = words[0] # storing first and last words
            last = words[-1]              

            words = words[1:-1]

            for i in range(len(words)):
                words[i] = "$@*&#"
            
            words.insert(0, first) # adding first and last words back
            words.append(last)
            
            censored_message = " ".join(words)

        elif self.level == 3:
            
            censored_message = "[REDACTED]"

        else:
            censored_message = "[ERROR]"
        
        return censored_message

note1 = SecretNote("This is a simple test message for SecretNote class", "Agent X", 1)
print(note1)  # Expected output: "This is *** test *** for SecretNote ***"

note2 = SecretNote("This is a simple test message for SecretNote class", "Agent X", 2)
print(note2)  # Expected output: "This $@*&# $@*&# $@*&# for $@*&# class"

note3 = SecretNote("This is a simple test message for SecretNote class", "Agent X", 3)
print(note3)  # Expected output: "[REDACTED]"

note4 = SecretNote("This is a simple test message", "Agent X", 99)
print(note4)  # Expected output: "[ERROR]"


            
