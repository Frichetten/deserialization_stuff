<?php
  class state_object {
    public $state_data = "";

    function __destruct() {
      file_put_contents("state_data.php", $this->state_data);
      print "Destroying Object: " . $this->state_data;
    }
  }

  $state = $_GET['state'];
  
  print "File: " . $state . "<br><br>";

  unserialize($state);

?>
