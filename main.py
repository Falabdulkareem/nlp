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
#import MySQLdb
from Negation import Find_Negation



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
    
    # convert to lowercase
    q = q.lower()
    
    ContainsRegex = request.forms.get('RegexRadios')
    print "regex is " + ContainsRegex
    
    if ContainsRegex == '1':
        Preference, Goal, GoalForm, PrefForm = test_patterns(q, 3,
                                                [ 'upmost importance (.*)',
                                                  'you must (.*)',
                                                  'it is most important (.*)',
                                                  'must complete (.*)',
                                                  'never ignore (.*)',
                                                  '(.*) must be achieved before another task is started',
                                                  '(.*) must be achieved',
                                                  '(.*) must be completed',
                                                  'without achieving (.*), there is no purpose of (.*)',
                                                  '(.*) must be at the top of the priority list',
                                                  '(.*) cannot be neglected',
                                                  '(.*) requires immediate attention',
                                                  'under no circumstances should you not (.*)',
                                                  '(.*) should be completed as soon as possible',
                                                  'let go of anything and do (.*)',
                                                  '(.*) need to be achieve at 100 percent of the goal',
                                                 ])
                                                 
        if Preference is None:    
            Preference, Goal, GoalForm, PrefForm = test_patterns(q, 1,
                                                    [ 'is (.*) if (.*)',
                                                      '(.*) if (.*)', 
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
                                                      'is (.*) we (.*)',
                                                      'is (.*) to us (.*)',
                                                      'is (.*?) to (.*)',
                                                      'is (.*) for me (.*)',
                                                      'is (.*) for us (.*)',
                                                      'is (.*?) for (.*)',
                                                      'is (.*?) that (.*)',
                                                      '(.*?) that (.*)',
                                                      'is (.*?) in (.*)',
                                                      '(.*?) in (.*)',
                                                      '(.*?) is to (.*)',
                                                      'I am (.*?) in (.*)',
                                                      'I am (.*?) to (.*)',                                                    
                                                      '(.*?) on (.*)',
                                                      '(.*?) to (.*)',
                                                      '(.*?) about (.*)',
                                                      'you (.*) achieve (.*)',
                                                      '(.*) achieving (.*)',
                                                     ])

        if Preference is None:
            Preference, Goal, GoalForm, PrefForm = test_patterns(q, 2,
                                                [ '(.*) is of (.*)',
                                                  '(.*) has the (.*)',
                                                  '(.*) has (.*)',
                                                  '(.*) can be (.*)',
                                                  '(.*) by any means (.*)',
                                                  'the importance of (.*) is (.*)', 
                                                  '(.*) is (.*)',  
                                                 ])
                                                 
        
        """                                     
        if Preference is not None:
            # Open database connection
            db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="mysql")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            try:
                # Check if the Preference is already in DB and get the Count
                cursor.execute("Select * from Hundred_Percent where Pref = %s", [Preference])
                result = cursor.fetchone()
                count = result[2]
                count = count+1
                print "this is the count"
                print count

                cursor.execute ("UPDATE Hundred_Percent SET Count=%s WHERE Pref=%s", (count,[Preference]))

            # if Preference is not in DB, INSERT it.
            except:
                # Execute the SQL command
                cursor.execute("INSERT INTO Hundred_Percent(Pref, Count) VALUES (%s,%s)", (Preference,1))
                # Commit your changes in the database
                db.commit()

            # Fetch a single row using fetchone() method.
            data = cursor.fetchone()
            #print data

            # disconnect from server
            db.close()

            # write the Preference in File
            with open("Pref/Hundred.txt", "a") as Pref_file:
                Pref_file.write(Preference + "\n")
            Pref_file.close()
        
        """  
        
        # if there is a separate goal and preference, send only the goal to the semantic similarity function
        # if there was no prefernce specified, send all the sentence to the semantic similarity
        if Goal is not None:
            q = Goal
            print "If Goal is not none print Q"
            print q
        else:
            # The goal part specified in the interface will be the whole sentence
            Goal = q
        
    elif ContainsRegex == '2':
        Goal = q
        GoalForm = None
        Preference = "No preference option was chosen" 
        PrefForm = "No preference option was chosen"
        
    # Get the Domain and if the sentence contains regex or not
    DomainType = request.forms.get('optionsRadios')
    ContainsRegex = request.forms.get('RegexRadios')
    print DomainType
    print "regex is " + ContainsRegex
    
    # Get the highest matching goals for the entered sentence 
    GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
    FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = ChooseDomain(q, DomainType, 0,0,0,0,0,0)
    
    # if the sentence didn't contains preference, and was not checked for negation
    if GoalForm is None:
        GoalForm = Find_Negation(q)
    
    return template("request", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MatchingGoal=MatchingGoal, SecondMatchingGoal= SecondMatchingGoal, 
        ThirdMatchingGoal= ThirdMatchingGoal, FourthMatchingGoal=FourthMatchingGoal, FifthMatchingGoal=FifthMatchingGoal, GoalForm=GoalForm, PrefForm=PrefForm)


bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))