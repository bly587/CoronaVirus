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
  //$output = shell_exec("python3 webScrap.py");
  // $command = 'ls';
  // exec($command, $out, $status);
  // $command = escapeshellcmd('python3 /Users/titanmitchell/Documents/CPSC_Courses/CPSC353/CoronaVirus/webScrap.py');
  // $output = shell_exec($command);
  exec('/Users/titanmitchell/Documents/CPSC_Courses/CPSC353/CoronaVirus/webScrap.py');
  //var_dump($output);
  // echo $output;
  exit();
}
