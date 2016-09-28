/**
 * Created by Antonio on 21/09/16.
 */

function setImg(){
    var ext = ".png";
    var fullImg = img.concat(ext);
    //alert(fullImg);
    $('#sortable').append('<li class="ui-state-default"><img src='+fullImg+' /></li>');
}

var img;

function myAjax (nomefile) {
    var testo = nomefile;
    estensione = nomefile.split('.').pop().toLowerCase();
    if(estensione == "csv"){
        $.ajax( { type : 'POST',
            data : {testo},
            url  : 'action.php',              // <=== CALL THE PHP FUNCTION HERE.
            success: function ( data ) {
                img = testo.slice(0, -4);
                //alert( data );               // <=== VALUE RETURNED FROM FUNCTION.
            },
            error: function (xhr, status, error) {
                // executed if something went wrong during call
                if (xhr.status > 0) alert('got error: ' + status); // status 0 - when load is interrupted
            },
            complete: function (data) {
                setImg();
                $('.waiting').hide();
            },
            beforeSend:function(){
                $('.waiting').show();
            }
        });
    }
    else{
        alert("Richiesto un file di tipo csv");
    }

}

function removeCanvas(){
    $(".modal-body").empty();
}

function removeContent() {
    $('#contenuto').empty();
    $('#contenuto').append('<ul id="sortable"> </ul>');
}

function removeContent2() {
    $('.col-md-8').empty();
    $('.col-md-8').append('<div class="waiting"></div> <ul id="sortable"> </ul>');
    $('.waiting').hide();
}

function setTitle(){
    var titolo = document.getElementById('title').value;
    $('#sortable').prepend('<li class="ui-state-default"><h1>'+titolo+'</h1></li>');
    $('#title').val('');
    $('#sortable').css('cursor', 'default');
}

function setText(){
    var testo = document.getElementById('text').value;
    $('#sortable').append('<li class="ui-state-default"><h4>'+testo+'</h4></li>');
    $('#text').val('');
    $('#sortable').css('cursor', 'default');
}

var x = 1; //initlal text box count
function addElements(){
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".col-md-4"); //Fields wrapper


    if(x < max_fields){ //max input box allowed
        x++;
        $('#firstimg').after('<div class="gruppoinput"> <label class="btn btn-default btn-info" style="margin-top: 8px">Browse <input type="file" style="display: none;" class="inputfile"/> </label> <button type="button" class="btn btn-outline-danger" disabled="disabled">Ok</button> <span id="remove_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </div>');
    }


    $(wrapper).on("click","#remove_field", function(){ //user click on remove text
        $(this).parent('div').remove(); x--;
    })
}

var y = 1; //initlal text box count
function addText(){
    var max_fieldsY      = 10; //maximum input boxes allowed
    var wrapperY         = $(".col-md-4"); //Fields wrapper


    if(x < max_fieldsY){ //max input box allowed
        y++;
        $('#firstInput').after('<form class="form-inline" id="firstInput" style="margin-top: 8px;"><div class="form-group"><input type="text" class="form-control" id="text" placeholder="Testo"></div> <button type="button" class="btn btn-primary" id="inserisciTitolo" onclick="setText(text.value)">Ok</button> <span id="remove_text_field" class="glyphicon glyphicon-remove" aria-hidden="true" style="vertical-align: middle"></span> </form>');
    }

    $(wrapperY).on("click","#remove_text_field", function(){ //user click on remove text
        $(this).parent('form').remove(); y--;
    })
}
