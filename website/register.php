<html>
<?php
  include "connect.php";
?>
<head>
<title>Login Form Design</title>
    <link rel="stylesheet" type="text/css" href="style1.css">
    <style>
    body{
        background: url(img/res.jpg);
    }
    </style>
</head>
<body>
    <div class="loginbox">
    <img src="img/avatar.png" class="avatar">
        <h1>Register</h1>
        <form method="post" action="">
            <p>Username</p>
            <input type="text" name="username" placeholder="Enter Username..." required="">
            <p>Email</p>
            <input type="email" name="email" placeholder="Enter Email..." required="">
            <p>Password1</p>
            <input type="password" name="password1" placeholder="Enter password..." required="">
            <p>Password2</p>
            <input type="password" name="password2" placeholder="Confirm password" required="">
            <input type="submit" name="submit" value="Register">
            <a href="index.php">Already Have an account?</a>
        </form>
    </div>
    <?php
  		if (isset($_POST['submit'])){
  			$count=0;
  			$sql="SELECT username from USER";
  			$res=mysqli_query($db,$sql);
  			while($row=mysqli_fetch_assoc($res)){
  				if($row['username']==$_POST['username']){
  					$count=$count+1;
  				}
  			}
  		if($_POST['password1']!=$_POST['password2']){
  			?>
  				<script type="text/javascript">
  					alert("Password doesn't match!!!");
  				</script>
  			<?php
  		}
  		else{
  		if($count==0){
  			mysqli_query($db,"INSERT INTO `USER` VALUES('$_POST[username]','$_POST[email]','$_POST[password1]','$_POST[password2]');");
  	?>
  		<script type="text/javascript">
  			alert("Registration successfull");
        window.location="index.php";
  		</script>
  	<?php
  }
  		else{
  			?>
  				<script type="text/javascript">
  					alert("Username already exist");
  				</script>
  			<?php
  		}
  	}
    	}
    ?>
</body>
</html>
