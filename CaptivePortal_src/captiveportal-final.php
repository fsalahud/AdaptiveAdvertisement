<!DOCTYPE html>
<html>

<head>
<meta charset="utf-8">
    <meta name="viewport" content="width=device-width" />
	<script src="captiveportal-code.js"></script>
  <script src="captiveportal-ajax.jquery.min.js"></script>
  <script src="captiveportal-jquery.serializejson.js"></script>
  <script type="text/javascript">
    var filePath = "captiveportal-file.txt";
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET",filePath,false);
    xmlhttp.send(null);
    var fileContent = xmlhttp.responseText;
    var convert= JSON.parse(fileContent);
    // console.log(fileContent);
    // console.log(convert);


    $.ajax(
        {
          url : "http://testad1234.herokuapp.com/api/adduser/",
          type: "POST",
          data : convert,
          headers : {'Content-Type':undefined},
          success:function(result)
                  {
                    console.log("success");
                    alert("post success");
                  }
        });
    </script>
  
    <link href="captiveportal-main.css" rel="stylesheet" type="text/css" />
    <link href="captiveportal-success.css" rel="stylesheet" type="text/css" />
    <link rel='stylesheet prefetch' href='http://netdna.bootstrapcdn.com/bootstrap/3.0.2/css/bootstrap.min.css'>

  </head>

  <body>
  <?php     
        $visitfile='captiveportal-visit.txt';
        $visithandle = fopen($visitfile, 'w') or die ('Cannot open');
        $visitdata= 'No';
        fwrite($visithandle, $visitdata);
      ?>
   <div class="row">
    <div class="far col-sm-12">
    <div class="navigation fin_nav"><img src="captiveportal-2022.png" id="logo"> 
       <p id="title">Welcome to <br>Stadium Wi-Fi </p>
      </div>
    </div>
    </div>

    <div class="succ far-bg-img">
    <img src="captiveportal-qatar_sky2.jpg">
    </div>
    <div class="row">
    <div class="far col-sm-6">
    <div class="wrapper">


    <h2 class="success form-signin-heading">Connection Successful!<br>
      <span id="subhead">You can now access the internet </span></br></br> <span id="surprise">Keep a watch on the billboards ahead! ;) </span>
    </h2>
       
    </div>
    </div>
    </div>
  </body>
</html>