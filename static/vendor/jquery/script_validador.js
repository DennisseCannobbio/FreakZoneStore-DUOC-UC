$(function(){

    submitFormsCred = function(){
        if(validacion() && validacion_credito()){ // envia si las validaciones son true
            console.log("nop");
            succes();
            setTimeout(
                function(){
                    document.getElementById("form1").submit();
                    document.getElementById("formPayCred").submit();
                    location.href = "Inicio.html" // te envia a la pagina principal

                },5000);
        }
        else{
            error();
        }
        
        }
    submitFormsDebt = function(){
        if(validacion() && validacion_debito()){ // envia si las validaciones son true
            console.log("nop");
            succes();
            setTimeout(
                function(){
                    document.getElementById("form1").submit();
                    document.getElementById("formPayDebt").submit();
                    location.href = "Inicio.html" // te envia a la pagina principal
                },5000);
        }
        else{
            error();
        }
        
        }
    resetAll = function(){
        document.getElementById("form1").reset();
        document.getElementById("formPayCred").reset();
        document.getElementById("formPayDebt").reset();
    }

    terms = function() {
        alert("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam fringilla porta purus. Nulla non tortor turpis. Ut nec tortor eget erat laoreet condimentum. In iaculis lacinia quam eget tempor. Nulla ante massa, tempor et accumsan eget, congue ornare enim. Sed ullamcorper erosquis ex fringilla, eu tempor nisi euismod. Duis sit amet purus nec nisi sagittis facilisis vel id diam"); 
    }


    // validacion de la targeta de credito

    function validacion_credito(){
        var form = document.forms.formPayCred;
        if(!form[1].validity.valid){
            console.log("nop");
            form[1].focus();
            return false;
        }
        if(!form[2].validity.valid){
            console.log("nop");
            form[2].focus();
            return false;
        }
        if(!form[3].validity.valid){
            console.log("nop");
            form[3].focus();
            return false;
        }
        if(!form[4].validity.valid){
            console.log("nop");
            form[4].focus();
            return false;
        }
        return true;
    }


    // validacion de la targeta de debito

    function validacion_debito(){
        
        var form = document.forms.formPayDebt;
        if(!form[1].validity.valid){
            console.log("nop");
            form[1].focus();
            return false;
        }
        if(!form[2].validity.valid){
            console.log("nop");
            form[2].focus();
            return false;
        }
        if(!form[3].validity.valid){
            console.log("nop");
            form[3].focus();
            return false;
        }
        if(!form[4].validity.valid){
            console.log("nop");
            form[4].focus();
            return false;
        }
        return true;
        
    }
    
    // Validacion del formulario de la informacion del usuario

    function validacion(){
        var form = document.forms.form1;
        if(!form[1].validity.valid){
            console.log("nop");
            form[1].focus();
            return false;
        }

        if(!form[2].validity.valid){
            console.log("nop");
            form[2].focus();
            return false;
        }
        
        if(!form[3].validity.valid){
            console.log("nop");
            form[3].focus();
            return false;
        }
        if(!form[4].validity.valid){
            console.log("nop");
            form[4].focus();
            return false;
        }
        if(!form[6].validity.valid){
            console.log("nop");
            form[6].focus();
            return false;
        }
        if(!form[7].validity.valid){
            console.log("nop");
            form[7].focus();
            return false;
        }
        if(!form[8].validity.valid){
            console.log("nop");
            form[8].focus();
            return false;
        }
        if(!form[11].validity.valid){
            console.log("nop");
            form[11].focus();
            return false;
        }
        if(!form[13].validity.valid){
            console.log("nop");
            form[13].focus();
            return false;
        }
        if(!form[14].validity.valid){
            console.log("nop");
            form[14].focus();
            return false;
        }
        if(!form[17].validity.valid){
            console.log("nop");
            form[17].focus();
            return false;
        }
        if(!form[18].validity.valid){
            console.log("nop");
            form[18].focus();
            return false;
        }
        return true;

    }


    // Funcion que muestra mensaje error o exito del envio, ademas de mover la pagina al mensaje
    function error(){
        $('#error').show(200);
        $('html,body').animate({
            scrollTop: $('#error').offset().top
        },2000);
    }

    function succes(){
        $('#succes').show(200);
        $('html,body').animate({
            scrollTop: $('#succes').offset().top
        },2000);
    }

});