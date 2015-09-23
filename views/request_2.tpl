<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Natural Language Interface for Goals and Preferences</title>

  <!-- Bootstrap -->
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootswatch/3.2.0/united/bootstrap.min.css">

  <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
      <![endif]-->
</head>
<body>
  <div class="container">
    <h1>Natural Language Interface for Goals and Preferences</h1>
    <div class="row">
       <div class="col-md-6">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">Goal</h3>
                </div>
                <div class="panel-body">
                   %if Goal is not None:
                        {{ Goal }}
                   %else:
                        The system was unable to detect the goal 
                   %end
                </div>
            </div> 
        </div>
        
        <div class="col-md-6">
            <div class="panel panel-danger">
                 <div class="panel-heading">
                      <h3 class="panel-title">Goal Form</h3>
                 </div>
                 <div class="panel-body">
                    %if GoalForm is not None:
                      {{ GoalForm }}
                    %else:
                      The system was unable to detect the form of the goal 
                    %end
                  </div>
             </div> 
        </div>
     </div>

    <div class="row">
        <div class="col-md-6">
            <div class="panel panel-primary">
                <div class="panel-heading">
                    <h3 class="panel-title">Preference</h3>
                </div>
                <div class="panel-body">
                   %if Preference is not None:
                        {{ Preference }}
                   %else:
                        No preferences specified in the entered query 
                   %end
                </div>
            </div> 
        </div>
        <div class="col-md-3">
                <div class="panel panel-danger">
                   <div class="panel-heading">
                        <h3 class="panel-title">Preference Form</h3>
                   </div>
                   <div class="panel-body">
                      %if PrefForm is not None:
                        {{ PrefForm }}
                      %else:
                        No preferences specified in the entered query
                      %end
                    </div>
                </div> 
        </div>
        <div class="col-md-3">
                <div class="panel panel-danger">
                    <div class="panel-heading">
                        <h3 class="panel-title">Preference Value</h3>
                    </div>
                    <div class="panel-body">
                        %if PrefValue is not None:
                            %if PrefLoc == 1:
                            <table class="table">
                                %for output in PrefValue:
                                <tr class="active"><td>{{ output }}</td></tr>
                                %end
                            </table>
                            %else:
                            {{ PrefValue }}
                            %end
                        %else:
                            Preference value could not be identified 
                        %end
                    </div>
                </div> 
        </div>
    </div>
 
    <form role="form" action="/request_2" method="POST">
    <div class="panel panel-default">
        <div class="panel-body">
            <div class="form-group">
            <label class="col-lg-2 control-label">Did you mean: (Neg)</label>
            <div class="col-lg-10">
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadiosNeg" id="optionNeg1" value="{{MatchingGoalP}}, optionNeg1" >
                  {{MatchingGoalP}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadiosNeg" id="optionNeg2" value="{{SecondMatchingGoalP}}, optionNeg2">
                  {{SecondMatchingGoalP}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadiosNeg" id="optionNeg3" value="{{ThirdMatchingGoalP}}, optionNeg3">
                  {{ThirdMatchingGoalP}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadiosNeg" id="optionsNeg4" value="{{FourthMatchingGoalP}}, optionsNeg4">
                  {{FourthMatchingGoalP}}
                </label>
              </div>
               <div class="radio">
                <label>
                  <input type="radio" name="optionsRadiosNeg" id="optionNeg5" value="{{FifthMatchingGoalP}}, optionNeg5">
                  {{FifthMatchingGoalP}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadiosNeg" id="optionNeg6" value="None, optionNeg6">
                  None of the above
                </label>
              </div>
            </div>
          </div>
          
                <br><br><br><br><br><br><br><br><br>
                
          <div class="form-group">
            <label class="col-lg-2 control-label">Did you mean:</label>
            <div class="col-lg-10">
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadios" id="option1" value="{{MatchingGoal}}, option1" >
                  {{MatchingGoal}} 
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadios" id="option2" value="{{SecondMatchingGoal}}, option2">
                  {{SecondMatchingGoal}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadios" id="option3" value="{{ThirdMatchingGoal}}, option3">
                  {{ThirdMatchingGoal}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadios" id="option4" value="{{FourthMatchingGoal}}, option4">
                  {{FourthMatchingGoal}}
                </label>
              </div>
               <div class="radio">
                <label>
                  <input type="radio" name="optionsRadios" id="option5" value="{{FifthMatchingGoal}}, option5">
                  {{FifthMatchingGoal}}
                </label>
              </div>
              <div class="radio">
                <label>
                  <input type="radio" name="optionsRadios" id="option6" value="None, option6">
                  None of the above
                </label>
              </div>
              <div class="form-group">
                <div class="col-lg-15 col-lg-offset-2">
                  <button type="submit" class="btn btn-primary">Submit</button>
                </div>
              </div>      
            </div>
          </div>      
        </div>
    </div>
    </form>
        
    
                    
   

        
         
      </div>
    </div>
  </div>

  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
</body>
</html>