# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$14-Oct-2014 12:43:21 PM$"

from umbc2 import sss
from LargestValue import second_largest, third_largest

def ChooseDomain(q, d):
    
    # Nurse domain
    if d == '1':        
        Goals = ["happy nurse",
        "sad nurse",
        "happy patient",
        "sad patient",
        "comfortable nurse",
        "uncomfortable nurse",
        "patient feels cared for",
        "nurse notified",
        "system notifies the nurse through speakers",
        "system notifies the nurse through earphones",
        "nurse responded call",
        "nurse talked with patient",
        "nurse visited patient",
        "nurse walks to patients room",
        "nurse skips visit",
        "nurse talks with patient by mobile",
        "nurse walks to the nurse station",
        "nurse talks to the patient at the nurse station",
        "nurse turns request off",
        "increase nurse productivity",
        "avoid patient disturbance",
        "avoid nurse disturbance"
        ]
        
        #Goal16 = "Nurse Talks with patient from Nursing Station
        #Goal11 = "Nurse doesn't Talk with Patient"
        #Goal5 = "nurse attend to patient"

        # The similarity score for each goal in Goals[]
        res = []
        for i in range(0, 22):
            res.append(str(sss(q,Goals[i])))
    
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 22):
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
            
        return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal
    
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
        
         # The similarity score for each goal in Goals[]
        res = []
        for i in range(0, 32):
            res.append(str(sss(q,Goals[i])))
    
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 32):
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
        
        return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal
    
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
        
        return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal
        
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
        
         # The similarity score for each goal in Goals[]
        res = []
        for i in range(0, 82):
            res.append(str(sss(q,Goals[i])))
    
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 82):
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
        
        return GoalsSimilarity, MatchingGoal, SecondMatchingGoal, ThirdMatchingGoal