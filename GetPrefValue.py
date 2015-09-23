# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$17-Sep-2015 06:17:45 PM$"

import re
import MySQLdb
from umbc2 import sss
import math



def GetValue(Preference , db_selected):
    
    Flag = False
    
    if db_selected == '1':
        print "Original db"
        # Open database connection locally
        #db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="mysql")
        
        # Open database connection on Heroku
        db = MySQLdb.connect(host="us-cdbr-iron-east-02.cleardb.net", user="b62b27ccdd4efc", passwd="da3e7042", db="heroku_8372ebe815fe21e")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Check the value of the Preference and get the MAX Count
        # Table for original system (100%, 75%, 50%, 25%, 0%) - return back

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

            
            
    elif db_selected == '4':
        
        print "Task 4 db"
        # Preferences in Table (Task4)
        # Open database connection
        db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="Task4")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()


        cursor.execute("select * from (select %s as TableName, count, pref from Critical where pref = %s \
                            union all \
                            select %s as TableName, count, pref from High_Importance where pref = %s \
                            union all \
                            select %s as TableName, count, pref from Medium_Importance where pref = %s \
                            union all \
                            select %s as TableName, count, pref from Low_Importance where pref = %s \
                            union all \
                            select %s as TableName, count, pref from No_Importance where pref = %s \
                            ) as result order by count desc", ('Critical',[Preference],'High_Importance',[Preference],'Medium_Importance',[Preference],'Low_Importance',[Preference],'No_Importance',[Preference]))
        
    # Preferences for Task 5
    elif db_selected == '5':
        
        # Preferences in Table (Task4)
        # Open database connection
        
        print "Task5 db"
        
        db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="Task5")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Preferences in Table (Task5)
        cursor.execute("select * from (select %s as TableName, count, pref from Absolutely where pref = %s \
                            union all \
                            select %s as TableName, count, pref from Important where pref = %s \
                            union all \
                            select %s as TableName, count, pref from WouldBeNice  where pref = %s \
                            union all \
                            select %s as TableName, count, pref from Unnecessary where pref = %s \
                            ) as result order by count desc", ('Absolutely',[Preference],'Important',[Preference],'WouldBeNice',[Preference],'Unnecessary',[Preference]))


        
    try:
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

        print "enter GetPrefValue Page !!"

        # disconnect from server
        db.close()
        
        MaxExcel = None

        return PrefValue, PrefLoc, MaxExcel
    
    except:
        # The preference is not in db
        if db_selected == '1':
            print "enter the except"
            
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

            # Assign the preference Values, regardless of the Form positive of negative
            if Value == 0 or math.isinf(Value) :
                PrefValue = "UNKNOWN VALUE"
            elif Value == Pref100:
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
            MaxExcel = "Pref from SS"

            return PrefValue, PrefLoc, MaxExcel
        
        elif db_selected == '4':
            print "enter the except"

            Pref1_Inf = 0     # count the the number of times the SSS returns infinty value
            Pref2_Inf = 0
            Pref_1 = open('Task4Pref/Critical.txt', 'r')
            Pref_2 = open('Task4Pref/HighImportance.txt', 'r')
            Pref_3 = open('Task4Pref/MediumImportance.txt', 'r')
            Pref_4 = open('Task4Pref/LowImportance.txt', 'r')
            Pref_5 = open('Task4Pref/NoImportance.txt', 'r')

        elif db_selected == '5':
            print "enter the except"
            
            Pref1_Inf = 0     
            Pref2_Inf = 0 
            Pref_1 = open('Task5Pref/Absolutely.txt', 'r')
            Pref_2 = open('Task5Pref/Important.txt', 'r')
            Pref_3 = open('Task5Pref/WouldBeNice.txt', 'r')
            Pref_4 = open('Task5Pref/Unnecessary.txt', 'r')
            
            
        if db_selected == '4' or db_selected == '5':
            if db_selected == '4':
                a = 41
                b = 38
                c = 32
                d = 23
                e = 25
                
                # Calculate the preferences within (No Importance) becasue Task 5 has only 4  preferences
                No_Val = 0 
                for line5 in Pref_5:
                    if not math.isinf(sss(Preference,line5)):
                        No_Val = No_Val + sss(Preference,line5)
                    else:
                        print line5 + "Not a valid result"

                No_Val = No_Val /e
                print "avg No_Val is: " + str(No_Val)
            
            else:
                a = 36
                b = 35
                c = 33
                d = 34
                
            
            # Start calculating the value for each preference set
            Critical_Val = 0 
            for line1 in Pref_1:
                # check if the output of sss is not infinity
                if not math.isinf(sss(Preference,line1)):
                    Critical_Val = Critical_Val + sss(Preference,line1)
                else:
                    print line1 + "Not a valid result"
                    Pref1_Inf = Pref1_Inf + 1

            if Pref1_Inf == a:
                Critical_Val = 0
            else:
                Critical_Val = Critical_Val /(a-Pref1_Inf)
                print "avg Critical_Val is: " + str(Critical_Val)

            #-----
            High_Val = 0 
            for line2 in Pref_2:
                if not math.isinf(sss(Preference,line2)):
                    High_Val = High_Val + sss(Preference,line2)
                else:
                    print line2 + "Not a valid result"
            
            if Pref2_Inf == b:
                High_Val = 0
            else:
                High_Val = High_Val / (b-Pref2_Inf)
                print "avg High_Val is: " + str(High_Val)

            #-----
            Medium_Val = 0 
            for line3 in Pref_3:
                #print line3
                if not math.isinf(sss(Preference,line3)):
                    Medium_Val = Medium_Val + sss(Preference,line3)
                #    print "Medium_Val is: " + str(Medium_Val)
                else:
                    print line3 + "Not a valid result"

            Medium_Val = Medium_Val /c
            print "avg Medium_Val is: " + str(Medium_Val)

            #-----
            Low_Val = 0 
            for line4 in Pref_4:
                #print line4
                if not math.isinf(sss(Preference,line4)):
                    Low_Val = Low_Val + sss(Preference,line4)
                #    print "Low_Val is: " + str(Low_Val)
                else:
                    print line4 + "Not a valid result"

            Low_Val = Low_Val /d
            print "avg Low_Val is: " + str(Low_Val)

            
            # Choose the Max value and assign the prefernce statement
            if db_selected == '4':
                Value = max(Critical_Val, High_Val, Medium_Val, Low_Val, No_Val)

                # Assign the preference Values
                if Value == 0:
                    PrefValue = "UNKNOWN VALUE"
                elif Value == Critical_Val:
                    PrefValue = "Critical"
                elif Value == High_Val:
                    PrefValue = "High Importance"
                elif Value == Medium_Val:
                    PrefValue = "Medium Importance"
                elif Value == Low_Val:
                    PrefValue = "Low Importance"
                elif Value == No_Val:
                    PrefValue = "No Importance"
            else:
                Value = max(Critical_Val, High_Val, Medium_Val, Low_Val)

                # Assign the preference Values
                if Value == 0:
                    PrefValue = "UNKNOWN VALUE"
                elif Value == Critical_Val:
                    PrefValue = "Absolutely Essential"
                elif Value == High_Val:
                    PrefValue = "Important"
                elif Value == Medium_Val:
                    PrefValue = "Would be nice"
                elif Value == Low_Val:
                    PrefValue = "Unnecessary"
                    

        PrefLoc = 2
        print "this is pref value"
        print PrefValue
        MaxExcel = "Pref from SS"
        return PrefValue, PrefLoc, MaxExcel
    
  

