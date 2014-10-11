# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import sys
import time
import random
import datetime 
import bottle
from bottle import route, run, template, request
import os
import nltk
import quepy
from SPARQLWrapper import SPARQLWrapper, JSON
from umbc2 import sss
#from NLTK import ie_preprocess
import string
from Pattern import test_patterns

bottle.debug(True)

@bottle.route("/")
def tryquestion():
    return template("index")
    
@bottle.post("/request")
def answerq():
    q = request.forms.get('input')
    
    # Add its, it's
    Preference, Goal, GoalForm, PrefForm = test_patterns(q, 1,
                                            [ r'(.*) if (.*)', 
                                              r'is of (.*?) to us (.*)',
                                              r'is of (.*?) to me (.*)',
                                              r'is of (.*?) for us (.*)',
                                              r'is of (.*?) for me (.*)',
                                              r'is of (.*?) to (.*)',
                                              r'is of (.*) that (.*)',
                                              r'is (.*?) to me (.*)',
                                              r'is (.*?) to us (.*)',
                                              r'is (.*?) to (.*)',
                                              r'is (.*?) for me (.*)',
                                              r'is (.*?) for us (.*)',
                                              r'is (.*?) for (.*)',
                                              r'is (.*?) that (.*)',
                                             ])
                                             
    if Preference is None:
        Preference, Goal, GoalForm, PrefForm = test_patterns(q, 2,
                                            [ r'(.*) is of (.*)',
                                              r'the importance of (.*) is (.*)', 
                                              r'(.*) is (.*)',  
                                             ])
    
    if Goal is not None:
        q = Goal
        print q
    else:
        Goal = q
         
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
    
    """
    yield u"<p>The similarity score between " + q + u"<a> and </a>"u"</p>"
    yield u"<p> " + Goal1 + u"<a> is: "u"</a>" + res1 + u"</p>"
    yield u"<p> " + Goal23 + u"<a> is: "u"</a>" + res23 + u"</p>"
    yield u"<p> " + Goal2 + u"<a> is: "u"</a>" + res2 + u"</p>"
    yield u"<p> " + Goal24 + u"<a> is: "u"</a>" + res24 + u"</p>"
    yield u"<p> " + Goal3 + u"<a> is: "u"</a>" + res3 + u"</p>"
    yield u"<p> " + Goal25 + u"<a> is: "u"</a>" + res25 + u"</p>"
    yield u"<p> " + Goal4 + u"<a> is: "u"</a>" + res4 + u"</p>"
    yield u"<p> " + Goal5 + u"<a> is: "u"</a>" + res5 + u"</p>"
    yield u"<p> " + Goal6 + u"<a> is: "u"</a>" + res6 + u"</p>"
    yield u"<p> " + Goal7 + u"<a> is: "u"</a>" + res7 + u"</p>"
    yield u"<p> " + Goal8 + u"<a> is: "u"</a>" + res8 + u"</p>"
    yield u"<p> " + Goal9 + u"<a> is: "u"</a>" + res9 + u"</p>"
    yield u"<p> " + Goal10 + u"<a> is: "u"</a>" + res10 + u"</p>"
    #yield u"<p> " + Goal11 + u"<a> is: "u"</a>" + res11 + u"</p>"
    yield u"<p> " + Goal12 + u"<a> is: "u"</a>" + res12 + u"</p>"
    yield u"<p> " + Goal13 + u"<a> is: "u"</a>" + res13 + u"</p>"
    yield u"<p> " + Goal14 + u"<a> is: "u"</a>" + res14 + u"</p>"
    yield u"<p> " + Goal15 + u"<a> is: "u"</a>" + res15 + u"</p>"
    #yield u"<p> " + Goal16 + u"<a> is: "u"</a>" + res16 + u"</p>"
    yield u"<p> " + Goal17 + u"<a> is: "u"</a>" + res17 + u"</p>"
    yield u"<p> " + Goal18 + u"<a> is: "u"</a>" + res18 + u"</p>"
    yield u"<p> " + Goal19 + u"<a> is: "u"</a>" + res19 + u"</p>"
    yield u"<p> " + Goal20 + u"<a> is: "u"</a>" + res20 + u"</p>"
    yield u"<p> " + Goal21 + u"<a> is: "u"</a>" + res21 + u"</p>"
    yield u"<p> " + Goal22 + u"<a> is: "u"</a>" + res22 + u"</p>"
       """
       
    MaxScore = max(res1, res2, res3, res4, res6, res7, res8, res9, res10, res12, res13, res14,  \
    res15, res17, res18, res19, res20, res21, res22 ,res23, res24, res25)
    #yield "The hgihest score is: " + MaxScore
    
    if GoalForm is None:
        # Get a bag of words without punctuation
        words = [word.strip(string.punctuation) for word in q.split()]
        print words

        # Create a list and add the words to the list
        my_list = [] 
        for current_word in words:
            my_list.append(current_word.lower())

        # Create a list with negative words
        NegativeWords = ["not", "haven't", "havent", "hasn't", "hasnt", "didn't", "didnt", "doesn't",\
        "doesnt", "don't", "dont", "shouldn't", "shouldnt", "couldn't", "couldnt", "can't", "cant", "cannot", \
        "no" , "nobody"]

        # Check if the sentence written have any negative words
        FoundNeg = set(NegativeWords).intersection(my_list)
        print FoundNeg

        if FoundNeg:
            GoalForm = "The sentence is in negative form"
        else:
            GoalForm = "The sentence is in positive form"
    
    
    return template("request", GoalsSimilarity=GoalsSimilarity, Preference=Preference, Goal=Goal, MaxScore=MaxScore, GoalForm=GoalForm, PrefForm=PrefForm)


bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))