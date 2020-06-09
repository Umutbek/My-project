<?php
  include "connect.php";
  include "navbar.php";
  require_once 'auth_check.php'
?>
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Title</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
  integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="css/my_style.css">
</head>
<body>
<!---slider--->
<div id="slider">
<div id="headerslider" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#headerslider" data-slide-to="0" class="active"></li>
    <li data-target="#headerslider" data-slide-to="1"></li>
    <li data-target="#headerslider" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block img-fluid" src="img/slider1.jpg">
    </div>
  <div class="carousel-item">
    <img class="d-block img-fluid" src="img/3.jpg">
  </div>
  <div class="carousel-item">
    <img class="d-block img-fluid" src="img/4.jpg">
  </div>
  </div>
  <a class="carousel-control-prev" href="#headerslider" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#headerslider" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
<section id="gallery">
  <div class="container">
    <h1>Gallery</h1>
    <div class="row">
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/adana.jpg">
    <img src="img/adana.jpg" class="img-responsive">
    </a>
      <div><h3>Adana Kebab</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/tavuk.png">
    <img src="img/tavuk.png" class="img-responsive">
    </a>
      <div><h3>Tavuk Kebab</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/th.jpg">
    <img src="img/th.jpg" class="img-responsive">
    </a>
      <div><h3>Sheftali Kebab</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/kuzu.jpg">
    <img src="img/kuzu.jpg" class="img-responsive">
    </a>
      <div><h3>Kuzu Kebab</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/salmon.jpg">
    <img src="img/salmon.jpg" class="img-responsive">
    </a>
      <div><h3>Salmon</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/cupra.jpg">
    <img src="img/cupra.jpg" class="img-responsive">
    </a>
      <div><h3>Cupra</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/levrek.jpg">
    <img src="img/levrek.jpg" class="img-responsive">
    </a>
      <div><h3>Levrek</h3></div>
    </div>
    </div>
    <div class="col-md-3 profile-pic text-center">
    <div class="img-box">
    <a target="_blank" href="img/kalamar.jpg">
    <img src="img/kalamar.jpg" class="img-responsive">
    </a>
      <div><h3>Kalamar</h3></div>
    </div>
    </div>
  </div>
</div>
</section>
<section id="about">
  <div class="container">
    <h1>About us</h1>
    <div class="first">
      <img class="img1" src="img/about1.jpg" alt="Aspava">
      <p>Aspava Restaurant aims to provide a professional,
         friendly and courteous service to all our guests.
          To maintain a clean, comfortable and well maintained premises for both guests and staff.
          To produce the best quality and delicious food only using the best quality ingredients.
           By upholding these values and supporting local fisherman and farmers,
            where we get most of our high quality produce,
             we have been serving the best tasting kebabs and seafood to Cyprus for 40 years.</p>
    </div>

</div>
</section>
<!---Contact us----->
<section id="contact">
  <div class="container">
    <h2>Contact us</h2>
  <div class="row">
    <div class="col-md-6">
      <form class="contact-form" action="index.php" method="post">
        <div class="form-group">
          <input type="text" class="form-control" name="first_name" placeholder="Your name">
        </div>
        <div class="form-group">
          <input type="text" class="form-control" name="phone_number" placeholder="Phone Number">
        </div>
        <div class="form-group">
          <input type="email" class="form-control" name="email" placeholder="Email Address">
        </div>
        <div class="form-group">
          <textarea class="form-control" rows="4.5" name="message" placeholder="Your Message"></textarea>
        </div>
        <button type="submit" name="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
  <?php
  if(isset($_POST['submit'])){
    $first_name=$_POST['first_name'];
    $phone_number=$_POST['phone_number'];
    $email=$_POST['email'];
    $message=$_POST['message'];
    $q="INSERT INTO `contact` VALUES('$first_name','$phone_number','$email','$message');";
    mysqli_query($db,$q);
  }
  ?>
  <div class="col-md-6 contact-info">
    <div class="follow"><b>Address:</b><i class="fa fa-map-marker"></i>Yedidalga</div>
    <div class="follow"><b>Phone:</b> <i class="fa fa-phone"></i> +905338338067</div>
    <div class="follow"><b>Email:</b> <i class="fa fa-envelope-o"></i> aspava1970@gmail.com</div>
    <div class="follow"><label><b>Social Media:</b></label>
      <a href="https://www.instagram.com/aspava.a/"><i class=" fa fa-instagram"></i></a>
      <a href="https://www.facebook.com/AspavaRestaurantYedidalga"><i class=" fa fa-facebook"></i></a>
    </div>
  </div>
</div>
</div>
</section>
<section id="footer">
  <div class="container text-center">
    <p>Thank you for visiting <i class="fa fa-heart-o"></i></p>
  </div>
</section>
  </body>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</html>
