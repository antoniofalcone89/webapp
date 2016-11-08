/**
 * Created by Antonio on 21/09/16.
 */

function setSortable(){

    $( "#sortable1" ).sortable({
        placeholder: "ui-state-highlight"
    });
    $( "#sortable1" ).disableSelection();

    $( "#sortable2" ).sortable({
        placeholder: "ui-state-highlight"
    });
    $( "#sortable2" ).disableSelection();

}

function setImg(imgname){
    var ext = ".png";
    var fullImg = img.concat(ext);
    //alert(fullImg);
    if(squadra == 1){
        $('#sortable1').append('<li class="ui-state-default"><img src='+imgname+' /></li>');
    }
    else if(squadra == 2){
        $('#sortable2').append('<li class="ui-state-default"><img src='+imgname+' /></li>');
    }
}

function setImg2(imgname){
    imgname.slice(0,-1); //elimino l'ultimo carattere perchè c'è un / dopo il nome
    imgname = "imgGen/" + imgname;
    if(squadra == 1){
        $('#sortable1').append('<li class="ui-state-default"><img src='+imgname+' /></li>');
    }
    else if(squadra == 2){
        $('#sortable2').append('<li class="ui-state-default"><img src='+imgname+' /></li>');
    }

}

var img;

function myAjax (nomefile) {
    var testo = nomefile;
    var nomeimg;
    estensione = nomefile.split('.').pop().toLowerCase();
    if(estensione == "csv"){
        $.ajax( { type : 'POST',
            data : {testo},
            url  : 'action.php',              // <=== CALL THE PHP FUNCTION HERE.
            success: function ( data ) {
                img = testo.slice(0, -4);
                nomeimg = data;
                //alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
            },
            error: function (xhr, status, error) {
                // executed if something went wrong during call
                if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
            },
            complete: function (data) {
                setImg(nomeimg);
                $('.waiting').hide();
                //$("#heatmap1").replaceWith($("#heatmap1").clone());
                $("#firstimg1").closest('.gruppoinput1').children('p.nomefile').remove();
                $("#firstimg2").closest('.gruppoinput2').children('p.nomefile').remove();
            },
            beforeSend:function(){
                $('.waiting').show();
            }
        });
    }
    else{
        alert("Richiesto un file di tipo csv");
        //$("#heatmap1").replaceWith($("#heatmap1").clone());
        //$("#heatmap2").replaceWith($("#heatmap2").clone());
        $("#firstimg1").closest('.gruppoinput1').children('p.nomefile').remove();
        $("#firstimg2").closest('.gruppoinput2').children('p.nomefile').remove();
    }

}


//INFOGRAFICA DISTANZE REPARTI ATTACCO DIFESA
function distanze(filenames1, numfiles1) {
    var nomifiles = filenames1;
    var allcsv1 = 0;
    var nomeimg;

    if(numfiles1!=3){
        alert("Devi selezionare 3 file csv");
    }
    else{
        $.each(filenames1,function(index) {
            estensione = filenames1[index].split('.').pop().toLowerCase();
            if(estensione != "csv"){
                allcsv1 = 1;
            }
        });
        if(allcsv1 == 1){
            alert("Tutti i file devono essere di tipo .csv");
            $("#distanze1").replaceWith($("#distanze1").clone());
        }
        else{
            $.ajax( { type : 'POST',
                data : {arrayFiles: nomifiles},
                url  : 'actionDistanze.php',              // <=== CALL THE PHP FUNCTION HERE.
                success: function ( data ) {
                    nomeimg = data;
                    //alert( data );               // nome del file creato, restituito dal php
                },
                error: function (xhr, status, error) {
                    // executed if something went wrong during call
                    if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
                },
                complete: function (data) {
                    setImg2(nomeimg);
                    $('.waiting').hide();
                    $("#distanze1").replaceWith($("#distanze1").clone());
                    $("#distanze1").closest('.gruppoinputDistanze1').children('p.numfiles').remove();
                    $("#distanze2").closest('.gruppoinputDistanze2').children('p.numfiles').remove();
                },
                beforeSend:function(){
                    $('.waiting').show();
                }
            });
        }
    }

}

