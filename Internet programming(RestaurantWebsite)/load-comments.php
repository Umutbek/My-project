<?php
    include "connect.php";
    $newcount=$_POST['newcount'];
    $q="SELECT * FROM `comments` ORDER BY `comments`.`id` DESC LIMIT $newcount";
    $res=mysqli_query($db,$q);
    echo "<table class='table table-bordered'>";
    while($row=mysqli_fetch_assoc($res)){
      echo "<tr>";
        echo "<td>"; echo $row['comment']; echo "</td>";
      echo "</tr>";
    }
  echo "</table>";
?>
