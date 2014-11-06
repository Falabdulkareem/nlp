# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$14-Oct-2014 12:43:21 PM$"

from umbc2 import sss

def ChooseDomain(q, d):
    
    if d == '1':        
        Goal1 = "happy nurse"
        Goal23 = "sad nurse"
        Goal2 = "happy patient"
        Goal24 = "sad patient"
        Goal3 = "comfortable nurse"
        Goal25 = "uncomfortable nurse"
        Goal4 = "patient feels cared for"
        #Goal5 = "nurse attend to patient"
        Goal6 = "nurse notified"
        Goal7 = "system notifies the nurse through speakers"
        Goal8 = "system notifies the nurse through earphones"
        Goal9 = "nurse responded call"
        Goal10 = "nurse talked with patient"
        #Goal11 = "Nurse doesn't Talk with Patient"
        Goal12 = "nurse visited patient"
        Goal13 = "nurse walks to patients room"
        Goal14 = "nurse skips visit"
        Goal15 = "nurse talks with patient by mobile"
        #Goal16 = "Nurse Talks with patient from Nursing Station"
        Goal17 = "nurse walks to the nurse station"
        Goal18 = "nurse talks to the patient at the nurse station"
        Goal19 = "nurse turns request off"
        Goal20 = "increase nurse productivity"
        Goal21 = "no patient disturbance"
        Goal22 = "no nurse disturbance"

        res1 = str(sss(q,Goal1))
        res23 = str(sss(q,Goal23))
        res2 = str(sss(q,Goal2))
        res24 = str(sss(q,Goal24))
        res3 = str(sss(q,Goal3))
        res25 = str(sss(q,Goal25))
        res4 = str(sss(q,Goal4))
        #res5 = str(sss(q,Goal5))
        res6 = str(sss(q,Goal6))
        res7 = str(sss(q,Goal7))
        res8 = str(sss(q,Goal8))
        res9 = str(sss(q,Goal9))
        res10 = str(sss(q,Goal10))
        #res11 = str(sss(q,Goal11))
        res12 = str(sss(q,Goal12))
        res13 = str(sss(q,Goal13))
        res14 = str(sss(q,Goal14))
        res15 = str(sss(q,Goal15))
        #res16 = str(sss(q,Goal16))
        res17 = str(sss(q,Goal17))
        res18 = str(sss(q,Goal18))
        res19 = str(sss(q,Goal19))
        res20 = str(sss(q,Goal20))
        res21 = str(sss(q,Goal21))
        res22 = str(sss(q,Goal22))

        GoalsSimilarity = [Goal1 + " is: " + res1, 
            Goal23 + " is: " + res23, 
            Goal2 +  " is: " + res2,
            Goal24 + " is: " + res24,
            Goal3 +  " is: " + res3,
            Goal25 + " is: " + res25,
            Goal4 +  " is: " + res4,
            #Goal5 +  " is: " + res5,
            Goal6 +  " is: " + res6,
            Goal7 +  " is: " + res7,
            Goal8 +  " is: " + res8,
            Goal9 +  " is: " + res9,
            Goal10 + " is: " + res10,
            Goal12 + " is: " + res12,
            Goal13 + " is: " + res13,
            Goal14 + " is: " + res14,
            Goal15 + " is: " + res15,
            Goal17 + " is: " + res17,
            Goal18 + " is: " + res18,
            Goal19 + " is: " + res19,
            Goal20 + " is: " + res20,
            Goal21 + " is: " + res21,
            Goal22 + " is: " + res22,
        ]

        MaxScore = max(res1, res2, res3, res4, res6, res7, res8, res9, res10, res12, res13, res14,  \
        res15, res17, res18, res19, res20, res21, res22 ,res23, res24, res25)

        return GoalsSimilarity, MaxScore
    
    else:
        Goal1 = "qoute given"
        Goal2 = "customer requests quote"
        Goal3 = "provide quote"
        Goal4 = "customer places order"
        Goal5 = "books available"
        Goal6 = "books ordered"
        Goal7 = "contact supplier"
        Goal8 = "supplier provides price"
        Goal9 = "place order to supplier"
        Goal10 = "books acquired"
        Goal11 = "supplier ships books"
        Goal12 = "book arrive at wearhouse"
        Goal13 = "books delivered"
        Goal14 = "books deliver to courier"
        Goal15 = "handle receipt"
        Goal16 = "place receipt in shipment"
        Goal17 = "courier delivers to customer"
        Goal18 = "payment received"
        Goal19 = "payment via credit card"
        Goal20 = "get credit card card number"
        Goal21 = "get credit card authorization"
        Goal22 = "charge credit card"
        Goal23 = "payment via money order"
        Goal24 = "customer issues money order"
        Goal25 = "customer sends money order"
        Goal26 = "receive money order"
        Goal27 = "receipt sent"
        Goal28 = "send printed receipt"
        Goal29 = "print receipt"
        Goal30 = "separate receipt sent"
        Goal31 = "submit receipt"
        Goal32 = "deliver receipt"
        Goal33 = "send electronic receipt"
        Goal34 = "happy customer"
        Goal35 = "expedite process"
        Goal36 = "reduce customer side cost"
        Goal37 = "customer convenience"
        Goal38 = "supplier provides price before provide qoute"
        Goal39 = "establish transaction security"
        Goal40 = "payment traceability"
        Goal41 = "no electronic fraud"
        Goal42 = "use robust legal documentation"
        Goal43 = "charge credit card before deliver to courier"
        Goal44 = "deliver to courier after get credit card authorization"
        Goal45 = "reduce transaction costs"
        Goal46 = "send printed receipt after payment via credit card"
        Goal47 = "sad customer"
        Goal48 = "customer inconvenient"

        res1 = str(sss(q,Goal1))
        res2 = str(sss(q,Goal2))
        res3 = str(sss(q,Goal3))    
        res4 = str(sss(q,Goal4))
        res5 = str(sss(q,Goal5))
        res6 = str(sss(q,Goal6))
        res7 = str(sss(q,Goal7))
        res8 = str(sss(q,Goal8))
        res9 = str(sss(q,Goal9))
        res10 = str(sss(q,Goal10))
        res11 = str(sss(q,Goal11))
        res12 = str(sss(q,Goal12))
        res13 = str(sss(q,Goal13))
        res14 = str(sss(q,Goal14))
        res15 = str(sss(q,Goal15))
        res16 = str(sss(q,Goal16))
        res17 = str(sss(q,Goal17))
        res18 = str(sss(q,Goal18))
        res19 = str(sss(q,Goal19))
        res20 = str(sss(q,Goal20))
        res21 = str(sss(q,Goal21))
        res22 = str(sss(q,Goal22))
        res23 = str(sss(q,Goal23))
        res24 = str(sss(q,Goal24))
        res25 = str(sss(q,Goal25))
        res26 = str(sss(q,Goal26))
        res27 = str(sss(q,Goal27))
        res28 = str(sss(q,Goal28))
        res29 = str(sss(q,Goal29))
        res30 = str(sss(q,Goal30))
        res31 = str(sss(q,Goal31))
        res32 = str(sss(q,Goal32))
        res33 = str(sss(q,Goal33))
        res34 = str(sss(q,Goal34))
        res35 = str(sss(q,Goal35))
        res36 = str(sss(q,Goal36))
        res37 = str(sss(q,Goal37))
        res38 = str(sss(q,Goal38))
        res39 = str(sss(q,Goal39))
        res40 = str(sss(q,Goal40))
        res41 = str(sss(q,Goal41))
        res42 = str(sss(q,Goal42))
        res43 = str(sss(q,Goal43))
        res44 = str(sss(q,Goal44))
        res45 = str(sss(q,Goal45))
        res46 = str(sss(q,Goal46))
        res47 = str(sss(q,Goal47))
        res48 = str(sss(q,Goal48))
            
        GoalsSimilarity = [Goal1 + " is: " + res1, 
            Goal2 +  " is: " + res2,
            Goal3 +  " is: " + res3,
            Goal4 +  " is: " + res4,
            Goal5 +  " is: " + res5,
            Goal6 +  " is: " + res6,
            Goal7 +  " is: " + res7,
            Goal8 +  " is: " + res8,
            Goal9 +  " is: " + res9,
            Goal10 + " is: " + res10,
            Goal11 + " is: " + res11,
            Goal12 + " is: " + res12,
            Goal13 + " is: " + res13,
            Goal14 + " is: " + res14,
            Goal15 + " is: " + res15,
            Goal16 + " is: " + res16,
            Goal17 + " is: " + res17,
            Goal18 + " is: " + res18,
            Goal19 + " is: " + res19,
            Goal20 + " is: " + res20,
            Goal21 + " is: " + res21,
            Goal22 + " is: " + res22,
            Goal23 + " is: " + res23, 
            Goal24 + " is: " + res24,
            Goal25 + " is: " + res25,
            Goal26 + " is: " + res26,
            Goal27 + " is: " + res27,
            Goal28 + " is: " + res28,
            Goal29 + " is: " + res29,
            Goal30 + " is: " + res30,
            Goal31 + " is: " + res31,
            Goal32 + " is: " + res32,
            Goal33 + " is: " + res33, 
            Goal34 + " is: " + res34,
            Goal35 + " is: " + res35,
            Goal36 + " is: " + res36,
            Goal37 + " is: " + res37,
            Goal38 + " is: " + res38,
            Goal39 + " is: " + res39,
            Goal40 + " is: " + res40,
            Goal41 + " is: " + res41,
            Goal42 + " is: " + res42,
            Goal43 + " is: " + res43, 
            Goal44 + " is: " + res44,
            Goal45 + " is: " + res45,
            Goal46 + " is: " + res46,
            Goal47 + " is: " + res47,
            Goal48 + " is: " + res48,
        ]
        
        MaxScore = max(res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res11, res12, res13, res14,  \
        res15, res16, res17, res18, res19, res20, res21, res22 ,res23, res24, res25, res26, res27, res28, res29, \
        res30, res31, res32 ,res33, res34, res35, res36, res37, res38, res39, res40, res41, res42, res43, res44, \
        res45, res46, res47, res48)

        return GoalsSimilarity, MaxScore