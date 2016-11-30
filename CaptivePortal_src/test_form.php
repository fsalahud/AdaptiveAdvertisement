<!DOCTYPE html>
<html lang="en">
  <head>
  <!-- <meta http-equiv="refresh" content="10" /> -->

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width" />
    <script src="captiveportal-ajax.jquery.min.js"></script>
    <!-- <script src="captiveportal-jquery.serializejson.js"></script> -->
    
    <link href="captiveportal-main.css" rel="stylesheet" type="text/css" />
    <link rel='stylesheet prefetch' href='http://netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css'>

  </head>


  <!-- action="$PORTAL_ACTION$" -->
<!--   <body onload="visit();">
 -->
   <body>
     <div class="row">
    <div class="far col-sm-12">
    <div class="navigation_form"><img src="captiveportal-2022.png" id="logo"> 
       <p id="title_form">Welcome to <br>Stadium Wi-Fi </p>
      </div>
    </div>
    </div>

    <div class="far-bg-img_form">
    <img src="captiveportal-qatar_sky2.jpg">
    </div>
    <div class="row">
    <div class="far col-sm-6">
    <div class="wrapper">
    <div id="info">

      <h2 class="form-signin-heading">Fill in your information to connect to the wireless network</h2>
        
      <form class="form-signin" method="post" id="ajaxform" role="form" action="captiveportal-success.php">       
        <div class="form-group">
          <div class="category"> What is your Gender? </div>
          
          <div class="far radio">
              <input id="male" type="radio" name="gender" value="male" required>
              <label for="male"><span id="far-op">Male</span></label>
          </div>
         
         
          <div class="far radio">
              <input id="female" type="radio" name="gender" value="female">
              <label for="female"><span id="far-op">Female</span></label>
          </div>
         
        </div>
        <hr>

       
        <div class="form-group" id="age">
          <div class="category">What is your Age Group?</div>
            <select class="form-control" name="age" required>
              <option>15-20</option>
              <option>21-30</option>
              <option>31-40</option>
              <option>41-50</option>
              <option>51-older</option>
            </select>
        </div>
        <hr>
    
        <div class="form-group">
          <div class="category">What is your Residency Status?</div>
           
            <div class="far radio">
                <input id="res-yes" type="radio" name="qatar_resident" value="Yes" required>
                <label for="res-yes"><span id="far-op">Resident</span></label>
            </div>
          
    
            <div class="far radio">
                <input id="res-no" type="radio" name="qatar_resident" value="No">
                <label for="res-no"><span id="far-op">Non-Resident</span></label>
            </div>
            
        </div>
        <hr>

        <div class="form-group">
          <div class="category">Have children with you?</div>
           
            <div class="far radio">
                <input id="child-yes" type="radio" name="children" value="Yes" required>
                <label for="child-yes"><span id="far-op">Yes</span></label>
            </div>  
       
            
            
            <div class="far radio">
                <input id="child-no" type="radio" name="children" value="No" required>
                <label for="child-no"><span id="far-op">No</span></label>
            </div>
           
        </div>
        <hr>

          <!-- <input name="redirurl" type="hidden" value="captiveportal-sucess.html"> -->
          <!-- <input name="zone" type="hidden" value="$PORTAL_ZONE$"> -->
        <input type="submit" name="testaccept" id="simplepost" class="fin btn btn-info" value="Continue">
      </form>
      </div>

          <br>
          <br>
          <br>
     <div id="connection">


          <form method="post" action="$PORTAL_ACTION$">
                <!-- <form class="form-signin" method="post" action="captiveportal-final.php"> -->
                 <h2 class="farj-heading">Almost there!</h2>
                 <div class="farj-heading">Connect to access the internet</div>
            <input name="redirurl" type="hidden" value="captiveportal-final.php">
            <input name="accept" type="submit" id="connectbtn" class="farj btn btn-info" value="Connect" onclick="">
          </form>
          </div>

          <div id="div1">
          </div>

          
    </div>
    </div>
    </div>


    <script type="text/javascript">
      var visit_check;
      $(document).ready(function(){
        setTimeout(function(){
          $("#div1").load("captiveportal-visit.txt");
        },2000);
      setTimeout(function(){
        visit_check=$('#div1').html()
        console.log(visit_check);
      },2500);
      setTimeout(function(){
        if(visit_check=== "Yes"){
          $('#info').css('display','none');
          $('#connection').css('display','block');
        }
      },3000);
    });
     
    </script>


  
  </body>
</html>

    
    
    


