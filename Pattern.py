# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$1-Oct-2014 12:31:07 PM$"

import re
import string

def test_patterns(text, Pref_loc, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Show the character positions and input text
   # print
   # print ''.join(str(i/10 or ' ') for i in range(len(text)))
   # print ''.join(str(i%10) for i in range(len(text)))
   # print text

    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            '''
            s = match.start()
            e = match.end()
            print '  %2d : %2d = "%s"' % \
                (s, e-1, text[s:e])'''
            if match:
                print match.group(1)
                print match.group(2)
                
                # Get a bag of words without punctuation
                if Pref_loc == 1:
                    Pref_words = [word.strip(string.punctuation) for word in match.group(1).split()]
                    Goal_words = [word.strip(string.punctuation) for word in match.group(2).split()]
                else:
                    Pref_words = [word.strip(string.punctuation) for word in match.group(2).split()]
                    Goal_words = [word.strip(string.punctuation) for word in match.group(1).split()]
                
                print Pref_words
                print Goal_words

                # Create a list and add the words to the list
                Pref_list = [] 
                Goal_list = []
                for current_word in Pref_words:
                    Pref_list.append(current_word.lower())
                    
                for current_word in Goal_words:
                    Goal_list.append(current_word.lower())

                # Create a list with negative words
                NegativeWords = ["not", "haven't", "havent", "hasn't", "hasnt", "didn't", "didnt", "doesn't",\
                "doesnt", "don't", "dont", "shouldn't", "shouldnt", "couldn't", "couldnt", "can't", "cant", "cannot", \
                "no" , "nobody"]

                # Check if the sentence written have any negative words
                Pref_FoundNeg = set(NegativeWords).intersection(Pref_list)
                Goal_FoundNeg = set(NegativeWords).intersection(Goal_list)
                print Pref_FoundNeg
                print Goal_FoundNeg

                if Pref_FoundNeg:
                    PrefForm = "Negative"
                else:
                    PrefForm = "Positive"
        
                if Goal_FoundNeg:
                    GoalForm = "Negative"
                else:
                    GoalForm = "Positive"
                    
                print PrefForm
                print GoalForm
                
                if Pref_loc == 1:
                    return match.group(1), match.group(2), GoalForm, PrefForm 
                else:   
                    return match.group(2), match.group(1), GoalForm, PrefForm 
    return None, None, None, None
            
            
            
    