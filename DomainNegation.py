#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$14-Oct-2014 12:43:21 PM$"

from umbc2 import sss
from Negation import Find_Negation



def NegationInDomain(q, d, Goals, GoalsWithNeg, GoalsNegation, FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch):
    PostP = None
    MatchingGoalNeg = None
    SecondMatchingGoalNeg = None
    ThirdMatchingGoalNeg = None
    FourthMatchingGoalNeg = None
    FifthMatchingGoalNeg = None
    
    if d == '1':
        a= 21           # Goals
        b= 27           # GoalsWithNeg
        c= 6            # GoalsNegation
    elif d =='2':
        a= 32
        b= 57
        c= 27
    elif d =='3':
        a= 23
        b= 27
        c= 4
    elif d =='4':
        a= 82
        b= 91
        c= 9
    elif d =='5':
        a= 24
        b= 43
        c= 19
    elif d =='6':
        a= 22
        b= 35
        c= 13
    elif d =='7':
        a= 19
        b= 23
        c= 4
        
    # Create a list to contains all the Goals and the Score for each goal
    GoalScoreList = []
    GoalScoreListNeg = []


    # Initialize 21 elements in the list
    for i in range(0, a):
        GoalScoreList.append([])

    for i in range(0, b):
        GoalScoreListNeg.append([])

    # Set the Goals and Scores 
    for i in range(0, a):
        GoalScoreList[i].append(Goals[i])
        GoalScoreList[i].append(str(sss(q,Goals[i])))
    
   
    # Finding the semantic similarity between goals within goal model
    """
    # Add new variable for matching the goals with each other in each domain (Analaysis Purpose)
    ScoreListAnalysis = sorted(GoalScoreList, key=lambda Score: Score[1])
    GoalsSimilarityAnalysis = []
    
    print "count: " + str(count)
    j = 0
        
    temp = ScoreListAnalysis
    
    print temp
    
    for j in range(0, count):
        for item in range(0, a - count):
            if temp[item][0] == GoalsInFile[j][0]:
                print "enter if condition \n"
                print temp[item][0]
                temp.pop(item)
                
    
    for i in range(0, a - count):
        GoalsSimilarityAnalysis.append(temp[i][0] + ": " + str(temp[i][1]))
    """


    for i in range(0, b):
        GoalScoreListNeg[i].append(GoalsWithNeg[i])
        GoalScoreListNeg[i].append(str(sss(q,GoalsWithNeg[i])))

    # Sort the list in descending order  
    SortedScoreList = sorted(GoalScoreList, key=lambda Score: Score[1], reverse=True)
    SortedScoreListNeg = sorted(GoalScoreListNeg, key=lambda Score: Score[1], reverse=True)

    # The goal and similarity score in one senetence
    GoalsSimilarity = []
    for i in range(0, a):
        GoalsSimilarity.append(SortedScoreList[i][0] + ": " + str(SortedScoreList[i][1]))
        print GoalsSimilarity[i]

    GoalsSimilarityNeg = []
    for i in range(0, b):
        GoalsSimilarityNeg.append(SortedScoreListNeg[i][0] + ": " + str(SortedScoreListNeg[i][1]))

    # The top 5 matching goals and their index
    First = SortedScoreList[0]
    MaxScore = First[1]
    MatchingGoal = First[0].capitalize() + ": " + str(First[1]) + ""

    Second = SortedScoreList[1]
    SecondScore = Second[1]
    SecondMatchingGoal = Second[0].capitalize() + ": " + str(Second[1]) + ""

    Third = SortedScoreList[2]
    ThirdScore = Third[1]
    ThirdMatchingGoal = Third[0].capitalize() + ": " + str(Third[1]) + ""

    Fourth = SortedScoreList[3]
    FourthScore = Fourth[1]
    FourthMatchingGoal = Fourth[0].capitalize() + ": " + str(Fourth[1]) + ""

    Fifth = SortedScoreList[4]
    FifthScore = Fifth[1]
    FifthMatchingGoal = Fifth[0].capitalize() + ": " + str(Fifth[1]) + ""

    # Similarity for Goals with Negation
    GoalForm = Find_Negation(q)

    FirstNeg = SortedScoreListNeg[0]
    MaxScoreNeg = FirstNeg[1]
    MatchingGoalNeg = FirstNeg[0].capitalize() + ": " + str(FirstNeg[1]) + ""

    SecondNeg = SortedScoreListNeg[1]
    SecondScoreNeg = SecondNeg[1]
    SecondMatchingGoalNeg = SecondNeg[0].capitalize() + ": " + str(SecondNeg[1]) + ""

    ThirdNeg = SortedScoreListNeg[2]
    ThirdScoreNeg = ThirdNeg[1]
    ThirdMatchingGoalNeg = ThirdNeg[0].capitalize() + ": " + str(ThirdNeg[1]) + ""

    FourthNeg = SortedScoreListNeg[3]
    FourthScoreNeg = FourthNeg[1]
    FourthMatchingGoalNeg = FourthNeg[0].capitalize() + ": " + str(FourthNeg[1]) + ""

    FifthNeg = SortedScoreListNeg[4]
    FifthScoreNeg = FifthNeg[1]
    FifthMatchingGoalNeg = FifthNeg[0].capitalize() + ": " + str(FifthNeg[1]) + ""

    Flag1 = False
    Flag2 = False
    Flag3 = False
    Flag4 = False
    Flag5 = False

    Flag1p = False
    Flag2p = False
    Flag3p = False
    Flag4p = False
    Flag5p = False

    FirstConvert = None
    SecondConvert = None
    ThirdConvert = None
    FourthConvert = None
    FifthConvert = None

    
    
    g = "improve transport services"    

    if GoalForm == "Positive":
        print "enter positive" 
        for i in range(0,c):   
            # if the goal component is a shadow goal
            if FirstNeg[0] == GoalsNegation[i][1] and Flag1p == False:
                FirstConvert = GoalsNegation[i][0]
                PostP = " (¬" + FirstConvert + ")"
            #    MatchingGoal = "Negative (" + FirstConvert + ")["+MaxScoreNeg+"]"
                print "post p2: " + PostP
                print "matching goal2: " + MatchingGoal
                if FirstConvert == g:
                    FirstMatch = FirstMatch + 1
                Flag1p = True
        # if the goal component is original goal
        if Flag1p == False:
            PostP = "(" + FirstNeg[0] + ")" 
            print "post p: " + PostP
            print "matching goal: " + MatchingGoalNeg
            
    elif GoalForm == "Negative":

        print "enter negative"
        for i in range(0,c):
            # if the goal component is a shadow goal
            print "this is first neg:  " + FirstNeg[0]
            print "goals negation: " + GoalsNegation[i][1]
            if FirstNeg[0] == GoalsNegation[i][1] and Flag1 == False:
                print "first if"
                FirstConvert = GoalsNegation[i][0]
                PostP = "(¬" + FirstNeg[0] + ") = " + FirstConvert
            #    MatchingGoal = "Negative (" + FirstNeg[0] + ") = " + FirstConvert + " ["+MaxScoreNeg+"]"
            #    print "Matching goal 2: " + MatchingGoal
                if FirstConvert == g:
                    FirstMatch = FirstMatch + 1
                Flag1 = True
                print "flag 2"
                print Flag1
        
            # if the goal component is original goal
            #elif FirstNeg[0] == GoalsNegation[i][0]:
        if Flag1 == False:
            print "second if"
            FirstConvert = GoalsNegation[i][1]
            PostP = "(¬" + FirstNeg[0] + ")"
        #    MatchingGoal = "Negative (" + FirstNeg[0] + ")["+MaxScoreNeg+"]"
        #    print "matching goal: " + MatchingGoal
            Flag1 = True
            print "flag 1"
            print Flag1
            
    
    return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
        PostP, MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
        FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch
                
            
        
    """
    if GoalForm == "Positive":
        print "enter positive" 
        for i in range(0,c):   
            # if the goal component is the origianl goal
        #    print "first negation 0: " + FirstNeg[0]
        #    print Goals[i]
            if FirstNeg[0] ==  GoalsNegation[i][0]:
                PostP = "(" + GoalsNegation[i][0] + ")" + " ["+MaxScoreNeg+"]"
            #    MatchingGoal = Goals[i] + " ["+MaxScoreNeg+"]"
                Flag1p = True
                print "post p: " + PostP
                print "matching goal: " + MatchingGoal
            # if the goal component is the shadow goal
            elif FirstNeg[0] == GoalsNegation[i][1] and Flag1p == False:
                FirstConvert = GoalsNegation[i][0]
                PostP = "Negative (" + FirstConvert + ")["+MaxScoreNeg+"]"
            #    MatchingGoal = "Negative (" + FirstConvert + ")["+MaxScoreNeg+"]"
                print "post p2: " + PostP
                print "matching goal2: " + MatchingGoal
                if FirstConvert == g:
                    FirstMatch = FirstMatch + 1
                Flag1p = True
            
            

        if not Flag1p:
            for i in range(0,c): 
                # if the goal component is the origianl goal
                if SecondNeg[0] == GoalsNegation[i][0]:
                   PostP = "(" + GoalsNegation[i][0] + ")" + " ["+SecondScoreNeg+"]" 
                #   SecondMatchingGoal = GoalsNegation[i][0] + " ["+SecondScoreNeg+"]"
                   Flag2p = True
                # if the goal component is the shadow goal
                elif SecondNeg[0] == GoalsNegation[i][1] and Flag2p == False:
                    SecondConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + SecondConvert + ")["+SecondScoreNeg+"]"
                #    SecondMatchingGoal = "Negative (" + SecondConvert + ")["+SecondScoreNeg+"]"
                    if SecondConvert == g:
                        SecondMatch = SecondMatch + 1
                    Flag2p = True

        if not Flag1p and not Flag2p:
            for i in range(0,c):  
                if ThirdNeg[0] == GoalsNegation[i][0]:
                   PostP = GoalsNegation[i][0] + " ["+ThirdScoreNeg+"]"
            #       PostP = GoalsNegation[i][0]
                   ThirdMatchingGoal = GoalsNegation[i][0] + " ["+ThirdScoreNeg+"]"
                   Flag3p = True
                elif ThirdNeg[0] == GoalsNegation[i][1] and Flag3p == False:
                    ThirdConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + ThirdConvert + ")["+ThirdScoreNeg+"]"
            #        PostP = "Negative (" + ThirdConvert + ")"
                    ThirdMatchingGoal = "Negative (" + ThirdConvert + ")["+ThirdScoreNeg+"]"
                    if ThirdConvert == g:
                        ThirdMatch = ThirdMatch + 1
                    Flag3p = True

        if not Flag1p and not Flag2p and not Flag3p:
            for i in range(0,c):      
                if FourthNeg[0] == GoalsNegation[i][0]:
                   PostP = GoalsNegation[i][0] + " ["+FourthScoreNeg+"]" 
            #       PostP = GoalsNegation[i][0]
                   FourthMatchingGoal = GoalsNegation[i][0] + " ["+FourthScoreNeg+"]" 
                   Flag4p = True
                elif FourthNeg[0] == GoalsNegation[i][1] and Flag4p == False:
                    FourthConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + FourthConvert + ")["+FourthScoreNeg+"]"
            #        PostP = "Negative (" + FourthConvert + ")"
                    FourthMatchingGoal = "Negative (" + FourthConvert + ")["+FourthScoreNeg+"]"
                    if FourthConvert == g:
                        FourthMatch = FourthMatch + 1
                    Flag4p = True

        if not Flag1p and not Flag2p and not Flag3p and not Flag4p:
            for i in range(0,c):  
                if FifthNeg[0] == GoalsNegation[i][0]:
                   PostP = GoalsNegation[i][0] + " ["+FifthScoreNeg+"]"
            #       PostP = GoalsNegation[i][0] 
                   FifthMatchingGoal = GoalsNegation[i][0] + " ["+FifthScoreNeg+"]"
                   Flag5p = True
                elif FifthNeg[0] == GoalsNegation[i][1]:
                    FifthConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + FifthConvert + ")["+FifthScoreNeg+"]"
            #        PostP = "Negative (" + FifthConvert + ")"
                    FifthMatchingGoal = "Negative (" + FifthConvert + ")["+FifthScoreNeg+"]"
                    if FifthConvert == g:
                        FifthMatch = FifthMatch + 1
                    Flag5p = True


    elif GoalForm == "Negative":

        print "enter negative"
        for i in range(0,c):
            if FirstNeg[0] == GoalsNegation[i][0]:
                FirstConvert = GoalsNegation[i][1]
                PostP = "Negative (" + FirstNeg[0] + ")["+MaxScoreNeg+"]"
                MatchingGoal = "Negative (" + FirstNeg[0] + ")["+MaxScoreNeg+"]"
                Flag1 = True
                print "flag 1"
                print Flag1
            elif FirstNeg[0] == GoalsNegation[i][1]:
                FirstConvert = GoalsNegation[i][0]
                PostP = "Negative (" + FirstNeg[0] + ") = " + FirstConvert + " ["+MaxScoreNeg+"]"
                MatchingGoal = "Negative (" + FirstNeg[0] + ") = " + FirstConvert + " ["+MaxScoreNeg+"]"
                if FirstConvert == g:
                    FirstMatch = FirstMatch + 1
                Flag1 = True
                print "flag 2"
                print Flag1

        if not Flag1:
            for i in range(0,c):    
                if SecondNeg[0] == GoalsNegation[i][0]:
                    print "flag 3"
                    print Flag1
                    SecondConvert = GoalsNegation[i][1]
                    PostP = "Negative (" + SecondNeg[0] + ")["+SecondScoreNeg+"]"
                    SecondMatchingGoal = "Negative (" + SecondNeg[0] + ")["+SecondScoreNeg+"]"
                    Flag2 = True
                elif SecondNeg[0] == GoalsNegation[i][1]:
                    SecondConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + SecondNeg[0] + ") = " + SecondConvert + " ["+SecondScoreNeg+"]"
                    SecondMatchingGoal = "Negative (" + SecondNeg[0] + ") = " + SecondConvert + " ["+SecondScoreNeg+"]"
                    if SecondConvert == g:
                        SecondMatch = SecondMatch + 1
                    Flag2 = True

        if not Flag1 and not Flag2:
            for i in range(0,c):          
                if ThirdNeg[0] == GoalsNegation[i][0]:
                    ThirdConvert = GoalsNegation[i][1]
                    PostP = "Negative (" + ThirdNeg[0] + ")["+ThirdScoreNeg+"]"
                    ThirdMatchingGoal = "Negative (" + ThirdNeg[0] + ")["+ThirdScoreNeg+"]"
                    Flag3 = True
                elif ThirdNeg[0] == GoalsNegation[i][1]:
                    ThirdConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + ThirdNeg[0] + ") = " + ThirdConvert + " ["+ThirdScoreNeg+"]"
                    ThirdMatchingGoal = "Negative (" + ThirdNeg[0] + ") = " + ThirdConvert + " ["+ThirdScoreNeg+"]"
                    if ThirdConvert == g:
                        ThirdMatch = ThirdMatch + 1
                    Flag3 = True

        if not Flag1 and not Flag2 and not Flag3:
            for i in range(0,c):          
                if FourthNeg[0] == GoalsNegation[i][0]:
                    FourthConvert = GoalsNegation[i][1]
                    PostP = "Negative (" + FourthNeg[0] + ")["+FourthScoreNeg+"]"
                    FourthMatchingGoal = "Negative (" + FourthNeg[0] + ")["+FourthScoreNeg+"]"
                    Flag4 = True
                elif FourthNeg[0] == GoalsNegation[i][1]:
                    FourthConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + FourthNeg[0] + ") = " + FourthConvert + " ["+FourthScoreNeg+"]"
                    FourthMatchingGoal = "Negative (" + FourthNeg[0] + ") = " + FourthConvert + " ["+FourthScoreNeg+"]"
                    if FourthConvert == g:
                        FourthMatch = FourthMatch + 1
                    Flag4 = True

        if not Flag1 and not Flag2 and not Flag3 and not Flag4:
            for i in range(0,c):      
                if FifthNeg[0] == GoalsNegation[i][0]:
                    FifthConvert = GoalsNegation[i][1]
                    PostP = "Negative (" + FifthNeg[0] + ")["+FifthScoreNeg+"]"
                    FifthMatchingGoal = "Negative (" + FifthNeg[0] + ")["+FifthScoreNeg+"]"
                    Flag5 = True
                elif FifthNeg[0] == GoalsNegation[i][1]:
                    FifthConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + FifthNeg[0] + ") = " + FifthConvert + " ["+FifthScoreNeg+"]" 
                    FifthMatchingGoal = "Negative (" + FifthNeg[0] + ") = " + FifthConvert + " ["+FifthScoreNeg+"]"
                    if FifthConvert == g:
                        FifthMatch = FifthMatch + 1
                    Flag5 = True
    """
    

    # get the first, second, third, fourth, fifth matching result in the report automatically
    """
    print "intersection"
    if FirstConvert == g or SecondConvert == g or ThirdConvert == g or FourthConvert == g or FifthConvert == g:
        print "negation count"
    elif First[0] == g:
        FirstMatch = FirstMatch + 1
    elif Second[0] == g:
        SecondMatch = SecondMatch + 1
    elif Third[0] == g:
        ThirdMatch = ThirdMatch + 1
    elif Fourth[0] == g:
        FourthMatch = FourthMatch + 1
    elif Fifth[0] == g:
        FifthMatch = FifthMatch + 1
    else:
        NoMatch = NoMatch + 1
    """