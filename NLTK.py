#!/usr/bin/env python
# coding: utf-8

# Copyright (c) 2012, Machinalis S.R.L.
# This file is part of quepy and is distributed under the Modified BSD License.
# You should have received a copy of license in the LICENSE file.
#
# Authors: Rafael Carrascosa <rcarrascosa@machinalis.com>
#          Gonzalo Garcia Berrotaran <ggarcia@machinalis.com>

__author__="Fatima"
__date__ ="$7-Jul-2014 4:41:18 PM$"

import nltk, re, pprint


def ie_preprocess(document):
   
        text = nltk.word_tokenize(document)
        text = nltk.pos_tag(text)
        print text
                
        grammar = "NP: {<DT>?<NN.*>+}"
        # "NP: {<DT>?<JJ.*>*<NN.*>+}"
        
        cp = nltk.RegexpParser(grammar)
   
        result = cp.parse(text) 
        print(result) 
        result.draw()

              