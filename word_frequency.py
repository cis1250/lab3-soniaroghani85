#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

user_sentence = input("Enter a sentence: ")

while (is_sentence(user_sentence) == False):
    print("This does not meet the criteria for a sentence.")
    user_sentence = input("Enter a sentence: ")


sentence_clean = re.sub(r'[^\w\s]', '', user_sentence).lower()
words = sentence_clean.split()

word_list = []
freq_list = []

for word in words:
    if word in word_list:
        index = word_list.index(word)
        freq_list[index] += 1
    else:
        word_list.append(word)
        freq_list.append(1)


for i in range(len(word_list)):
    print(f"{word_list[i]}: {freq_list[i]}")
    
