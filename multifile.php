<?php
if(isset($_POST['ok']))
   foreach ($_FILES['file']['name'] as $filename) {
    echo $filename.'<br/>';
}
?>