<?


function prova(){
    // $file = $_POST['testo'];
    $myArray = $_REQUEST['arrayFiles'];
    json_encode($myArray);

    exec( "python distanzaAttDif.py $myArray[0] $myArray[1] $myArray[2]",  $output, $ret_code);
    //$out = shell_exec( "python plotModulo.py $myArray[0] $myArray[1] $myArray[2] $myArray[3] $myArray[4] $myArray[5] $myArray[6] $myArray[7] $myArray[8] $myArray[9] $myArray[10]");

    $fp = fopen('logDistanze.txt', 'w');
    fwrite($fp, $output[0]);
    fclose($fp);
    echo $output[0]; //invio il nome del file che mi ha dato lo script python al javascript
    // $out = shell_exec( "python plotModulo.py $file");
    // $fp = fopen('logDisp.txt', 'w');
}
prova();
?>
