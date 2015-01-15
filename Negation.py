# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$15-Jan-2015 1:29:51 PM$"

import string

def Find_Negation(s):
    # Get a bag of words without punctuation
    words = [word.strip(string.punctuation) for word in s.split()]
    print words

    # Create a list and add the words to the list
    my_list = [] 
    for current_word in words:
        my_list.append(current_word.lower())

    # Create a list with negative words
    NegativeWords = ["not", "haven't", "havent", "hasn't", "hasnt", "didn't", "didnt", "doesn't",\
    "doesnt", "don't", "dont", "shouldn't", "shouldnt", "couldn't", "couldnt", "can't", "cant", "cannot", \
    "no" , "nobody"]

    # Check if the sentence written have any negative words
    FoundNeg = set(NegativeWords).intersection(my_list)
    print FoundNeg

    if FoundNeg:
        return "Negative"
    else:
        return "Positive"