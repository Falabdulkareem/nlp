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
from Nurse import nursedomain
from NLTK import ie_preprocess
import string

bottle.debug(True)

# quepy.set_loglevel("DEBUG")
"""
@bottle.route("/")
def index():
    yield u"<p>Here is a <a href=\"http://bottlepy.org/\">bottle</a> app under construction. This example converts the question 'What is a blowtorch?' to a SPARQL query using <a href=\"http://quepy.machinalis.com/\">quepy</a>, queries dbpedia and returns the results (the RDF literals retrieved by rdfs:comment).</p>"
    yield u"Try your own question like this: <a href=\"http://pacific-river-6269.herokuapp.com/question/Who is Arnold Schwarzenegger?\">http://pacific-river-6269.herokuapp.com/question/Who is Arnold Schwarzenegger?</a>"
    target, query, metadata = dbpedia.get_query("what is a blowtorch?")
    yield u"<p>" + query + u"</p>"
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    for result in results["results"]["bindings"]:
        yield "<p>" + result["x1"]["value"] + "</p>"
    return
"""
#   @get("/tryqustion") # or @route('/login')
@bottle.route("/")
def tryquestion():
 return '''
    <form action="/" method="post">
        Enter you NLQ: <input name="query" type="text" size="65" />
        <input value="Search" type="submit" />
     </form>
    '''
#@post('/tryqustion') # or @route('/login', method='POST')
@bottle.route("/", method="POST")
def answerq():
    q = request.forms.get('query')
    
    Goal1 = "happy nurse"
    Goal2 = "happy patient"
    Goal3 = "nurse comfort"
    Goal4 = "patient feels cared for"
    Goal5 = "nurse attend to patient"
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
    res2 = str(sss(q,Goal2))
    res3 = str(sss(q,Goal3))
    res4 = str(sss(q,Goal4))
    res5 = str(sss(q,Goal5))
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
    
    
    #for x in range(0,1):
    #expression = sss(q,Goal1)
    
    yield u"<p>The similarity score between " + q + u"<a> and </a>"u"</p>"
    yield u"<p> " + Goal1 + u"<a> is: "u"</a>" + res1 + u"</p>"
    yield u"<p> " + Goal2 + u"<a> is: "u"</a>" + res2 + u"</p>"
    yield u"<p> " + Goal3 + u"<a> is: "u"</a>" + res3 + u"</p>"
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
       
    yield max(res1, res2, res3, res4, res5, res6, res7, res8, res9, res10, res12, res13, res14,  \
    res15, res17, res18, res18, res20, res21, res22)
    
    # Get a bag of words without punctuation
    words = [word.strip(string.punctuation) for word in q.split()]
    print words
    
    # Create a list and add the words to the list
    my_list = [] 
    for current_word in words:
        my_list.append(current_word.lower())
        
    # Create a list with negative words
    NegativeWords = ["not", "haven't", "havent", "hasn't", "hasnt", "didn't", "didnt", "doesn't",\
    "doesnt", "don't", "dont", "shouldn't", "shouldnt", "couldn't", "couldnt", "can't", "cant", "cannot"]
    
    # Check if the sentence written have any negative words
    FoundNeg = set(NegativeWords).intersection(my_list)
    print FoundNeg
    
    if FoundNeg:
        yield u"<p>The sentence is in Negative form</p>"

    
    #ie_preprocess(q) # test NLTK
    
   # text = nltk.word_tokenize(q)
   # print nltk.pos_tag(text) 
    #print expression
    
    #yield u"<p>" + str(expression) + u"</p>"
    
    """ 
    print target
    print query
    print metadata
    """    

    """
    if isinstance(metadata, tuple):
            query_type = metadata[0]
            metadata = metadata[1]
    else:
            query_type = metadata
            metadata = None
    if query is None:
        yield u"<p>Query not generated :(</p>"
   
    yield u"<p>" + query + u"</p>"
    
    if target.startswith("?"):
            target = target[1:]
    if query:
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)
            results = sparql.query().convert()

            if not results["results"]["bindings"]:
                yield u"<p>No answer found :(</p>"
  
    for result in results["results"]["bindings"]:
       yield "<p>" + result["x1"]["value"] + "</p>"
    return
    """

bottle.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))