# This is the code in details, but the above code is working perfectly !
"""
    if Preference is not None:
        # Open database connection
        db = MySQLdb.connect(host="localhost", user="Fatima", passwd="", db="Task5")

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        try:
            # Check the value of the Preference and get the MAX Count
            # Table for original system (100%, 75%, 50%, 25%, 0%) - return back

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

            # Preferences in Table (Task4)

            cursor.execute("select * from (select %s as TableName, count, pref from Critical where pref = %s \
                                union all \
                                select %s as TableName, count, pref from High where pref = %s \
                                union all \
                                select %s as TableName, count, pref from Medium where pref = %s \
                                union all \
                                select %s as TableName, count, pref from Low where pref = %s \
                                union all \
                                select %s as TableName, count, pref from No where pref = %s \
                                ) as result order by count desc", ('Critical',[Preference],'High',[Preference],'Medium',[Preference],'Low',[Preference],'No',[Preference]))

            # Preferences in Table (Task5)

            cursor.execute("select * from (select %s as TableName, count, pref from Absolutely where pref = %s \
                                union all \
                                select %s as TableName, count, pref from Important where pref = %s \
                                union all \
                                select %s as TableName, count, pref from WouldBeNice  where pref = %s \
                                union all \
                                select %s as TableName, count, pref from Unnecessary where pref = %s \
                                ) as result order by count desc", ('Absolutely',[Preference],'Important',[Preference],'WouldBeNice',[Preference],'Unnecessary',[Preference]))

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
            # Preferences for original system - return back

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


            # Assign the preference Values, regardless of the Form positive of negative
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




            # Preferences for Task 4

            Pref_Inf = 0 
            Critical_Pref = open('Task4Pref/Critical.txt', 'r')
            High_Pref = open('Task4Pref/HighImportance.txt', 'r')
            Medium_Pref = open('Task4Pref/MediumImportance.txt', 'r')
            Low_Pref = open('Task4Pref/LowImportance.txt', 'r')
            No_Pref = open('Task4Pref/NoImportance.txt', 'r')

            Critical_Val = 0 
            for line1 in Critical_Pref:
                #print line1
                # check if the output of sss is not infinity
                if not math.isinf(sss(Preference,line1)):
                    Critical_Val = Critical_Val + sss(Preference,line1)
                #    print "Critical_Val is: " + str(Critical_Val)
                else:
                    print line1 + "Not a valid result"
                    Pref_Inf = Pref_Inf + 1

            if Pref_Inf == 41:
                Critical_Val = 0
            else:
                Critical_Val = Critical_Val /(41-Pref_Inf)
                print "avg Critical_Val is: " + str(Critical_Val)

            #-----
            High_Val = 0 
            for line2 in High_Pref:
                #print line2
                if not math.isinf(sss(Preference,line2)):
                    High_Val = High_Val + sss(Preference,line2)
                #    print "High_Val is: " + str(High_Val)
                else:
                    print line2 + "Not a valid result"

            High_Val = High_Val /38
            print "avg High_Val is: " + str(High_Val)

            #-----
            Medium_Val = 0 
            for line3 in Medium_Pref:
                #print line3
                if not math.isinf(sss(Preference,line3)):
                    Medium_Val = Medium_Val + sss(Preference,line3)
                #    print "Medium_Val is: " + str(Medium_Val)
                else:
                    print line3 + "Not a valid result"

            Medium_Val = Medium_Val /32
            print "avg Medium_Val is: " + str(Medium_Val)

            #-----
            Low_Val = 0 
            for line4 in Low_Pref:
                #print line4
                if not math.isinf(sss(Preference,line4)):
                    Low_Val = Low_Val + sss(Preference,line4)
                #    print "Low_Val is: " + str(Low_Val)
                else:
                    print line4 + "Not a valid result"

            Low_Val = Low_Val /23
            print "avg Low_Val is: " + str(Low_Val)

            #-----
            No_Val = 0 
            for line5 in No_Pref:
                #print line5
                if not math.isinf(sss(Preference,line5)):
                    No_Val = No_Val + sss(Preference,line5)
                #    print "No_Val is: " + str(No_Val)
                else:
                    print line5 + "Not a valid result"

            No_Val = No_Val /25
            print "avg No_Val is: " + str(No_Val)


            Value = max(Critical_Val, High_Val, Medium_Val, Low_Val, No_Val)

            # Assign the preference Values
            if Value == 0:
                PrefValue = "NO PREFERENCE"
            elif Value == Critical_Val:
                PrefValue = "Critical"
            elif Value == High_Val:
                PrefValue = "High Importance"
            elif Value == Medium_Val:
                PrefValue = "Medium Importance"
            elif Value == Low_Val:
                PrefValue = "Low Importance"
            elif Value == No_Val:
                PrefValue = "No Importance"


            # Preferences for Task 5

            Pref1_Inf = 0     # count the the number of times the SSS returns infinty value
            Pref2_Inf = 0 
            Absolutely_Pref = open('Task5Pref/Absolutely.txt', 'r')
            Important_Pref = open('Task5Pref/Important.txt', 'r')
            WouldBeNice_Pref = open('Task5Pref/WouldBeNice.txt', 'r')
            Unnecessary_Pref = open('Task5Pref/Unnecessary.txt', 'r')

            Critical_Val = 0 
            for line1 in Absolutely_Pref:
                #print line1
                # check if the output of sss is not infinity
                if not math.isinf(sss(Preference,line1)):
                    Critical_Val = Critical_Val + sss(Preference,line1)
                #    print "Critical_Val is: " + str(Critical_Val)
                else:
                    print line1 + "Not a valid result"
                    Pref1_Inf = Pref1_Inf + 1

            if Pref1_Inf == 36:
                Critical_Val = 0
            else:
                Critical_Val = Critical_Val /(36-Pref1_Inf)
                print "avg Critical_Val is: " + str(Critical_Val)

            #-----
            High_Val = 0 
            for line2 in Important_Pref:
                #print line2
                if not math.isinf(sss(Preference,line2)):
                    High_Val = High_Val + sss(Preference,line2)
                #    print "High_Val is: " + str(High_Val)
                else:
                    print line2 + "Not a valid result"
                    Pref2_Inf = Pref2_Inf + 1

            if Pref2_Inf == 35:
                High_Val = 0
            else:
                High_Val = High_Val /(35-Pref2_Inf)
                print "avg High_Val is: " + str(High_Val)

            #-----
            Medium_Val = 0 
            for line3 in WouldBeNice_Pref:
                #print line3
                if not math.isinf(sss(Preference,line3)):
                    Medium_Val = Medium_Val + sss(Preference,line3)
                #    print "Medium_Val is: " + str(Medium_Val)
                else:
                    print line3 + "Not a valid result"

            Medium_Val = Medium_Val /33
            print "avg Medium_Val is: " + str(Medium_Val)

            #-----
            Low_Val = 0 
            for line4 in Unnecessary_Pref:
                #print line4
                if not math.isinf(sss(Preference,line4)):
                    Low_Val = Low_Val + sss(Preference,line4)
                #    print "Low_Val is: " + str(Low_Val)
                else:
                    print line4 + "Not a valid result"

            Low_Val = Low_Val /34
            print "avg Low_Val is: " + str(Low_Val)


            Value = max(Critical_Val, High_Val, Medium_Val, Low_Val)

            # Assign the preference Values
            if Value == 0:
                PrefValue = "NO PREFERENCE"
            elif Value == Critical_Val:
                PrefValue = "Absolutely Essential"
            elif Value == High_Val:
                PrefValue = "Important"
            elif Value == Medium_Val:
                PrefValue = "Would be nice"
            elif Value == Low_Val:
                PrefValue = "Unnecessary"


            # if the Prference is in Negative Form, change the category of the Pref.
            # Add the below in comment -------------

            if PrefForm == "Negative":
                if Value == Pref100:
                    PrefValue = "0%"
                elif Value == Pref75:
                    PrefValue = "25%"
                elif Value == Pref50:
                    PrefValue = "50%"
                elif Value == Pref25:
                    PrefValue = "25%"
                elif Value == Pref0:
                    PrefValue = "0%"
            elif PrefForm == "Positive":       
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
            # Tell here -----------------------


            PrefLoc = 2
            print "this is pref value"
            print PrefValue
            #PrefValue = None
            MaxExcel = "Pref from SS"
            #MaxExcel1 = None
            #MaxExcel2 = None


        # disconnect from server
        db.close()
"""