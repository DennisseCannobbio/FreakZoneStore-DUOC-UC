$(function(){


    $('ul.parent > li').hover(function(){ // hace que el menu baje cuando este el raton encima
        $(this).find('ul.child').show(200);

    },function(){
        $(this).find('ul.child').hide(200);
    });

    $('ul.child > li').hover(function(){ // se cambia el color del fondo cuando el mouse pasa por encima
        $(this).css("background-color","#131c1e");
    },function(){
        $(this).css("background-color","rgb(189, 181, 181)");
        
    });

    function loadCart(){
        if (typeof(Storage) !== "undefined") {
          if(localStorage.cart) {
            document.getElementById("cart").innerHTML = "Carrito (" + localStorage.cart + ")";
          } else {
            document.getElementById("cart").innerHTML = "Carrito (0)";
          }
        } else {
          document.getElementById("result").innerHTML = "Carrito (No hay storage)";
        }
    };

    //   function loadCart(){
    //     if(localStorage.cart != null) {
    //         document.getElementById("cart").innerHTML = "Carrito (" + localStorage.cart + ")";
    //     }
    //     else {
    //         document.getElementById("cart").innerHTML = "Carrito (0)"
    //     }
    // }

});