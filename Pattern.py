# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$1-Oct-2014 12:31:07 PM$"

import re
from Negation import Find_Negation

def test_patterns(text, Pref_loc, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    
    # Look for each pattern in the text and print the results
    for pattern in patterns:
        print
        print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            if match:
                if Pref_loc == 1:   
                    # The preference then the goal is specified in the sentence
                    if pattern == 'i[\W]?( am|m) (.*?) in (.*)' or pattern == 'i[\W]?( am|m) (.*?) to (.*)' or pattern == 'i[\W]?( am|m) (.*?) [a-z]{0,2}[\s]*achieving (.*)':
                         PrefForm = Find_Negation(match.group(2))
                         GoalForm = Find_Negation(match.group(3))
                         return match.group(2), match.group(3), GoalForm, PrefForm 
                    else:
                        PrefForm = Find_Negation(match.group(1))
                        GoalForm = Find_Negation(match.group(2))
                        return match.group(1), match.group(2), GoalForm, PrefForm 

                elif Pref_loc == 2: 
                    # The goal then the preference is specified in the sentence
                    GoalForm = Find_Negation(match.group(1))
                    PrefForm = Find_Negation(match.group(2))
                    return match.group(2), match.group(1), GoalForm, PrefForm 
                 
                elif Pref_loc == 3:
                    # The preference then the goal is specified in the sentence
                    # The preference is defined in the regex
                    if pattern == '[a-z\s\W]+ (achieve|achieving|complete|completing) (.*) or not' or pattern == 'if there[\W]?( is|s) time left (.*)' or \
                    pattern == 'not that [a-z\s]+ (to|you) (.*)' or pattern == '(disregard|ignore entirely) (.*)':
                        Pref = match.group().replace(match.group(2),'').lstrip()
                        GoalForm = Find_Negation(match.group(2))
                        PrefForm = Find_Negation(Pref)
                        print Pref
                        return Pref, match.group(2), GoalForm, PrefForm
                    else:
                        print match.group(1)
                        Pref = match.group().replace(match.group(1),'').lstrip()
                        GoalForm = Find_Negation(match.group(1))
                        PrefForm = Find_Negation(Pref)
                        print Pref
                        return Pref, match.group(1), GoalForm, PrefForm

    return None, None, None, None
            
            
            
    