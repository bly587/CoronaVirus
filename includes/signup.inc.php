<?php
if (isset($_POST['signup-submit'])) {

  require 'dbh.inc.php';

  $email = $_POST['mailuid'];

  if (empty($email)) {
    header("Location: ../signup.php?error=emptyfields&mailuid=".$email);
    exit();
  }
  else {
    $sql = "INSERT INTO emails (mailuid) VALUES ('$email')";
    $stmt = mysqli_stmt_init($conn);
    // mysqli_stmt_bind_param($stmt, "s", $email);
    // mysqli_stmt_execute($stmt);
  }
  if (mysqli_query($conn, $sql)) {
      echo "New record created successfully";
  }
  else{
      echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
  // mysqli_stmt_close($stmt);
  mysqli_close($conn);
}
else {
  echo system("/Users/titanmitchell/Documents/CPSC_Courses/CPSC353/CoronaVirus/webScrap.py");
  $command = escapeshellcmd('/Users/titanmitchell/Documents/CPSC_Courses/CPSC353/CoronaVirus/webScrap.py');
  $output = shell_exec($command);
  var_dump($output);
  echo $output;
  exit();
}
