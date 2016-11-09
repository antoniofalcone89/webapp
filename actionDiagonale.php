<?


function bb(){
    //$out = shell_exec( 'python my_script.py');
    $file = $_POST['testo'];
    $out = shell_exec( "python diagonale.py $file");
    echo $out;
    $fp = fopen('log.txt', 'w');
    fwrite($fp, $out);
    fclose($fp);
}

bb();
?>
