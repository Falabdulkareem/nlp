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
@bottle.route("/request")
def tryquestion():
 return '''
    <form action="/request" method="post">
        Enter you NLQ: <input name="request" type="text" size="65" />
        <input value="Search" type="submit" />
     </form>
    '''
#@post('/tryqustion') # or @route('/login', method='POST')
@bottle.route("/request", method="POST")
def answerq():
    q = request.forms.get('request')
    
    Goal1 = "Add comment is never satisfied"
    Goal2 = "View prices is not satisfied before Login is satisfied"
    
    for x in range(0,1):
    #expression = sss(q,Goal1)
        yield u"<p>The similarity score between " + q + u"<a> and "u"</a>" + Goal1 + u"<a> is: "u"</a>" + str(sss(q,Goal1)) + u"</p>"
        yield u"<p>The similarity score between " + q + u"<a> and "u"</a>" + Goal2 + u"<a> is: "u"</a>" + str(sss(q,Goal2)) + u"</p>"
        
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