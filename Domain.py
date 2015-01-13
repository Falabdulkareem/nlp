# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$14-Oct-2014 12:43:21 PM$"

from umbc2 import sss

def ChooseDomain(q, d, FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch):
    
    # Nurse domain
    if d == '1':     
        Goals = ["happy nurse",
        #"sad nurse",
        "happy patient",
        #"sad patient",
        "comfortable nurse",
        #"uncomfortable nurse",
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
           
        """
        Goals1 = [
        ("happy nurse", sss(q,"happy nurse")),
        #"sad nurse",
        ("happy patient", sss(q,"happy patient")),
        #"sad patient",
        ("comfortable nurse", sss(q,"comfortable nurse")),
        #"uncomfortable nurse",
        ("patient feels cared for", sss(q,"patient feels cared for")),
        ("nurse notified", sss(q,"nurse notified")),
        ("system notifies the nurse through speakers", sss(q,"system notifies the nurse through speakers")),
        ("system notifies the nurse through earphones", sss(q,"system notifies the nurse through earphones")),
        ("nurse responded to the call", sss(q,"nurse responded to the call")),
        ("nurse talked with patient", sss(q,"nurse talked with patient")),
        ("nurse visited patient", sss(q,"nurse visited patient")),
        ("nurse walks to patients room", sss(q,"nurse walks to patients room")),
        ("nurse skips visit", sss(q,"nurse skips visit")),
        ("nurse talks with patient by mobile", sss(q,"nurse talks with patient by mobile")),
        ("nurse walks to the nursing station", sss(q,"nurse walks to the nursing station")),
        ("nurse talks to the patient at the nurse station", sss(q,"nurse talks to the patient at the nurse station")),
        ("nurse turns request off", sss(q,"nurse turns request off")),
        ("increase nurse productivity", sss(q,"increase nurse productivity")),
        ("avoid patient disturbance", sss(q,"avoid patient disturbance")),
        ("avoid nurse disturbance", sss(q,"avoid nurse disturbance")),
        ("nurse attend to patient", sss(q,"nurse attend to patient")),
        ("communication handled", sss(q,"communication handled"))
        ]
        """
        
        #Goal16 = "Nurse Talks with patient from Nursing Station
        #Goal11 = "Nurse doesn't Talk with Patient"
       
        # Create a list to contains all the Goals and the Score for each goal
        GoalScoreList = []
        
        # Initialize 21 elements in the list
        for i in range(0, 21):
            GoalScoreList.append([])
    
        # Set the Goals and Scores 
        for i in range(0, 21):
            GoalScoreList[i].append(Goals[i])
            GoalScoreList[i].append(str(sss(q,Goals[i])))
            
        # Sort the list in descending order  
        SortedScoreList = sorted(GoalScoreList, key=lambda Score: Score[1], reverse=True)
        
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 21):
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
             
        # get the first, second, third, fourth, fifth matching result in the report automatically
        g = "avoid nurse disturbance"
        
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

        return GoalsSimilarity , MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
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

        return GoalsSimilarity , MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
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
        "quick scheduling",
        "avoid annoying the participants"
        ]  
        
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

        return GoalsSimilarity , MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
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
        "user special means of transport",
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

        return GoalsSimilarity , MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal, FourthMatchingGoal, FifthMatchingGoal, \
            FirstMatch, SecondMatch, ThirdMatch, FourthMatch, FifthMatch, NoMatch
