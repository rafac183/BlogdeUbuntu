//cuadro de texto
var txt = document.getElementById("textoLineas");
var boton = document.getElementById("botoncito");
//boton y efeccto del click del boton seguido de la funcion
boton.addEventListener("click", dibujoPorClick);
//enlace con html
var x = document.getElementById("dibujitos");
var ancho = x.width;
var lienzo = x.getContext("2d");


function dibujarlineas(xinicial, yinicial, xfinal, yfinal, color) {
    lienzo.beginPath();
    lienzo.stroke.Style = color;
    lienzo.moveTo(xinicial ,yinicial);
    lienzo.lineTo(xfinal, yfinal);
    lienzo.stroke();
    lienzo.closePath();
}

//funcion de dibujar apenas presione el boton
function dibujoPorClick() {
    //parceint transforma texto a numero entero
    var xyz = parseInt(txt.value);
    var lineas = xyz;
    var l = 0;
    var xi, yi, xf, yf;
    var colorcito = "black"
    var espacio = ancho / lineas

    //curva1
    for(l = 0; l < lineas; l++) {
        yi = espacio * l;
        xf = espacio * (l + 1);
        dibujarlineas(0, yi, xf, 500, colorcito);
    }


    dibujarlineas(0, 1, 500, 1, colorcito);
    dibujarlineas(499, 1, 499, 500  , colorcito);
    dibujarlineas(500, 499, 0, 499, colorcito);
    dibujarlineas(1, 0, 1, 500, colorcito);
}