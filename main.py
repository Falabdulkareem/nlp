# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#import sys
#import time
#import random
#import datetime 
import bottle
from bottle import route, run, template, request
import os
#import nltk
#import quepy
#from SPARQLWrapper import SPARQLWrapper, JSON
#from umbc2 import sss
import string
from Pattern import test_patterns
from Domain import ChooseDomain


bottle.debug(True)

@bottle.route("/")
def tryquestion():
    return template("index")
    
@bottle.post("/request")
def answerq():
    # For analysing purposes
    """
    #read file
    file = open('Domains/Transportation/RepairMeansOfTransport.txt', 'r')
    f = open("Domains/Transportation/RepairMeansOfTransportResults.txt", "w")
    DomainType = request.forms.get('optionsRadios')
    count = 1
    
    FirstMatch = 0
    SecondMatch = 0
    ThirdMatch = 0
    FourthMatch = 0
    FifthMatch = 0 
    NoMatch = 0

    for line in file:
        print line
        q = line
    
        GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, FirstMatch, SecondMatch, \
        ThirdMatch, FourthMatch, FifthMatch, NoMatch = ChooseDomain(q, DomainType, FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch)
        
        f.write(str(count) + "- " + "The highest matching goals for: " + line + "\n" + MatchingGoal + "\n" + SecondMatchingGoal + 
        "\n" + ThirdMatchingGoal + "\n" + FourthMatchingGoal + "\n" + FifthMatchingGoal + "\n\n")
        
        count = count + 1
    
    f.write("The count of the having the right goal the first option: " + str(FirstMatch) + "\n" + "The count of the having the right goal the second option: " + str(SecondMatch) + "\n" + 
    "The count of the having the right goal the third option: " + str(ThirdMatch) + "\n" + "The count of the having the right goal the fourth option: " + str(FourthMatch) + "\n" + 
    "The count of the having the right goal the fifth option: " + str(FifthMatch) + "\n" + "The count of not having the right goal in the first five options: " + str(NoMatch) + "\n" )
    
    file.close()
    f.close()
    """

    q = request.forms.get('input')
    
    ContainsRegex = request.forms.get('RegexRadios')
    print "regex is " + ContainsRegex
    
    if ContainsRegex == '1':
        # Add its, it's
        Preference, Goal, GoalForm, PrefForm = test_patterns(q, 1,
                                                [ '(.*) if (.*)', 
                                                  'is (.*?) keeping (.*)',  
                                                  'is (.*?) letting (.*)',  
                                                  'is (.*?) having (.*)',  
                                                  'is of (.*) to us (.*)',
                                                  'is of (.*) to me (.*)',
                                                  'is of (.*) for us (.*)',
                                                  'is of (.*) for me (.*)',
                                                  'is of (.*?) to (.*)',
                                                  'is of (.*?) that (.*)',
                                                  'is (.*) to me (.*)',
                                                  'is (.*) to us (.*)',
                                                  'is (.*?) to (.*)',
                                                  'is (.*) for me (.*)',
                                                  'is (.*) for us (.*)',
                                                  'is (.*?) for (.*)',
                                                  'is (.*?) that (.*)',
                                                  '(.*?) in (.*)',
                                                  'I am (.*?) in (.*)',
                                                  'I am (.*?) to (.*)',
                                                  '(.*?) to (.*)',
                                                  '(.*?) about (.*)',
                                                  '(.*?) on (.*)',
                                                 ])

        if Preference is None:
            Preference, Goal, GoalForm, PrefForm = test_patterns(q, 2,
                                                [ '(.*) is of (.*)',
                                                  'the importance of (.*) is (.*)', 
                                                  '(.*) is (.*)',  
                                                 ])
    
        # if there is a separate goal and preference, send only the goal to the semantic similarity function
        # if there was no prefernce specified, send all the sentence to the semantic similarity
        if Goal is not None:
            q = Goal
            print q
        else:
            Goal = q
        
    elif ContainsRegex == '2':
        Goal = q
        GoalForm = None
        Preference = "No preference option was chosen" 
        PrefForm = "No preference option was chosen"
        
    
    DomainType = request.forms.get('optionsRadios')
    ContainsRegex = request.forms.get('RegexRadios')
    print DomainType
    print "regex is " + ContainsRegex
    
    
    GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
    FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = ChooseDomain(q, DomainType, 0,0,0,0,0,0)
    
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
            GoalForm = "Negative"
        else:
            GoalForm = "Positive"
    
    
    return template("request", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MatchingGoal=MatchingGoal, SecondMatchingGoal= SecondMatchingGoal, 
        ThirdMatchingGoal= ThirdMatchingGoal, FourthMatchingGoal=FourthMatchingGoal, FifthMatchingGoal=FifthMatchingGoal, GoalForm=GoalForm, PrefForm=PrefForm)


bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))