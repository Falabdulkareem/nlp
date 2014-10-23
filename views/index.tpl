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
                  <div class="col-md-4">
                    <div class="panel panel-primary" style="min-height: 280px;">
                      <div class="panel-heading">
                          <h3 class="panel-title">Motivation</h3>
                      </div>
                        <div class="panel-body">
                           <p>This Natural Language Interface allows users to express <a href="#">goals and preferences</a> without the need to understand the underlying structure and would get the benefits easily by using language of daily communication</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="panel panel-primary" style="min-height: 280px;">
                      <div class="panel-heading">
                          <h3 class="panel-title">Used Techniques</h3>
                      </div>
                        <div class="panel-body">
                           <p>Our natural language interface combines two methods: regular expressions and statistical method</p><p>The regular expressions match the preferences entered by the user and translate them to a predefined scale, while the statistical method measures the semantic similarity between the natural language query entered by the user and the set of goals to find the highest matching goal</p>
                        </div>
                    </div>
                </div>
                    <div class="col-md-4">
                    <div class="panel panel-primary" style="min-height: 280px;">
                     <div class="panel-heading">
                          <h3 class="panel-title">Outputs</h3>
                      </div>
                        <div class="panel-body">
                           <ul>
                                <li>Identify preferences</li>
                                <li>Measure the semantic similarity between the query entered and the set of goals</li>
                                <li>Identify the highest matching goal</li>
                                <li>Detect if the query entered was in negative form</li>
                                <li>Detect if the preference entered was in negative form</li>
                           </ul>
                        </div>
                    </div>
                </div>
            </div>              
                         
      <div class="jumbotron"> 
        <div class="row">    
            <div class="col-md-10">
                <form role="form" action="/request" method="POST">
                    
                    <div class="form-group">
                        <label class="col-lg-3 control-label">Choose Domain:</label>
                       
                              <div class="col-lg-3 text-primary" "radio">
                                <label>
                                  <input name="optionsRadios" id="NurseRadios" value="1" checked="" type="radio">
                                  Nurse domain 
                                </label>
                              </div>
                             
                                <div class="col-lg-3 text-primary" "radio">
                                  <label>
                                    <input name="optionsRadios" id="BookRadios" value="2" type="radio">
                                   Book order domain
                                  </label>
                                </div>
                            
                     </div>
                   
                    <br></br>
                                    
                    <div class="col-md-8">
                        <div class="form-group">
                            <label for="input">Enter you natural language query:</label>
                            <input type="text" class="form-control" id="input" name="input" placeholder="Enter a question">
                        </div>

                        <button type="submit" class="btn btn-primary">Get answer</button>
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