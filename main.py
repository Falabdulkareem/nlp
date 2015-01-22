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
import re



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
    
    # remove period at the end of the sentence
    q = re.sub(r'\.+$', '', q)
    
    # remove comma
    q = q.replace(",", "")
    print q
    
    ContainsRegex = request.forms.get('RegexRadios')
    print "regex is " + ContainsRegex
    
    if ContainsRegex == '1':
        Preference, Goal, GoalForm, PrefForm = test_patterns(q, 3,
                                                [ 'upmost importance (.*)',
                                                  'you must try (.*)',
                                                  'you must (.*)',                                                
                                                  'it is most important (.*)',
                                                  'must complete (.*)',
                                                  'never ignore (.*)',
                                                  '(.*) must be [a-z\s]+',                                                  
                                                  'without achieving (.*) there is no purpose of (.*)',                                                 
                                                  '(.*) cannot be neglected',
                                                  '(.*) requires immediate attention',
                                                  'under no circumstances should you not (.*)',
                                                  'let go of anything and do (.*)',
                                                  '(.*) need to be achieve at [0-9]+ percent of the goal',
                                                  '(.*) is (.*) please [a-z\s]+',                                                  
                                                  '(.*) is important to be achieved',
                                                  'why don[\S]*t you achieve (.*)[?]*',
                                                  'start on (.*) as [a-z\s]+',
                                                  'get (.*) done',
                                                  #'(.*) should be [a-z\s]+',
                                                  #'(.*) would be [a-z\s]+',
                                                  #'(.*) need[a-z]{0,1} [^to] [a-z\s]+',
                                                  'most resource will go to (.*)',
                                                  '[a-z\s\W]+ (achieve|achieving|complete|completing) (.*) or not',
                                                  '(.*) will (improve [a-z\s]+|make [a-z\s]+|be a bonus|not help [a-z\s]+)', 
                                                  '^if you can[\W]? (.*)',
                                                  #'(.*) (can|could|would|should) [a-z\s]+',
                                                  '(.*) (can|could|would|should) (be nice[a-z\s]*|be achieved[a-z\s]*|wait|be given[a-z\s]*|work|help[a-z\s]*|be finished[a-z\s]*|be completed[a-z\s]*)',
                                                  'don[\W]t forget (.*)',
                                                  '(.*) to be completed[a-z\s]*',
                                                  'you may or may not (.*)',                                                 
                                                  '(.*) may or may not[a-z\s]*',
                                                  'if possible (.*)',
                                                  'if there[\W]?( is|s) time left (.*)',
                                                  '(.*) doesn[\W]?t have great significance',
                                                  '[a-z\s]* consider (.*)',
                                                  'not that [a-z\s]+ (to|you) (.*)',
                                                  '(.*) is not that [a-z\s]+',                                                 
                                                  '(.*) if (nothing to do|you have time|possible)',
                                                  '(.*) provides [a-z\s]+',
                                                  '(disregard|ignore entirely) (.*)',
                                                 ])
                                                 
        if Preference is None:    
            Preference, Goal, GoalForm, PrefForm = test_patterns(q, 1,
                                                    [ 'is (.*?) if (.*)',  
                                                      'it (.*?) if (.*)',                                                      
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
                                                      'is (.*?) for (.*)',
                                                      'is (.*) to us (.*)',
                                                      'is (.*?) to (.*)',
                                                      'is (.*) for me (.*)',
                                                      'is (.*) for us (.*)',
                                                      'is (.*) that (.*)',
                                                      '(.*?) that (.*)',
                                                      'is (.*?) in (.*)',
                                                      'i[\W]?( am|m) (.*?) in (.*)',
                                                      'i (.*) if you achieve (.*)',
                                                      'i (.*) achieve (.*)',                                                     
                                                      '(.*?) in (.*)',
                                                      '(.*) if (.*)',
                                                      '(.*?) is to (.*)',                                                      
                                                      'i[\W]?( am|m) (.*?) to (.*)',   
                                                      'i (.*) to (.*)',
                                                      '(.*?) on (.*)',
                                                      '(.*) from (.*)',
                                                      '(.*?) to (.*)',
                                                      '(.*?) about (.*)',
                                                      'you (.*) achieve (.*)', 
                                                      'i[\W]?( am|m) (.*?) [a-z]{0,2}[\s]*achieving (.*)',
                                                      '(.*) achieving (.*)',
                                                      '(.*) doing (.*)',
                                                      '(.*) but (.*)',
                                                      '(.*) over (.*)',
                                                      '(.*) achieve (.*)',                                                    
                                                     ])

        if Preference is None:
            Preference, Goal, GoalForm, PrefForm = test_patterns(q, 2,
                                                [ '(.*) is of (.*)',                                                 
                                                  '(.*) has the (.*)',
                                                  '(.*) has (.*)',
                                                  #'(.*) should be (achieved|done) (.*)',
                                                  '(.*) can be (.*)',
                                                  '(.*) by any means (.*)',
                                                  'the importance of (.*) is (.*)', 
                                                  '(.*) is (.*)', 
                                                  'start on (.*) and (.*)',
                                                  '(.*) does (.*)',
                                                 
                                                 ])
                                                 
        
        """                                  
        if Preference is not None:
            # Open database connection
            db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="mysql")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()

            try:
                # Check if the Preference is already in DB and get the Count
                cursor.execute("Select * from Zero_Percent where Pref = %s", [Preference])
                result = cursor.fetchone()
                count = result[2]
                count = count+1
                print "this is the count"
                print count

                cursor.execute ("UPDATE Zero_Percent SET Count=%s WHERE Pref=%s", (count,[Preference]))

            # if Preference is not in DB, INSERT it.
            except:
                # Execute the SQL command
                cursor.execute("INSERT INTO Zero_Percent(Pref, Count) VALUES (%s,%s)", (Preference,1))
                # Commit your changes in the database
                db.commit()

            # disconnect from server
            db.close()

            # write the Preference in File
            with open("Pref/Zero.txt", "a") as Pref_file:
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