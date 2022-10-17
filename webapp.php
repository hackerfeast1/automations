<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="index.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Viga&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Francois+One&display=swap" rel="stylesheet">
<title>TRACKER</title>
</head>
<body>


<nav class="navbar ">
  <div class="container-fluid" style="align-items:center">
   <h2 class="name">COVID TRACKER</h2>
   <p class="second">India's Covid Details Win Over new and repeast <br> by sending emails<span>❤️</span></p>
   <img src="image.png" alt="profile-image">
  </div>
</nav>

<!-- As a heading -->
<nav class="navbar bg-light">
  <div class="container-fluid">
    <span class="navbar-brand mb-0 h1"></span>
  </div>
</nav>

<div class="middlecontainer"> 
  <div class="resources">
    <h2 class="sub">India's 2021 Covid Tracker </h2>
    <img src="image2.png" class="image2" alt="girl">
  </div>
</div>
</body>

    <?php 
    $data=file_get_contents('https://api.covid19india.org/data.json');
    $decode=json_decode($data,true);
    $i=1;
    ?>
    <table class="table table-hover table-sm w-25 p-3 table-light table-bordered" >
      <thead class="thead-dark">
      <tr>
        <th class="text-info table-active ml-2">State</th>
        <th class="text-danger table-active ml-2  ">Confirmed</th>
        <th class="text-success table-active">Active</th>
      </tr>
      </thead>
    
    <?
    for($i=1;$i<=10;$i++)
    {
      ?>
      <tr>
      <td><? echo $decode["statewise"][$i]["state"] ."\n";?></td>
      <td><? echo $decode["statewise"][$i]["confirmed"]."\n";?></td>
      <td><? echo $decode["statewise"][$i]["active"]."\n";?></td  >
      </tr>
      <?
    } 

    ?>
    </table>

    <div class="bottom-container">
      <div class="final"></div>
      <h1>hello mlf</h1>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
</body>
</html
