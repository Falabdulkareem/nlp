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
from umbc2 import sss
import xlrd



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
    
    with open ("Pref/Hundred.txt", "r") as Pref_File1:
        Hundred_Pref=Pref_File1.read().replace('\n', ' ')
    
    with open ("Pref/SeventyFive.txt", "r") as Pref_File2:
        SeventyFive_Pref=Pref_File2.read().replace('\n', ' ')
    
    with open ("Pref/Fifty.txt", "r") as Pref_File3:
        Fifty_Pref=Pref_File3.read().replace('\n', ' ')
    
    with open ("Pref/TwentyFive.txt", "r") as Pref_File4:
        TwentyFive_Pref=Pref_File4.read().replace('\n', ' ')
    
    with open ("Pref/Zero.txt", "r") as Pref_File5:
        Zero_Pref=Pref_File5.read().replace('\n', ' ')
        
    
    
    """
    count = 0
    file = open('TaskFour/Transportation.txt', 'r')
    workbook = xlsxwriter.Workbook('TaskFour/TransportationResults.xlsx')
    worksheet = workbook.add_worksheet()
    
   
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
    """
    """
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

    # convert to lowercase
    q = q.lower()

    # remove period at the end of the sentence
    q = re.sub(r'\.+$', '', q)

    # remove comma
    q = q.replace(",", "")
    print q

    # used in excel
    original = q

    ContainsRegex = request.forms.get('RegexRadios')
    print "regex is " + ContainsRegex

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
                                                  '^if you can[\W]? (.*)',
                                                  #'(.*) (can|could|would|should) [a-z\s]+',
                                                  '(.*) (can|could|would|should) (be nice[a-z\s]*|be achieved[a-z\s]*|wait|be given[a-z\s]*|work|help[a-z\s]*|be finished[a-z\s]*|be completed[a-z\s]*|make us[a-z\s]*)',
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
            print len(result)
            MaxCount = result[0][1]

            print "this is max count: "
            print MaxCount

            MaxRepeated = []
            for number in result:
                if number[1] == MaxCount:
                    MaxRepeated.append(number)

            print "max repeated"
            print MaxRepeated

            PrefLoc = 1
            PrefValue = []
            for row in MaxRepeated:
               PrefValue.append(row[0])
            print PrefValue

            # for excel sheet
            MaxExcel = result[0][0]
            print MaxExcel

            MaxExcel1 = None
            MaxExcel2 = None

            if len(result) - 1 == 1:
                if MaxCount == result[1][1]:
                    MaxExcel1 = result[1][0]
            if len(result) - 1 == 2:
                if MaxCount == result[2][1]:
                    MaxExcel2 = result[2][0]
            # end for excel 


        # if Preference is not in DB
        except:
            print "enter the except"
            Pref100 = sss(Preference,Hundred_Pref)
            Pref75 = sss(Preference,SeventyFive_Pref)
            Pref50 = sss(Preference,Fifty_Pref)
            Pref25 = sss(Preference,TwentyFive_Pref)
            Pref0 = sss(Preference,Zero_Pref)

            print Pref100
            print Pref75
            print Pref50
            print Pref25
            print Pref0

            Value = max(Pref100, Pref75, Pref50, Pref25,Pref0)

            if Value == Pref100:
                PrefValue = "100%"
            elif Value == Pref75:
                PrefValue = "75%"
            elif Value == Pref50:
                PrefValue = "50%"
            elif Value == Pref25:
                PrefValue = "25%"
            elif Value == Pref0:
                PrefValue = "0%"

            PrefLoc = 2
            print "this is pref value"
            print PrefValue
            #PrefValue = None
            MaxExcel = "Pref from SS"
            #MaxExcel1 = None
            #MaxExcel2 = None

        # disconnect from server
        db.close()

     
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

    """    
    elif ContainsRegex == '2':
        Goal = q
        GoalForm = None
        Preference = "No preference option was chosen" 
        PrefForm = "No preference option was chosen"
    """    
    # Get the Domain and if the sentence contains regex or not
    DomainType = request.forms.get('optionsRadios')
    ContainsRegex = request.forms.get('RegexRadios')
    print DomainType
    print "regex is " + ContainsRegex

    # Get the highest matching goals for the entered sentence 
    GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
    FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = ChooseDomain(q, DomainType, 0,0,0,0,0,0)

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
    else:
        worksheet.write(row, col + 2, "Could not be parsed")
        worksheet.write(row, col + 6, MatchingGoal)

    count = count + 1
    """      

    # if the sentence didn't contains preference, and was not checked for negation
    if GoalForm is None:
        GoalForm = Find_Negation(q)

    #workbook.close()

    return template("request", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MatchingGoal=MatchingGoal, SecondMatchingGoal= SecondMatchingGoal, 
        ThirdMatchingGoal= ThirdMatchingGoal, FourthMatchingGoal=FourthMatchingGoal, FifthMatchingGoal=FifthMatchingGoal, GoalForm=GoalForm, PrefForm=PrefForm, PrefValue=PrefValue, PrefLoc=PrefLoc)


bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))