//INFOGRAFICA DISTANZE REPARTI ATTACCO DIFESA
function numPassaggi(filenames1, numfiles1, modulo) {
    var nomifiles = filenames1;
    var allcsv1 = 0;
    var nomeimg;

    if(numfiles1!=10){
        alert("Devi selezionare 10 file csv");
    }
    else{
        $.each(filenames1,function(index) {
            estensione = filenames1[index].split('.').pop().toLowerCase();
            if(estensione != "csv"){
                allcsv1 = 1;
            }
        });
        if(allcsv1 == 1){
            alert("Tutti i file devono essere di tipo .csv");
            $("#passaggi").replaceWith($("#passaggi1").clone());
        }
        else{
            $.ajax( { type : 'POST',
                data : {arrayFiles: nomifiles, modulo},
                url  : 'actionPassaggi.php',              // <=== CALL THE PHP FUNCTION HERE.
                success: function ( data ) {
                    nomeimg = data;
                    //alert( data );               // nome del file creato, restituito dal php
                },
                error: function (xhr, status, error) {
                    // executed if something went wrong during call
                    if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
                },
                complete: function (data) {
                    setImg2(nomeimg);
                    $('.waiting').hide();
                    $("#passaggi1").replaceWith($("#passaggi1").clone());
                    $("#passaggi1").closest('.gruppoinputNumPassaggi1').children('p.numfiles').remove();
                    $("#passaggi2").closest('.gruppoinputNumPassaggi2').children('p.numfiles').remove();
                },
                beforeSend:function(){
                    $('.waiting').show();
                }
            });
        }
    }

}

function lightSquadra(squadra){
    if(squadra == 1){
        $('#contenuto1').effect("highlight", {}, 1000);
    }
    else if(squadra == 2){
        $('#contenuto2').effect("highlight", {}, 1000);
    }
}



//INFOGRAFICA DISPOSIZIONE IN CAMPO 433
function disposizione433(filenames, numfiles, effettiva) {
    var nomifiles = filenames;
    var allcsv = 0;
    var nomeimg;

    if(numfiles!=10){
        alert("Devi selezionare 10 file csv");
    }
    else{
        $.each(filenames,function(index) {
            estensione = filenames[index].split('.').pop().toLowerCase();
            if(estensione != "csv"){
                allcsv = 1;
            }
        });
        if(allcsv == 1){
            alert("Tutti i file devono essere di tipo .csv");
            $("#disposizione1").replaceWith($("#disposizione1").clone());
        }
        else{
            $.ajax( { type : 'POST',
                data : {arrayFiles: nomifiles, effettiva},
                url  : 'actionDisposizione433.php',              // <=== CALL THE PHP FUNCTION HERE.
                success: function ( data ) {
                    nomeimg = data;
                    //alert( data );               // nome del file creato, restituito dal php
                },
                error: function (xhr, status, error) {
                    // executed if something went wrong during call
                    if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
                },
                complete: function (data) {
                    setImg2(nomeimg);
                    $('.waiting').hide();
                    $("#disposizione1").replaceWith($("#disposizione1").clone());
                    $("#disposizione1").closest('.gruppoinputDisposizione1').children('p.numfiles').remove();
                    $("#disposizione2").closest('.gruppoinputDisposizione2').children('p.numfiles').remove();

                    $("#disposizioneEff1").replaceWith($("#disposizioneEff1").clone());
                    $("#disposizioneEff1").closest('.gruppoinputDisposizioneEff1').children('p.numfiles').remove();
                    $("#disposizioneEff2").closest('.gruppoinputDisposizioneEff2').children('p.numfiles').remove();
                },
                beforeSend:function(){
                    $('.waiting').show();
                }
            });
        }
    }

}

