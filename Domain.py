# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$14-Oct-2014 12:43:21 PM$"

from umbc2 import sss
from Negation import Find_Negation
from DomainNegation import NegationInDomain


def ChooseDomain(q, d, FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch):
    PostP = None
    MatchingGoalNeg = None
    SecondMatchingGoalNeg = None
    ThirdMatchingGoalNeg = None
    FourthMatchingGoalNeg = None
    FifthMatchingGoalNeg = None
    
    # Nurse domain
    if d == '1':     
        Goals = ["happy nurse",
        "happy patient",
        "comfortable nurse",
        "patient feels cared for",     
        "nurse notified",
        "system notifies the nurse through speakers",
        "system notifies the nurse through earphones",
        "nurse responded to the call",
        "nurse talked with patient",
        "nurse visited patient",
        "nurse walks to patients room",
        "nurse skips visit",
        "nurse talks with patient by mobile",
        "nurse walks to the nursing station",
        "nurse talks to the patient at the nurse station",
        "nurse turns request off",
        "increase nurse productivity",
        "avoid patient disturbance",     
        "avoid nurse disturbance",      
        "nurse attend to patient",
        "communication handled"
        ]
        
        GoalsWithNeg = ["happy nurse",
        "sad nurse", ###
        "happy patient",
        "sad patient", ###
        "comfortable nurse",
        "uncomfortable nurse",  ###
        "patient feels cared for",     
        "nurse notified",
        "system notifies the nurse through speakers",
        "system notifies the nurse through earphones",
        "nurse responded to the call",
        "nurse talked with patient",
        "nurse visited patient",
        "nurse walks to patients room",
        "nurse skips visit",
        "nurse talks with patient by mobile",
        "nurse walks to the nursing station",
        "nurse talks to the patient at the nurse station",
        "nurse turns request off",
        "increase nurse productivity",
        "decrease nurse productivity", ###
        "avoid patient disturbance",
        "patient disturbance", ###
        "avoid nurse disturbance",
        "nurse disturbance", ###
        "nurse attend to patient",
        "communication handled"
        ]
        
        GoalsNegation = [
        ("happy nurse", "sad nurse"),
        ("happy patient", "sad patient"),
        ("comfortable nurse", "uncomfortable nurse"),
        ("increase nurse productivity", "decrease nurse productivity"),
        ("avoid patient disturbance", "patient disturbance"),
        ("avoid nurse disturbance", "nurse disturbance")
        ]
            
        """
        #Goal16 = "Nurse Talks with patient from Nursing Station
        #Goal11 = "Nurse doesn't Talk with Patient"
       
        # Goals were 21 without the negation of the adj.
    
        # Create a list to contains all the Goals and the Score for each goal
        GoalScoreList = []
        GoalScoreListNeg = []
        
        
        # Initialize 21 elements in the list
        for i in range(0, 21):
            GoalScoreList.append([])
        
        for i in range(0, 27):
            GoalScoreListNeg.append([])
    
        # Set the Goals and Scores 
        for i in range(0, 21):
            GoalScoreList[i].append(Goals[i])
            GoalScoreList[i].append(str(sss(q,Goals[i])))
            
        for i in range(0, 27):
            GoalScoreListNeg[i].append(GoalsWithNeg[i])
            GoalScoreListNeg[i].append(str(sss(q,GoalsWithNeg[i])))
            
        # Sort the list in descending order  
        SortedScoreList = sorted(GoalScoreList, key=lambda Score: Score[1], reverse=True)
        SortedScoreListNeg = sorted(GoalScoreListNeg, key=lambda Score: Score[1], reverse=True)
        
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 21):
            GoalsSimilarity.append(SortedScoreList[i][0] + ": " + str(SortedScoreList[i][1]))
            
        GoalsSimilarityNeg = []
        for i in range(0, 27):
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
        
        g = "patient feels cared for"    
        
        if GoalForm == "Positive":
            print "enter positive" 
            for i in range(0,6):     
                if FirstNeg[0] == GoalsNegation[i][0]:
                    PostP = GoalsNegation[i][0] + " ["+MaxScoreNeg+"]"
                    MatchingGoal = GoalsNegation[i][0] + " ["+MaxScoreNeg+"]"
                    Flag1p = True
                elif FirstNeg[0] == GoalsNegation[i][1]:
                    FirstConvert = GoalsNegation[i][0]
                    PostP = "Negative (" + FirstConvert + ")["+MaxScoreNeg+"]"
                    MatchingGoal = "Negative (" + FirstConvert + ")["+MaxScoreNeg+"]"
                    if FirstConvert == g:
                        FirstMatch = FirstMatch + 1
                    Flag1p = True
            
            if not Flag1p:
                for i in range(0,6):      
                    if SecondNeg[0] == GoalsNegation[i][0]:
                       PostP = GoalsNegation[i][0] + " ["+SecondScoreNeg+"]"
                       SecondMatchingGoal = GoalsNegation[i][0] + " ["+SecondScoreNeg+"]"
                       Flag2p = True
                    elif SecondNeg[0] == GoalsNegation[i][1]:
                        SecondConvert = GoalsNegation[i][0]
                        PostP = "Negative (" + SecondConvert + ")["+SecondScoreNeg+"]"
                        SecondMatchingGoal = "Negative (" + SecondConvert + ")["+SecondScoreNeg+"]"
                        if SecondConvert == g:
                            SecondMatch = SecondMatch + 1
                        Flag2p = True
                        
            if not Flag1p and not Flag2p:
                for i in range(0,6):  
                    if ThirdNeg[0] == GoalsNegation[i][0]:
                       PostP = GoalsNegation[i][0] + " ["+ThirdScoreNeg+"]"
                       ThirdMatchingGoal = GoalsNegation[i][0] + " ["+ThirdScoreNeg+"]"
                       Flag3p = True
                    elif ThirdNeg[0] == GoalsNegation[i][1]:
                        ThirdConvert = GoalsNegation[i][0]
                        PostP = "Negative (" + ThirdConvert + ")["+ThirdScoreNeg+"]"
                        ThirdMatchingGoal = "Negative (" + ThirdConvert + ")["+ThirdScoreNeg+"]"
                        if ThirdConvert == g:
                            ThirdMatch = ThirdMatch + 1
                        Flag3p = True
            
            if not Flag1p and not Flag2p and not Flag3p:
                for i in range(0,6):      
                    if FourthNeg[0] == GoalsNegation[i][0]:
                       PostP = GoalsNegation[i][0] + " ["+FourthScoreNeg+"]" 
                       FourthMatchingGoal = GoalsNegation[i][0] + " ["+FourthScoreNeg+"]" 
                       Flag4p = True
                    elif FourthNeg[0] == GoalsNegation[i][1]:
                        FourthConvert = GoalsNegation[i][0]
                        PostP = "Negative (" + FourthConvert + ")["+FourthScoreNeg+"]"
                        FourthMatchingGoal = "Negative (" + FourthConvert + ")["+FourthScoreNeg+"]"
                        if FourthConvert == g:
                            FourthMatch = FourthMatch + 1
                        Flag4p = True
            
            if not Flag1p and not Flag2p and not Flag3p and not Flag4p:
                for i in range(0,6):  
                    if FifthNeg[0] == GoalsNegation[i][0]:
                       PostP = GoalsNegation[i][0] + " ["+FifthScoreNeg+"]"
                       FifthMatchingGoal = GoalsNegation[i][0] + " ["+FifthScoreNeg+"]"
                       Flag5p = True
                    elif FifthNeg[0] == GoalsNegation[i][1]:
                        FifthConvert = GoalsNegation[i][0]
                        PostP = "Negative (" + FifthConvert + ")["+FifthScoreNeg+"]"
                        FifthMatchingGoal = "Negative (" + FifthConvert + ")["+FifthScoreNeg+"]"
                        if FifthConvert == g:
                            FifthMatch = FifthMatch + 1
                        Flag5p = True
            
            
        elif GoalForm == "Negative":
 
            print "enter negative"
            for i in range(0,6):
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
                for i in range(0,6):    
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
                for i in range(0,6):          
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
                for i in range(0,6):          
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
                for i in range(0,6):      
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
                    
            
            
        # get the first, second, third, fourth, fifth matching result in the report automatically
       
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
        
        
        # For finding the semantic similarity for the goals within the goal model
        # Add (GoalsSimilarityAnalysis) and NegationDomain(GoalsInFile, count) below +  Add (GoalsSimilarityAnalysis)  in return
        
        GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, PostP,\
        MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
        FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = NegationInDomain(q, d, Goals, GoalsWithNeg, GoalsNegation,FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch)
        
        
        return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
            PostP, MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
            FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch
        
    
    # Car Manufacturer domain
    elif d == '2':
        Goals = ["increase customer loyalty",
        "increase return on investment",
        "increase sales volume",
        "increase Toyota sales",
        "increase VW sales",
        "increase profit per vehicle",
        "increase sales price",
        "increase foreign earnings",
        "lower production costs",
        "keep labour costs low",
        "improve economies of production",
        "reduce raw materials costs",
        "outsource units of production",
        "increase high margin sales",
        "improve car quality",
        "improve car service",
        "increase consumer appeal",
        "reduce operating costs",
        "lower environment impact",
        "lower purchase costs",
        "expand markets",
        "lower gas price",
        "improve mileage",
        "offer rebates",
        "lower loan interest rates",
        "lower sales price",
        "gas price rises",
        "US gas price rises",
        "Japanese gas price rises",
        "lower Japanese interest rates",
        "Japanese rates rise",
        "Yen rises"
        ]
        
        GoalsWithNeg = ["increase customer loyalty",
        "decrease customer loyalty", ###
        "increase return on investment",
        "decrease return on investment", ###
        "increase sales volume",
        "decrease sales volume", ###
        "increase Toyota sales",
        "decrease Toyota sales", ###
        "increase VW sales",
        "decrease VW sales", ###
        "increase profit per vehicle",
        "decrease profit per vehicle", ###
        "increase sales price",
    #    "lower sales price", ###
        "increase foreign earnings",
        "decrease foreign earnings", ###
        "lower production costs",
        "increase production costs", ###
        "keep labour costs low",
        "keep labour costs high", ###
        "improve economies of production",
        "decrease economies of production", ###
        "reduce raw materials costs",
        "increase raw materials costs", ###
        "outsource units of production",
        "increase high margin sales",
        "decrease high margin sales", ###
        "improve car quality",
        "decrease car quality", ###
        "improve car service",
        "decrease car service", ###
        "increase consumer appeal",
        "decrease consumer appeal", ###
        "reduce operating costs",
        "increase operating costs", ###
        "lower environment impact",
        "increase environment impact", ###
        "lower purchase costs",
        "increase purchase costs", ###
        "expand markets",
        "lower gas price",
    #    "increase gas price", ###
        "improve mileage",
        "lower mileage", ###
        "offer rebates",
        "lower loan interest rates",
        "increase loan interest rates", ###
        "lower sales price",
    #    "increase sales price", ###
        "gas price rises",
    #    "gas price declines", ###
        "US gas price rises",
        "US gas price declines", ###
        "Japanese gas price rises",
        "Japanese gas price declines", ###
        "lower Japanese interest rates",
        "increase Japanese interest rates", ###
        "Japanese rates rise",
        "Japanese rates decline", ###
        "Yen rises",
        "Yen declines" ###
        ]  
        
        GoalsNegation = [
        ("increase customer loyalty", "decrease customer loyalty"),
        ("increase return on investment", "decrease return on investment"),
        ("increase sales volume", "decrease sales volume"),
        ("increase Toyota sales", "decrease Toyota sales"),
        ("increase VW sales", "decrease VW sales"),
        ("increase profit per vehicle", "decrease profit per vehicle"),
    #    ("increase sales price","decrease sales price"),
        ("increase foreign earnings","decrease foreign earnings"),
        ("lower production costs","increase production costs"),
        ("keep labour costs low","keep labour costs high"),
        ("improve economies of production","decrease economies of production"),
        ("reduce raw materials costs","increase raw materials costs"),
        ("increase high margin sales","decrease high margin sales"),
        ("improve car quality","decrease car quality"),
        ("improve car service","decrease car service"),
        ("increase consumer appeal","decrease consumer appeal"),
        ("reduce operating costs","increase operating costs"),
        ("lower environment impact","increase environment impact"),
        ("lower purchase costs","increase purchase costs"),
        ("lower gas price","increase gas price"),
        ("improve mileage","lower mileage"),
        ("lower loan interest rates","increase loan interest rates"),
        ("lower sales price","increase sales price"),
    #    ("gas price rises","gas price declines"),
        ("US gas price rises","US gas price declines"),
        ("Japanese gas price rises","Japanese gas price declines"),
        ("lower Japanese interest rates","increase Japanese interest rates"),
        ("Japanese rates rise", "Japanese rates decline"),
        ("Yen rises", "Yen declines")
        ]
        
        # For finding the semantic similarity for the goals within the goal model
        # Add (GoalsSimilarityAnalysis) and NegationDomain(GoalsInFile, count) below +  Add (GoalsSimilarityAnalysis)  in return
        
        GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, PostP,\
        MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
        FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = NegationInDomain(q, d, Goals, GoalsWithNeg, GoalsNegation,FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch)
        
    
        
        """
        # Create a list to contains all the Goals and the Score for each goal
        GoalScoreList = []
        
        # Initialize 32 elements in the list
        for i in range(0, 32):
            GoalScoreList.append([])
    
        # Set the Goals and Scores 
        for i in range(0, 32):
            GoalScoreList[i].append(Goals[i])
            GoalScoreList[i].append(str(sss(q,Goals[i])))
            
        # Sort the list in descending order  
        SortedScoreList = sorted(GoalScoreList, key=lambda Score: Score[1], reverse=True)
        
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 32):
            GoalsSimilarity.append(SortedScoreList[i][0] + ": " + str(SortedScoreList[i][1]))
        
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
        
         # get the first, second, third, fourth, fifth matching results in the report automatically
        g = "lower gas price"
        
        if First[0] == g:
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
        
        return GoalsSimilarity,  MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
            PostP, MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
            FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch
    
    # Meeting Scheduler
    elif d == '3':
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
        "quick schedule",
        "avoid annoying the participants"
        ]  
        
        GoalsWithNeg = ["have meeting scheduled",
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
        "increase labor", ###
        "maximize attendance",
        "minimize attendance", ###
        "quick schedule",
        "slow scheduling", ###
        "avoid annoying the participants",
        "annoy the participants" ###
        ]  
        
        GoalsNegation = [
        ("reduce labor", "increase labor"),
        ("maximize attendance", "minimize attendance"),
        ("quick schedule", "slow schedule"),
        ("avoid annoying the participants", "annoy the participants"),
        ]
        
        """
        # Create a list to contains all the Goals and the Score for each goal
        GoalScoreList = []
        
        # Initialize 23 elements in the list
        for i in range(0, 23):
            GoalScoreList.append([])
    
        # Set the Goals and Scores 
        for i in range(0, 23):
            GoalScoreList[i].append(Goals[i])
            GoalScoreList[i].append(str(sss(q,Goals[i])))
            
        # Sort the list in descending order  
        SortedScoreList = sorted(GoalScoreList, key=lambda Score: Score[1], reverse=True)
        
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 23):
            GoalsSimilarity.append(SortedScoreList[i][0] + ": " + str(SortedScoreList[i][1]))
        
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
        
         # get the first, second, third, fourth, fifth matching results in the report automatically
        g = "request constraints by email"
        
        if First[0] == g:
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
        
        # For finding the semantic similarity for the goals within the goal model
        # Add (GoalsSimilarityAnalysis) and NegationDomain(GoalsInFile, count) below +  Add (GoalsSimilarityAnalysis)  in return
        
        GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, PostP,\
        MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
        FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = NegationInDomain(q, d, Goals, GoalsWithNeg, GoalsNegation,FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch)
        
        
        return GoalsSimilarity , MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
            PostP, MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
            FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch
        
    # Transportation
    elif d == '4':
        Goals = ["supply public transport service",
        "manage financial budget",
        "manage service costs",
        "obtain founds",
        "manage profits",
        "cover service costs",
        "invest on the service",
        "use external founds",
        "increase profits",
        "use profits",
        "sell tickets",
        "decide sale strategy",
        "avoid fraud",
        "verify tickets",
        "provide tickets",
        "estimate sale places", 
        "add sale points on the path",
        "decide service cost",
        "estimate service costs",
        "define profits to reach",
        "evaluate alternative resources",
        "guarantee transportation",
        "transport users to destination",
        "connect points",
        "manage mobility",
        "build infrastructure",
        "use means of transport",
        "build means of transport",
        "organize public competition",
        "choose directly company",
        "maintain means of transport",
        "clean means of transport", 
        "supply means of transport",
        "repair means of transport",
        "protect means of transport",
        "serve path",
        "plan transport service",
        "timetable",
        "define path",
        "make public service available ",
        "facilitate tickets purchasing",
        "group users",
        "exchange means of transport",
        "locate stations",
        "provide parking area",
        "minimize cost per user",
        "improve transport services",
        "improve old services", 
        "provide new services",
        "satisfy users",
        "improve quality of life",
        "monitor pollution",
        "use special means of transport",
        "respect rules",
        "provide comfort",
        "provide acoustic comfort",
        "provide visual comfort",
        "provide postural comfort",
        "provide climatic comfort",
        "minimizing time",
        "favourite public traffic",
        "create reserved lanes",
        "regulate reserved lanes",
        "public services in limited zones",
        "avoid traffic",
        "optimize coverage",
        "use historical information",
        "use special instruments",
        "protect users",
        "guarantee drivers capabilities",
        "check drivers capabilities",
        "check drivers health",
        "check drivers attitudes",
        "guarantee the user behavior",
        "provide rules",
        "make to respect the law",
        "introduce controllers",
        "protect drivers health",
        "protect user health",
        "forbid smoking", 
        "ensure structures",
        "protect from pollution",
        ]
        
        GoalsWithNeg = ["supply public transport service",
        "manage financial budget",
        "manage service costs",
        "obtain founds",
        "manage profits",
        "cover service costs",
        "invest on the service",
        "use external founds",
        "increase profits",
        "decrease profits", ###
        "use profits",
        "sell tickets",
        "decide sale strategy",
        "avoid fraud",
        "allow fraue", ###
        "verify tickets",
        "provide tickets",
        "estimate sale places", 
        "add sale points on the path",
        "decide service cost",
        "estimate service costs",
        "define profits to reach",
        "evaluate alternative resources",
        "guarantee transportation",
        "transport users to destination",
        "connect points",
        "manage mobility",
        "build infrastructure",
        "use means of transport",
        "build means of transport",
        "organize public competition",
        "choose directly company",
        "maintain means of transport",
        "clean means of transport", 
        "supply means of transport",
        "repair means of transport",
        "protect means of transport",
        "serve path",
        "plan transport service",
        "timetable",
        "define path",
        "make public service available ",
        "facilitate tickets purchasing",
        "group users",
        "exchange means of transport",
        "locate stations",
        "provide parking area",
        "minimize cost per user",
        "maximize cost per user", ###
        "improve transport services",
        "reduce transport services", ###
        "improve old services", 
        "reduce old services", ###
        "provide new services",
        "satisfy users",
        "improve quality of life",
        "reduce quality of life", ###
        "monitor pollution",
        "use special means of transport",
        "respect rules",
        "provide comfort",
        "provide acoustic comfort",
        "provide visual comfort",
        "provide postural comfort",
        "provide climatic comfort",
        "minimizing time",
        "maximizing time", ###
        "favourite public traffic",
        "create reserved lanes",
        "regulate reserved lanes",
        "public services in limited zones",
        "avoid traffic",
        "allow traffic", ###
        "optimize coverage",
        "use historical information",
        "use special instruments",
        "protect users",
        "guarantee drivers capabilities",
        "check drivers capabilities",
        "check drivers health",
        "check drivers attitudes",
        "guarantee the user behavior",
        "provide rules",
        "make to respect the law",
        "introduce controllers",
        "protect drivers health",
        "protect user health",
        "forbid smoking", 
        "allow smoking", ###
        "ensure structures",
        "protect from pollution",
        ]  
        
        GoalsNegation = [
        ("increase profits", "decrease profits"),
        ("avoid fraud", "allow fraud"),
        ("minimize cost per user", "maximize cost per user"),
        ("improve transport services", "reduce transport services"),
        ("improve old services", "reduce old services"),
        ("improve quality of life", "reduce quality of life"),
        ("minimizing time", "maximizing time"),
        ("avoid traffic", "allow traffic"),
        ("forbid smoking", "allow smoking")
        ]
        
        """
        # Create a list to contains all the Goals and the Score for each goal
        GoalScoreList = []
        
        # Initialize 82 elements in the list
        for i in range(0, 82):
            GoalScoreList.append([])
    
        # Set the Goals and Scores 
        for i in range(0, 82):
            GoalScoreList[i].append(Goals[i])
            GoalScoreList[i].append(str(sss(q,Goals[i])))
            
        # Sort the list in descending order  
        SortedScoreList = sorted(GoalScoreList, key=lambda Score: Score[1], reverse=True)
        
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 82):
            GoalsSimilarity.append(SortedScoreList[i][0] + ": " + str(SortedScoreList[i][1]))
        
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
        
         # get the first, second, third, fourth, fifth matching results in the report automatically
        g = "repair means of transport"
        
        if First[0] == g:
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
        
        # For finding the semantic similarity for the goals within the goal model
        # Add (GoalsSimilarityAnalysis) and NegationDomain(GoalsInFile, count) below +  Add (GoalsSimilarityAnalysis)  in return
        
        
        GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, PostP,\
        MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
        FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch = NegationInDomain(q, d, Goals, GoalsWithNeg, GoalsNegation,FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch)
         
        
        return GoalsSimilarity , MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
             PostP, MatchingGoalNeg, SecondMatchingGoalNeg, ThirdMatchingGoalNeg, FourthMatchingGoalNeg, FifthMatchingGoalNeg, \
             FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch
