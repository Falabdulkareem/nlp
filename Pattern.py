# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Fatima"
__date__ ="$1-Oct-2014 12:31:07 PM$"

import re
from Negation import Find_Negation
import xlsxwriter

def test_patterns(text, Pref_loc, patterns=[]):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print
    them to stdout.
    """
    # Add a number to each regex, to assign it to the excel sheet (for K fold cross validation)
    #RegexNo = No
    
    # Look for each pattern in the text and print the results
    for pattern in patterns:
        #print
        #print 'Matching "%s"' % pattern
        for match in re.finditer(pattern, text):
            if match:
                print 'Matching "%s"' % pattern
                print 'This is pref loc'
                print Pref_loc
                """
                col = 1
                write_worksheet.write(curr_row, col, text)
                write_worksheet.write(curr_row, col + 1, RegexNo)
                write_worksheet.write(curr_row, col + 2, pattern)
                """
                if Pref_loc == 1:   
                    # The preference then the goal is specified in the sentence
                    if pattern == 'i[\W]?( am|m) (.*?) in (.*)' or pattern == 'i[\W]?( am|m) (.*?) to (.*)' or pattern == 'i[\W]?( am|m) (.*?) [a-z]{0,2}[\s]*achieving (.*)'\
                    or pattern == 'i[\W]?( am|m) (.*?) of (.*)':
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
                    '''
                    # The preference is in the first block
                    if pattern == '[a-z\s\W]+ (achieve|achieving|complete|completing) (.*) or not' or pattern == 'if there[\W]?( is|s) time left (.*)' or \
                    pattern == 'not that [a-z\s]+ (to|you) (.*)' or pattern == '(disregard|ignore entirely|skip|ignore) (.*)' or pattern == '(don[\W]t forget|don[\W]t spend any[\s]?time) (.*)'\
                    or pattern == '(you may or may not|you may have) (.*)' or pattern == 'must (complete|always) (.*)':
                        Pref = match.group().replace(match.group(2),'').lstrip()
                        GoalForm = Find_Negation(match.group(2))
                        PrefForm = Find_Negation(Pref)
                        print Pref
                        return Pref, match.group(2), GoalForm, PrefForm
                    '''
                    
                    # The preference is in the first&second block 
                    if pattern == '(you|participants|we|nurses?) (should definitely|should keep|should|need|can|would benefit) (.*)':
                        Pref = match.group().replace(match.group(3),'').lstrip()
                        GoalForm = Find_Negation(match.group(3))
                        PrefForm = Find_Negation(Pref)
                        print Pref
                        return Pref, match.group(3), GoalForm, PrefForm
                    else:
                        print match.group(1)
                        Pref = match.group().replace(match.group(1),'').lstrip()          # extract match.group(1) from the whole sentence to get the pref
                        GoalForm = Find_Negation(match.group(1))
                        PrefForm = Find_Negation(Pref)
                        print Pref
                        return Pref, match.group(1), GoalForm, PrefForm
                    #RegexNo += 1
                    
                elif Pref_loc == 4:
                    # The preference then the goal is specified in the sentence
                    # The preference is defined in the regex
                    # The preference is in the first block
                    Pref = match.group().replace(match.group(2),'').lstrip()
                    GoalForm = Find_Negation(match.group(2))
                    PrefForm = Find_Negation(Pref)
                    print "This is the pref: " + Pref
                    return Pref, match.group(2), GoalForm, PrefForm
        
    return None, None, None, None
            
            
            
    