//INFOGRAFICA DISPOSIZIONE IN CAMPO 352
function disposizione352(filenames, numfiles, effettiva) {
    var nomifiles = filenames;
    var allcsv = 0;
    var nomeimg;

    if(numfiles!=10){
        alert("Devi selezionare 10 file csv");
    }
    else{
        $.each(filenames,function(index) {
            estensione = filenames[index].split('.').pop().toLowerCase();
            if(estensione != "csv"){
                allcsv = 1;
            }
        });
        if(allcsv == 1){
            alert("Tutti i file devono essere di tipo .csv");
            $("#disposizione1").replaceWith($("#disposizione1").clone());
        }
        else{
            $.ajax( { type : 'POST',
                data : {arrayFiles: nomifiles, effettiva},
                url  : 'actionDisposizione352.php',              // <=== CALL THE PHP FUNCTION HERE.
                success: function ( data ) {
                    nomeimg = data;
                    //alert( data );               // nome del file creato, restituito dal php
                },
                error: function (xhr, status, error) {
                    // executed if something went wrong during call
                    if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
                },
                complete: function (data) {
                    setImg2(nomeimg);
                    $('.waiting').hide();
                    $("#disposizione1").replaceWith($("#disposizione1").clone());
                    $("#disposizione1").closest('.gruppoinputDisposizione1').children('p.numfiles').remove();
                    $("#disposizione2").closest('.gruppoinputDisposizione2').children('p.numfiles').remove();

                    $("#disposizioneEff1").replaceWith($("#disposizioneEff1").clone());
                    $("#disposizioneEff1").closest('.gruppoinputDisposizioneEff1').children('p.numfiles').remove();
                    $("#disposizioneEff2").closest('.gruppoinputDisposizioneEff2').children('p.numfiles').remove();
                },
                beforeSend:function(){
                    $('.waiting').show();
                }
            });
        }
    }

}


function removeCanvas(){
    $(".modal-body").empty();
}

function removeContent() {
    $('#contenuto').empty();
    $('#contenuto').append('<ul id="sortable" class="ui-sortable"> </ul>');
}

function removeSquadra1() {
    $('#contenuto1').empty();
    $('#contenuto1').append('<ul id="sortable1" class="ui-sortable"> </ul>');
    setSortable();
}

function removeSquadra2() {
    $('#contenuto2').empty();
    $('#contenuto2').append('<ul id="sortable2" class="ui-sortable"> </ul>');
    setSortable();
}

var squadra = 1;

function mostraBottoniSquadra2() {
    //$('#bottonisquadra1').hide();
    $('#bottonisquadra2').show();
    $('#bottoni_squadra1').hide();
    $('#bottoni_squadra2').show();
    $("#disposizione2").replaceWith($("#disposizione2").clone());

    lightSquadra(2);
    squadra = 2;
}

function cambiaSquadra(){
    if (squadra == 1){
        $('#bottonisquadra').html("Modifica la squadra 1");
        $('#bottoni_squadra1').hide();
        $('#bottoni_squadra2').show();
        //$("#disposizione2").replaceWith($("#disposizione2").clone());
        lightSquadra(2);
        squadra = 2;
    }
    else if(squadra == 2){
        $('#bottonisquadra').html("Modifica la squadra 2");
        $('#bottoni_squadra2').hide();
        $('#bottoni_squadra1').show();
        //$("#disposizione2").replaceWith($("#disposizione2").clone());
        lightSquadra(1);
        squadra = 1;
    }
}

function set433_1() {
    $('.gruppoinputDistanze1').show();
    $('.gruppoinputDistanze2').hide();

}

function set433_2() {
    $('.gruppoinputDistanze2').show();

}

function set352_1() {
    $('.gruppoinputDistanze1').hide();
}

function set352_2() {
    $('.gruppoinputDistanze2').hide();
}

function mostraBottoniSquadra1() {
    //$('#bottonisquadra2').hide();
    $('#bottonisquadra1').show();
    $('#bottoni_squadra2').hide();
    $('#bottoni_squadra1').show();
    $("#disposizione1").replaceWith($("#disposizione1").clone());
    lightSquadra(1);
    squadra = 1;
}

function captureCurrentDiv()
{
    html2canvas([document.getElementById('contenitore')], {
        onrendered: function(canvas)
        {
            var img = canvas.toDataURL()
            $.post("save.php", {data: img}, function (file) {
                window.location.href =  "download.php?path="+ file});
        }
    });
}

