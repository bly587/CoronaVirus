<?php

$url = 'https://www.ocregister.com/wp-content/uploads/2018/11/1104-REALBRIEFS-Chapman-Keck-32.jpg?w=810';
?>


<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Sign Up</title>
    <style type="text/css">
      body
      {
        margin: 0;
        padding: 0;
        font-family: sans-serif;
        background: #34495e;
        background-image: url('<?php echo $url ?>');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: cover;
      }
      header{
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('<?php echo $url ?>');
        height: 100vh;
        background-size: cover;
        background-position: center;
      }

      ul{
        list-style-type: none;
        margin-top: 25px;
      }

      ul li{
        display: inline-block;
      }

      ul li a{
        text-decoration: none;
        color: #fff;
        padding: 5px 20px;
        border: 1px solid #fff;
        transition: 0.6s ease;
      }

      ul li a:hover{
        background-color: #fff;
        color: #000;
      }

      .main{
        max-width: 1200px;
        margin: 0;
        position: fixed;
        right: 20px;
      }

      .box{
        width: 40%;
        padding: 40px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
      }

      .box h1{
        color: white;
        text-transform: uppercase;
        font-weight: 500;
      }

      .box input[type = "text"]{
        border: 0;
        background: none;
        display: block;
        margin: 20px auto;
        text-align: center;
        border: 2px solid #3498db;
        padding: 14px 10px;
        width: 200px;
        outline: none;
        color: white;
        border-radius: 24px;
        transition: 0.25s;
      }

      .box input[type = "text"]:focus{
        width: 280px;
        border-color: #2ecc71;
      }

      .box input[type = "submit"]{
        border: 0;
        background: none;
        display: block;
        margin: 20px auto;
        text-align: center;
        border: 2px solid #2ecc71;
        padding: 14px 40px;
        outline: none;
        color: white;
        border-radius: 24px;
        transition: 0.25s;
        cursor: pointer;
      }


      .box input[type = "submit"]:hover{
        background: #2ecc71;
      }
    </style>
    <!-- <link rel="stylesheet" type="text/css" href="style1.css"> -->
  </head>
  <body>
    <header>
      <div class="main">
        <ul>
          <li><a href="./index.html">Home</a></li>
          <li><a href="./index.html#about">About</a></li>
          <li><a href="./signup.php">Sign Up</a></li>
        </ul>
      </div>
      <form class="box" action="includes/signup.inc.php" method="post">
        <h1>Sign Up</h1>
        <input type="text" name="mailuid" placeholder="Email">
        <input type="submit" name="signup-submit" value="Sign Up">
        <h1>Get Info</h1>
        <input type="submit" name="get_Info" value="Get Info">
      </form>
    </header>
  </body>
</html>
