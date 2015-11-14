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
from GetPrefValue import GetValue
from Negation import Find_Negation
import re
import xlsxwriter
import MySQLdb
import sys


bottle.debug(True)

@bottle.route("/")
def tryquestion():
    return template("index")
    #return template("ChooseUser")

"""
@bottle.post("/CollectData")
def ChooseUser():
    
    UserType = request.forms.get('UserRadios')
    print "User Type is " + UserType
    
    if UserType == '1':
        return template("index")
    else:
        return template("CollectData")
    


@bottle.post("/index")
def collectUserInfo():
    
    UserInfo()
    
    return template("index")
"""    
    
    
@bottle.post("/request_1")
def answerq():
    # For Semantic Analysis Purposes
    # Plus finding the semantic similarity between goals within goal model
    """
    #read file
    file = open('GoalAnalysis/Transportation.txt', 'r')
    f = open("GoalAnalysis/TransportationResults_1.txt", "w")
    DomainType = request.forms.get('optionsRadios')
    count = 1
    
    FirstMatch = 0
    SecondMatch = 0
    ThirdMatch = 0
    FourthMatch = 0
    FifthMatch = 0 
    NoMatch = 0
    
    count = 0
    GoalsInFile = []
    
    # Initialize 21 elements in the list
    for i in range(0, 82):
        GoalsInFile.append([])
    
    for line in file:
        print line
        q = line
            
            
        # set the first goal     
        GoalsInFile[count].append(q[:-1])
        count = count + 1
        print "this is Goals in File:"
        print GoalsInFile
        # To run it I need to add (GoalsSimilarityAnalysis) + (GoalsInFile, count) in the rest of the system
        GoalsSimilarity, GoalsSimilarityAnalysis, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
        PostP, MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
        FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = ChooseDomain(q, DomainType, GoalsInFile, count, FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch)
        for i in range(0, 82 - count):      
            f.write(str(GoalsSimilarityAnalysis[i]) + "\n")
        
        f.write("\n\n")
    """
    """
        # Find the top 5 matching
        f.write(str(count) + "- " + "The highest matching goals for: " + line + "\n" + MatchingGoal + "\n" + SecondMatchingGoal + 
        "\n" + ThirdMatchingGoal + "\n" + FourthMatchingGoal + "\n" + FifthMatchingGoal + "\n\n")
        
        count = count + 1
    
    f.write("The count of the having the right goal the first option: " + str(FirstMatch) + "\n" + "The count of the having the right goal the second option: " + str(SecondMatch) + "\n" + 
    "The count of the having the right goal the third option: " + str(ThirdMatch) + "\n" + "The count of the having the right goal the fourth option: " + str(FourthMatch) + "\n" + 
    "The count of the having the right goal the fifth option: " + str(FifthMatch) + "\n" + "The count of not having the right goal in the first five options: " + str(NoMatch) + "\n" )
    
    file.close()
    f.close()
    """
    # to run the system if there is no prference specified (Already Added PrefLoc in GetPrefValue)
    PrefValue = None
    #PrefLoc = None
    PostP = None      
    
    # To do analysis for each Domain and output the result on Excel (Task3,4,5)
    """
    count = 0
    file = open('Task5Pref/Fold2/WouldBeNiceEntry.txt', 'r')
    #workbook = xlsxwriter.Workbook('TaskFive/Fold2/TransportationResults.xlsx')
    #worksheet = workbook.add_worksheet()
    """
    """
    for line in file:
        print line
        q = line
        
        q = q.rstrip()
    """
    
    # read excel with the goals and output excel with the count and regex rule for each goal
    """
    write_workbook = xlsxwriter.Workbook('Task1Result.xlsx')
    write_worksheet = write_workbook.add_worksheet()
    workbook = xlrd.open_workbook('Task1.xlsx')
    worksheet = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet.nrows - 1
    #num_cells = worksheet.ncols - 1
    curr_row = -1
    curr_cell = 1
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)
        print 'Row:', curr_row
        cell_value = worksheet.cell_value(curr_row, curr_cell)
        print cell_value
    # read data from Task 1 excel 
    workbook = xlrd.open_workbook('Testing/Testing10.xlsx')
    worksheet = workbook.sheet_by_name('Sheet1')
    # write testing data and the parsing result
    write_workbook = xlsxwriter.Workbook('Testing/Testing10Result.xlsx')
    write_worksheet = write_workbook.add_worksheet()
    # training row is from the start of the training data in excel - 2
    training_row = 58
    all_rows = worksheet.nrows - 1
    #num_cells = worksheet.ncols - 1
    curr_row = 0
    curr_cell = 1
    while curr_row < training_row:
        # the first row of the training data, which is the training data in excel - 1
        training_row1 = 59
        found = 0 
        curr_row += 1
        row = worksheet.row(curr_row)
        print 'Row:', curr_row
        cell_value = worksheet.cell_value(curr_row, curr_cell)
        Regex_Count = worksheet.cell_value(curr_row, curr_cell + 1)
        print cell_value
        print 'Count: ', Regex_Count
        print 'curr row: ', curr_row
        print 'training_row: ', training_row
        print 'all rows: ', all_rows
        # loop through the training data and find the match
        while training_row1 < all_rows:
            value = worksheet.cell_value(training_row1, curr_cell + 1)
            #print 'This is Regex count: ', Regex_Count
            #print 'this is value: ', value
            if Regex_Count == value:
                # write parse
                print "enter regex = value"
                col = 1
                write_worksheet.write(curr_row, col, cell_value)
                write_worksheet.write(curr_row, col + 1, Regex_Count)
                write_worksheet.write(curr_row, col + 2, "Parse")
                found = 1 
    """        

    #return back after finish with analysis
    q = request.forms.get('input')
    #q = cell_value

    #---- Text Normalization ----#
    # convert to lowercase
    q = q.lower()

    # remove period at the end of the sentence
    q = re.sub(r'\.+$', '', q)

    # remove comma
    q = q.replace(",", "")
    print q
    #----------------------------#
    
    # used in excel
    original = q

    ContainsRegex = request.forms.get('RegexRadios')
    print "regex is " + ContainsRegex


    ResultPage = request.forms.get('ResultRadios')

    db =  request.forms.get('dbRadios')
    print "this is db: " + str(db)

    # pattern count number for excel 
    # in k fold cross validation; i sent (write_worksheet,curr_row, No) to test_patterns function
    No = 0 

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
                                                  '^if you can[\W]?t (.*)',
                                                  #'(.*) (can|could|would|should) [a-z\s]+',
                                                  '(.*) (can|could|would|should) (be nice[a-z\s]*|be achieved[a-z\s]*|wait|be given[a-z\s]*|work|help[a-z\s]*|be finished[a-z\s]*|be completed[a-z\s]*|make us[a-z\s]*|be done[a-z\s]*)',
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
        No = 36
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

        No = 76
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
                write_worksheet.write(curr_row, col + 3, Goal)
                write_worksheet.write(curr_row, col + 4, Preference)
        training_row1 +=1
        if found == 0:
            # write no matching regex
            #print "did  enter found"
            col = 1
            write_worksheet.write(curr_row, col, cell_value)
            write_worksheet.write(curr_row, col + 1, Regex_Count)
            write_worksheet.write(curr_row, col + 2, "Could not Parse")
        """

        print "this is the preference before function: " 
        print Preference
        print "this is db: " + str(db)

        # get the value for the preference from db
        # return back after analysis
        if Preference is not None:
            print "in function page main"
            PrefValue, PrefLoc, MaxExcel, MaxExcel1, MaxExcel2  = GetValue(Preference, db)
        
        """
        # insert into db the preference according to each table (100,75,50,25,0)
        # PrefLoc to prevent output error !!
        PrefLoc = 1
        if Preference is not None:
            # Open database connection
            db = MySQLdb.connect(host="us-cdbr-iron-east-02.cleardb.net", user="b62b27ccdd4efc", passwd="da3e7042", db="heroku_8372ebe815fe21e")
            #db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="Task5")

            # prepare a cursor object using cursor() method
            cursor = db.cursor()
            try:  
                # Check if the Preference is already in DB and get the Count
                cursor.execute("Select * from wouldbenice3 where Pref = %s", [Preference])
                result = cursor.fetchone()
                count = result[2]
                count = count+1
                print "this is the count"
                print count
                cursor.execute ("UPDATE wouldbenice3 SET Count=%s WHERE Pref=%s", (count,[Preference]))
            # if Preference is not in DB, INSERT it.
            except:
                # Execute the SQL command
                cursor.execute("INSERT INTO wouldbenice3(Pref, Count) VALUES (%s,%s)", (Preference,1))
                # Commit your changes in the database
                db.commit()
            # disconnect from server
            db.close()
            # write the Preference in File
            with open("Task5Pref/Fold2/wouldbenice3.txt", "a") as Pref_file:
                Pref_file.write(Preference + "\n")
            Pref_file.close()
        """

        # if there is a separate goal and preference, send only the goal to the semantic similarity function
        # if there was no prefernce specified, send all the sentence to the semantic similarity
        if Goal is not None:
            OriginalQ = q
            q = Goal
            print "If Goal is not none print Q"
            print q 
        else:
            # The goal part specified in the interface will be the whole sentence
            Goal = q
            PrefValue = None
            PrefLoc = None


    elif ContainsRegex == '2':
        Goal = q
        GoalForm = None
        PrefLoc = 3
        PrefValue = "No preference option was chosen" 
        Preference = "No preference option was chosen" 
        PrefForm = "No preference option was chosen"


    # Get the Domain and if the sentence contains regex or not
    DomainType = request.forms.get('optionsRadios')
    ContainsRegex = request.forms.get('RegexRadios')
    print DomainType
    print "regex is " + ContainsRegex

    # Get the highest matching goals for the entered sentence 
    GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, PostP,\
    MatchingGoalP, SecondMatchingGoalP, ThirdMatchingGoalP, FourthMatchingGoalP, FifthMatchingGoalP,\
    FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = ChooseDomain(q, DomainType, 0,0,0,0,0,0)


    #Add the perference value to Post Processor 
    if PrefValue is not None:     #if there is an identified pref.
        if db == '1':
            print "enter db == 1"
            print PrefValue
            if PrefLoc == 1:
                PrefV = PrefValue[0]
                print "this is if PrefLoc = 1"
                print PrefV
            elif PrefLoc == 2:
                PrefV = PrefValue
                print "this is if PrefLoc = 2"
                print PrefV
            
            # if the sentence don't contain preference option
            if PrefLoc != 3:
                PrefV = re.sub('%', '', PrefV) 
                PrefV = int(PrefV) / float(100)
                print PrefV
                PostP = PostP + "[" + str(PrefV) + "]"
        else:
            print "enter db not equal to 1"
            if PrefLoc == 1:
                print PrefValue
                PrefV = re.sub(r'\d', '', str(PrefValue)) 
                PrefV = re.sub('_', ' ', str(PrefV))
                PrefV = re.sub('\'', '', str(PrefV))
                PostP = PostP +  str(PrefV)  
            elif PrefLoc == 2:
                #print PrefValue
                #PrefV = re.sub(r'\d', '', str(PrefValue)) 
                PostP = PostP + "[" + str(PrefValue) + "]" 

    # Write the result on excel sheet 
    """
    # Start from the first cell. Rows and columns are zero indexed.
    col = 0
    row = count
    # Iterate over the data and write it out row by row.
    #for q, Goal, Preference, PrefValue, MatchingGoal in (list):
    worksheet.write(row, col, original)
    worksheet.write(row, col + 1, Goal)
    if Preference is not None:
        worksheet.write(row, col + 2, Preference)
        worksheet.write(row, col + 3, MaxExcel)
        if PrefLoc == 1:
            if MaxExcel1 is not None and MaxExcel2 is None:
                worksheet.write(row, col + 4, MaxExcel1)
                worksheet.write(row, col + 6, MatchingGoal)
            if MaxExcel2 is not None:
                worksheet.write(row, col + 4, MaxExcel1)
                worksheet.write(row, col + 5, MaxExcel2)
                worksheet.write(row, col + 6, MatchingGoal)
            if MaxExcel1 is  None and MaxExcel2 is None:
                worksheet.write(row, col + 6, MatchingGoal)
        else:
            worksheet.write(row, col + 5, PrefValue) 
            worksheet.write(row, col + 6, MatchingGoal)
            worksheet.write(row, col + 7, PrefForm)
    else:
        worksheet.write(row, col + 2, "Could not be parsed")
        worksheet.write(row, col + 6, MatchingGoal)
    count = count + 1
    """

    # if the sentence didn't contains preference, and was not checked for negation
    if GoalForm is None:
        GoalForm = Find_Negation(q)

    #workbook.close()

    return template("request_1", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MatchingGoal=MatchingGoal, SecondMatchingGoal= SecondMatchingGoal, 
        ThirdMatchingGoal= ThirdMatchingGoal, FourthMatchingGoal=FourthMatchingGoal, FifthMatchingGoal=FifthMatchingGoal, PostP=PostP, \
        MatchingGoalP =MatchingGoalP, SecondMatchingGoalP=SecondMatchingGoalP, ThirdMatchingGoalP=ThirdMatchingGoalP, FourthMatchingGoalP=FourthMatchingGoalP, FifthMatchingGoalP=FifthMatchingGoalP,
        GoalForm=GoalForm, PrefForm=PrefForm, PrefValue=PrefValue, PrefLoc=PrefLoc)
        
        
    

bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
