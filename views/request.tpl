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
        <div class="col-md-6">
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
    </div>
    
    <div class="row">
        <div class="col-md-12">
            <div class="panel panel-primary">
               <div class="panel-heading">
                  <h3 class="panel-title">Highest Score</h3>
               </div>
               <div class="panel-body">
                    %if MaxScore is not None:
                      {{ MaxScore }}
                    %else:
                      No high score 
                    %end
               </div>
             </div> 
        </div>
    </div>

        <div class="panel panel-primary">
          <div class="panel-heading">
            <h3 class="panel-title">Results</h3>
          </div>
          <div class="panel-body">
            %try:
            <table class="table">
              %for result in GoalsSimilarity:
                <tr class="active"><td>{{ result }}</td></tr>
              %end
            </table>
            %except:
              No results
            %end
          </div>
        </div> 
         
      </div>
    </div>
  </div>

  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
</body>
</html>