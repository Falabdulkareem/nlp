# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import time
import random
import datetime 
import bottle
from bottle import route, run, template, request
import os
import nltk
import quepy
from SPARQLWrapper import SPARQLWrapper, JSON
from umbc2 import sss
import string
from Pattern import test_patterns
from Domain import ChooseDomain

bottle.debug(True)

@bottle.route("/")
def tryquestion():
    return template("index")
    
@bottle.post("/request")
def answerq():
    q = request.forms.get('input')
    
    # Add its, it's
    Preference, Goal, GoalForm, PrefForm = test_patterns(q, 1,
                                            [ r'(.*) if (.*)', 
                                              r'is of (.*?) to us (.*)',
                                              r'is of (.*?) to me (.*)',
                                              r'is of (.*?) for us (.*)',
                                              r'is of (.*?) for me (.*)',
                                              r'is of (.*?) to (.*)',
                                              r'is of (.*) that (.*)',
                                              r'is (.*?) to me (.*)',
                                              r'is (.*?) to us (.*)',
                                              r'is (.*?) to (.*)',
                                              r'is (.*?) for me (.*)',
                                              r'is (.*?) for us (.*)',
                                              r'is (.*?) for (.*)',
                                              r'is (.*?) that (.*)',
                                              r'I am (.*?) in (.*)',
                                              r'I am (.*?) to (.*)',
                                             ])
                                             
    if Preference is None:
        Preference, Goal, GoalForm, PrefForm = test_patterns(q, 2,
                                            [ r'(.*) is of (.*)',
                                              r'the importance of (.*) is (.*)', 
                                              r'(.*) is (.*)',  
                                             ])
    
    # if there is a separate goal and preference, send only the goal to the semantic similarity function
    # if there was no prefernce specified, send all the sentence to the semantic similarity
    if Goal is not None:
        q = Goal
        print q
    else:
        Goal = q
    
    DomainType = request.forms.get('optionsRadios')
    print DomainType
    GoalsSimilarity, MaxScore = ChooseDomain(q, DomainType)
    
    if GoalForm is None:
        # Get a bag of words without punctuation
        words = [word.strip(string.punctuation) for word in q.split()]
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
            GoalForm = "The sentence is in negative form"
        else:
            GoalForm = "The sentence is in positive form"
    
    
    return template("request", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MaxScore=MaxScore, GoalForm=GoalForm, PrefForm=PrefForm)


bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))