# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$14-Oct-2014 12:43:21 PM$"

from umbc2 import sss

def ChooseDomain(q, d):
    
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
        "no patient disturbance",
        "no nurse disturbance"
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
        MatchingGoal = Goals[MaxIndex].capitalize() + ", with a matching score: " + MaxScore + ""
             
        return GoalsSimilarity, MatchingGoal
    
    else:
        Goals = ["qoute given",
        "customer requests quote",
        "provide quote",
        "customer places order",
        "books available",
        "books ordered",
        "contact supplier",
        "supplier provides price",
        "place order to supplier",
        "books acquired",
        "supplier ships books",
        "book arrive at wearhouse",
        "books delivered",
        "books deliver to courier",
        "handle receipt",
        "place receipt in shipment",
        "courier delivers to customer",
        "payment received",
        "payment via credit card",
        "get credit card card number",
        "get credit card authorization",
        "charge credit card",
        "payment via money order",
        "customer issues money order",
        "customer sends money order",
        "receive money order",
        "receipt sent",
        "send printed receipt",
        "print receipt",
        "separate receipt sent",
        "submit receipt",
        "deliver receipt",
        "send electronic receipt",
        "happy customer",
        "expedite process",
        "reduce customer side cost",
        "customer convenience",
        "supplier provides price before provide qoute",
        "establish transaction security",
        "payment traceability",
        "no electronic fraud",
        "use robust legal documentation",
        "charge credit card before deliver to courier",
        "deliver to courier after get credit card authorization",
        "reduce transaction costs",
        "send printed receipt after payment via credit card",
        "sad customer",
        "customer inconvenient",
        ]
        
         # The similarity score for each goal in Goals[]
        res = []
        for i in range(0, 48):
            res.append(str(sss(q,Goals[i])))
    
        # The goal and similarity score in one senetence
        GoalsSimilarity = []
        for i in range(0, 48):
            GoalsSimilarity.append(Goals[i] + ": " + res[i])
        
        # The most matching goal and it's index
        MaxScore = max(res)
        MaxIndex = res.index(MaxScore)
        MatchingGoal = Goals[MaxIndex].capitalize() + ", with a matching score: " + MaxScore + ""
             
        return GoalsSimilarity, MatchingGoal
        