<!DOCTYPE html>
<html>

	<head>
<!-- 		<script type="text/javascript">
			history.back();
		</script> -->
		<script src="captiveportal-code.js"></script>
		
	</head>

	<body>
	  <?php 	  
		$remote_address = getenv("REMOTE_ADDR");
		// echo "Your IP address is $remote_address.";
		$browser_type = getenv("HTTP_USER_AGENT");
		// echo "You are using $browser_type.";
        $myfile='captiveportal-file.txt';
        $handle = fopen($myfile, 'w') or die ('Cannot open');
        $data= '{"username":"'.$remote_address.'","gender":"'.$_POST['gender'].'","age":"'.$_POST['age'].'","qatar_resident":"'.$_POST['qatar_resident'].'","children":"'.$_POST['children'].'"}';
        fwrite($handle, $data);
        // echo("<script>console.log(".json_encode($data).");</script>");
      ?>
      <?php 	  
        $visitfile='captiveportal-visit.txt';
        $visithandle = fopen($visitfile, 'w') or die ('Cannot open');
        $visitdata= 'Yes';
        fwrite($visithandle, $visitdata);
      ?>
      		<script type="text/javascript">
			history.back();
		</script>
	</body>
</html>