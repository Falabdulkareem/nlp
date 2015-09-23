# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$6-Jan-2014 01:46:45 PM$"


"""
OLD CODE

Goals = ["have meeting scheduled",
        "constraints gathered",
        "constraints gathered automatically",
        "constraints gathered by request based",
        "book the meeting",
        "find suitable slot",
        "find suitable room",
        "have meeting announced",
        "send email",
        "send attendance reminder",
        "participants attend meeting",
        "request constraints by calling everybody",
        "request constraints by email",
        "send invitation",
        "response received",
        "wait one day for responses to arrive",
        "wait three days for responses to arrive",
        "wait one week for responses to arrive", 
        "receive responses",
        "reduce labor",
        "maximize attendance",
        "quick scheduling",
        "avoid annoying the participants"
        ]  
        
         # The similarity score for each goal in Goals[]
        res = []
        for i in range(0, 23):
            res.append(str(sss(q,Goals[i])))
    
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 23):
            GoalsSimilarity.append(Goals[i] + ": " + res[i])
        

        # The most matching goal and it's index
        MaxScore = max(res)
        MaxIndex = res.index(MaxScore)
        MatchingGoal = Goals[MaxIndex].capitalize() + ": " + MaxScore + ""
             
         # Get the second and third highest scores and it's index
        SecondScore = second_largest(res)
        if SecondScore is not None:
            SecondIndex = res.index(SecondScore)
            SecondMatchingGoal = Goals[SecondIndex].capitalize() + ": " + SecondScore + ""
        else:
            SecondMatchingGoal = "None"
            
        
        ThirdScore = third_largest(res)
        if ThirdScore is not None:
            ThirdIndex = res.index(ThirdScore)
            ThirdMatchingGoal = Goals[ThirdIndex].capitalize() + ": " + ThirdScore + ""
        else:
            ThirdMatchingGoal = "None"
        
        
        # get the first, second, third matching result in the report automatically
        g = "request constraints by email"
        
        if Goals[MaxIndex] == g:
            FirstMatch = FirstMatch + 1
        elif Goals[SecondIndex] == g:
            SecondMatch = SecondMatch + 1
        elif Goals[ThirdIndex] == g:
            ThirdMatch = ThirdMatch + 1
        else:
            NoMatch = NoMatch + 1
            
        return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FirstMatch, SecondMatch, ThirdMatch, NoMatch
        
"""

"MAIN"
"""
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
import MySQLdb
from Negation import Find_Negation
import re
import xlsxwriter



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
    
    file = open('TaskThree/CarManufacturer/100.txt', 'r')
    for line in file:
        print line
        q = line
    
    # return back after finish with analysis
    #q = request.forms.get('input')
    
    # used in excel
    original = q
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
        
 
        # get the value for the preference from db
        if Preference is not None:
            # Open database connection
            db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="mysql")
            
            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            
            try:
                # Check the value of the Preference and get the MAX Count
                cursor.execute("select * from (select %s as TableName, count, pref from Hundred_Percent where pref = %s \
                                    union all \
                                    select %s as TableName, count, pref from SeventyFive_Percent where pref = %s \
                                    union all \
                                    select %s as TableName, count, pref from Fifty_Percent where pref = %s \
                                    union all \
                                    select %s as TableName, count, pref from TwentyFive_Percent where pref = %s \
                                    union all \
                                    select %s as TableName, count, pref from Zero_Percent where pref = %s \
                                    ) as result order by count desc", ('100%',[Preference],'75%',[Preference],'50%',[Preference],'25%',[Preference],'0%',[Preference]))

                #result = cursor.fetchone()
                
                # if the MAX count was in more than one table
                result = cursor.fetchall()
                print result
                MaxCount = result[0][1]
                
                # for excel sheet
                MaxExcel = result[0][0]
                print MaxExcel

                MaxExcel1 = None
                MaxExcel2 = None

                if MaxCount == result[1][1]:
                    MaxExcel1 = result[1][0]
                    if MaxCount == result [2][1]:
                        MaxExcel2 = result[2][0]
                # end for excel 
                
                print "this is max count: "
                print MaxCount
                
                MaxRepeated = []
                for number in result:
                    if number[1] == MaxCount:
                        MaxRepeated.append(number)
                 
                print "max repeated"
                print MaxRepeated

                PrefValue = []
                for row in MaxRepeated:
                   PrefValue.append(row[0])
                print PrefValue
                
            # if Preference is not in DB
            except:
                PrefValue = None
                MaxExcel = "Pref is unknown"
                MaxExcel1 = None
                MaxExcel2 = None
            
            # disconnect from server
            db.close()
            
        
        """ 
        # insert into db the preference according to each table (100,75,50,25,0)
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
            PrefValue = None
        
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
    
    
    if Goal is not None:
        workbook = xlsxwriter.Workbook('PrefValue.xlsx')
        worksheet = workbook.add_worksheet()
        
        #list = ([q], [Goal], [Preference], [PrefValue], [MatchingGoal])
        
        # Start from the first cell. Rows and columns are zero indexed.
        row = 0
        col = 0

        # Iterate over the data and write it out row by row.
        #for q, Goal, Preference, PrefValue, MatchingGoal in (list):
        worksheet.write(row, col,     original)
        worksheet.write(row, col + 1, Goal)
        if Preference is not None:
            worksheet.write(row, col + 2, Preference)
            worksheet.write(row, col + 3, MaxExcel)
            if MaxExcel1 is not None and MaxExcel2 is None:
                worksheet.write(row, col + 4, MaxExcel1)
                worksheet.write(row, col + 5, MatchingGoal)
            if MaxExcel2 is not None:
                worksheet.write(row, col + 5, MaxExcel2)
                worksheet.write(row, col + 6, MatchingGoal)
            if MaxExcel1 is  None and MaxExcel2 is None:
                worksheet.write(row, col + 4, MatchingGoal)
        else:
            worksheet.write(row, col + 2, "Could not be parsed")

                
        #    row += 1
        
        workbook.close()
    
    # if the sentence didn't contains preference, and was not checked for negation
    if GoalForm is None:
        GoalForm = Find_Negation(q)
    
    return template("request", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MatchingGoal=MatchingGoal, SecondMatchingGoal= SecondMatchingGoal, 
        ThirdMatchingGoal= ThirdMatchingGoal, FourthMatchingGoal=FourthMatchingGoal, FifthMatchingGoal=FifthMatchingGoal, GoalForm=GoalForm, PrefForm=PrefForm, PrefValue=PrefValue)


bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
"""