<?php
class AnyClass {
	function __destruct() {
		echo $this->data;
	}
}

file_exists('phar://test.phar');

?>
