<?php
  session_start();
  include "connect.php";
?>
<html>
<head>
<title>Login Form Design</title>
    <link rel="stylesheet" type="text/css" href="style1.css">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css" integrity="sha384-gfdkjb5BdAXd+lj+gudLWI+BXq4IuLW5IT+brZEZsLFm++aCMlF1V92rMkPaX4PP" crossorigin="anonymous">
    <style>
        #messages{
          background-color: grey;
          color: black;
          padding: 10px;
          margin-top: 10px;
        }
        .custom{
          position:absolute;
          top:260px;
          right:30px;
          padding:5px;
          color: white;
          cursor: pointer;
          opacity:0.5;
        }
        .custom:hover{
          opacity:1;
        }
        .custom:active{
          transform: scale(0.9);
        }
        body{
            background: url(img/res.jpg);
        }
    </style>
</head>
<body>
    <div class="loginbox">
    <img src="img/avatar.png" class="avatar">
        <h1>Login Here</h1>
        <form action="" method="post">
            <p>Username</p>
            <input type="text" name="username" placeholder="Enter Username" required="">
            <p>Password</p>
            <input type="password" id="txtpassword" name="password" placeholder="Enter Password" required="">
            <i id="eye" class="fa fa-eye-slash custom" aria-hidden="true"></i>
            <input type="submit" name="submit" value="Login">
            <a href="register.php">Don't have an account?</a>
        </form>
    </div>
    <script type="text/javascript">
      $(document).ready(function(){
        $("#eye").click(function(){
          var pass= $("#txtpassword");
          if(pass.attr("type")==="password"){
            $("#eye").removeClass("fa-eye-slash").addClass("fa-eye");
            pass.attr("type","text");
          }
          else{
            $("#eye").removeClass("fa-eye").addClass("fa-eye-slash");
            pass.attr("type","password");
          }
        });
      });
    </script>
<?php
if (isset($_POST['submit'])){
  $username=$_POST['username'];
  $count=0;
  $res=mysqli_query($db,"SELECT * FROM `USER` WHERE username='$_POST[username]' && password1='$_POST[password]';");
  $count=mysqli_num_rows($res);
if($count==0){
    ?>
    <script>
      alert("Invalid password or username");
    </script>
  <?php
  }
else{
  $_SESSION['username']=$username;
  header("location:main.php");
  }
}
?>
</body>
</html>
