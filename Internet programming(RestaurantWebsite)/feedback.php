<?php
  include "connect.php";
  include "navbar.php";
  require_once 'auth_check.php';
?>
<!DOCTYPE html>
<html>
<head>
  <title>Feedback</title>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
  <link rel="stylesheet" href="css/my_style.css">
  <style type="text/css">
    body{
      background-image: url("img/feedback.jpg");
    }
    .wrapper{
      padding:10px;
      margin: -20px auto;
      width: 900px;
      height:600px;
      background-color: black;
      opacity: .8;
      color: white;
      text-align: center;
    }
    .wrapper h3{
      margin-top: 10px;
    }
    .form-control{
      height: 70px;
      weight:60%;
    }
    .scroll{
      width:100%;
      height:350px;
      overflow: auto;
    }
    .scroll table{
      color: white;
    }
  </style>
  <script>
    $(document).ready(function(){
      var count=2;
      $("#button1").click(function(){
        count=count+2
        $("#comments").load("load-comments.php",{newcount:count});
      });
    });
  </script>
</head>
<body>
  <div class="wrapper">
    <h3>Write Feedback</h3>
    <form style="" action="" method="post">
      <input class="form-control" type="text" name="comment" placeholder="Write something..."></input><br>
      <input class="btn btn-info"  type="submit" name="submit" value="Comment" style="width:100px; height:35px;"></input>
    </form>
  <br>
  <div id="comments" class="scroll">
    <?php
      if(isset($_POST['submit'])){
        $sql="INSERT INTO `comments` VALUES('','$_POST[comment]');";
        if(mysqli_query($db,$sql)){
          $q="SELECT * FROM `comments` ORDER BY `comments`.`id` DESC LIMIT 2";
          $res=mysqli_query($db,$q);
          echo "<table class='table table-bordered'>";
          while($row=mysqli_fetch_assoc($res)){
            echo "<tr>";
              echo "<td>"; echo $row['comment']; echo "</td>";
            echo "</tr>";
          }
        echo "</table>";
        }
      }
      else{
        $q="SELECT * FROM `comments` ORDER BY `comments`.`id` DESC LIMIT 2";
        $res=mysqli_query($db,$q);
        echo "<table class='table table-bordered'>";
        while($row=mysqli_fetch_assoc($res)){
          echo "<tr>";
            echo "<td>"; echo $row['comment']; echo "</td>";
          echo "</tr>";
        }
      echo "</table>";
      }
    ?>
  </div>
    <input type="button" id="button1" class="btn btn-info" value="Show more">
</div>
</body>
</html>
