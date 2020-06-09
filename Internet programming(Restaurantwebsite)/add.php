<?php
  include "connect.php";
  include "navbar.php";
  require_once 'auth_check.php';
?>
<!DOCTYPE html>
<html>
<head>
  <title>Add</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="css/my_style.css">
  <link rel="stylesheet" href="style1.css">
  <style>
  body{
      background: url(img/res2.jpg);
  }
  </style>
</head>
<body>
  <div class="loginbox">
    <h1>Add Menu</h1>
    <form method="POST" action="">
      <label for="username">Food Name:</label><br>
      <input type="text" id="username" name="name"><br>
      <label for="pwd">Cost:</label><br>
      <input type="number" id="pwd" name="cost" min=0 ><br>
      <label>Category:</label><br>
      <select name="category">
      <option selected>Choose...</option>
      <option>Kebab</option>
      <option>Fishe</option>
      <option>Drink</option>
      </select>
      <br><br>
      <input class="btn btn-info" type="submit" name="submit" value="Add Menu">
    </form>
  </div>
<?php
  if(isset($_POST['submit'])){
    $name=$_POST['name'];
    $cost=$_POST['cost'];
    $category=$_POST['category'];
    $q="INSERT INTO `order` VALUES('','$name','$cost','$category');";
    mysqli_query($db,$q);
    ?>
    <script>
      alert("Menu Added Successfully");
    </script>
    <?php
  }
?>
</body>
</html>
