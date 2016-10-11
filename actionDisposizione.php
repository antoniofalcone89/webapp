<?


function prova(){
    // $file = $_POST['testo'];
    $myArray = $_REQUEST['arrayfiles'];
    echo "ciao";
    $fp = fopen('logDisp.txt', 'w');
    fwrite($fp, $myArray[1]);
    fclose($fp);
    // $out = shell_exec( "python plotModulo.py $file");
    // echo "$file";
    // $fp = fopen('logDisp.txt', 'w');
    // fwrite($fp, $out);
    // fclose($fp);
}

prova();
?>
