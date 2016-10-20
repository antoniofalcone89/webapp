<?


function bb(){
    //$out = shell_exec( 'python my_script.py');
    $files = glob('imgGen/*'); // get all file names
    foreach($files as $file){ // iterate files
      if(is_file($file))
    unlink($file); // delete file
}
}

bb();
?>