function captureSinglePlayer()
{
    html2canvas([document.getElementById('contenuto1')], {
        onrendered: function(canvas)
        {
            var img = canvas.toDataURL()
            $.post("save.php", {data: img}, function (file) {
                window.location.href =  "download.php?path="+ file});
        }
    });
}

function setTitle(){
    //var titolo = document.getElementById('title').value;
    if(squadra == 1){
        var title = $('#title').val();
        $('#sortable1').prepend('<li class="ui-state-default"><h1>'+title+'</h1></li>');
        $('#title').val('');
        $('#sortable1').css('cursor', 'default');
    }
    else if(squadra == 2){
        var title = $('#title2').val();
        $('#sortable2').prepend('<li class="ui-state-default"><h1>'+title+'</h1></li>');
        $('#title').val('');
        $('#sortable2').css('cursor', 'default');
    }
}

function setText(){
    //var testo = document.getElementById('text').value;
    if(squadra == 1){
        var testo = $('#text').val();
        $('#sortable1').append('<li class="ui-state-default"><h4>'+testo+'</h4></li>');
        $('#text').val('');
        $('#sortable1').css('cursor', 'default');
    }
    else if(squadra == 2){
        var testo = $('#text2').val();
        $('#sortable2').append('<li class="ui-state-default"><h4>'+testo+'</h4></li>');
        $('#text').val('');
        $('#sortable2').css('cursor', 'default');
    }
}

//PER AGGIUNGERE BOTTONI HEATMAP
var x = 1; //initlal text box count
function addElements(){
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".col-md-4"); //Fields wrapper

    if(squadra == 1){
        if(x < max_fields){ //max input box allowed
            x++;
            $('#firstimg1').after('<div class="gruppoinput1"><p class="lead" style="margin-bottom: 0;">Heatmap</p><label class="btn btn-default btn-info" style="margin-top: 8px">Browse <input type="file" style="display: none;" class="inputfile"/> </label> <button type="button" class="btn btn-outline-danger" disabled="disabled">Ok</button> <span id="remove_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </div>');
        }


        $(wrapper).on("click","#remove_field", function(){ //user click on remove text
            $(this).parent('div').remove(); x--;
        })
    }
    else if(squadra == 2){
        if(x < max_fields){ //max input box allowed
            x++;
            $('#firstimg2').after('<div class="gruppoinput2"><p class="lead" style="margin-bottom: 0;">Heatmap</p><label class="btn btn-default btn-info" style="margin-top: 8px">Browse <input type="file" style="display: none;" class="inputfile"/> </label> <button type="button" class="btn btn-outline-danger" disabled="disabled">Ok</button> <span id="remove_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </div>');
        }


        $(wrapper).on("click","#remove_field", function(){ //user click on remove text
            $(this).parent('div').remove(); x--;
        })
    }
}

//PER AGGIUNGERE ELEMENTI TESTO
var y = 1; //initlal text box count
function addText(){
    var max_fieldsY      = 10; //maximum input boxes allowed
    var wrapperY         = $(".col-md-4"); //Fields wrapper

    if(squadra == 1){
        if(x < max_fieldsY){ //max input box allowed
            y++;
            $('#firstInput1').after('<form class="form-inline" id="firstInput" style="margin-top: 8px;"><div class="form-group"><input type="text" class="form-control" id="text" placeholder="Testo"></div> <button type="button" class="btn btn-primary" id="inserisciTitolo" onclick="setText(text.value)">Ok</button> <span id="remove_text_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </form>');
        }

        $(wrapperY).on("click","#remove_text_field", function(){ //user click on remove text
            $(this).parent('form').remove(); y--;
        })
    }
    else if(squadra == 2){
        if(x < max_fieldsY){ //max input box allowed
            y++;
            $('#firstInput2').after('<form class="form-inline" id="firstInput" style="margin-top: 8px;"><div class="form-group"><input type="text" class="form-control" id="text" placeholder="Testo"></div> <button type="button" class="btn btn-primary" id="inserisciTitolo" onclick="setText(text.value)">Ok</button> <span id="remove_text_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </form>');
        }

        $(wrapperY).on("click","#remove_text_field", function(){ //user click on remove text
            $(this).parent('form').remove(); y--;
        })
    }

}
