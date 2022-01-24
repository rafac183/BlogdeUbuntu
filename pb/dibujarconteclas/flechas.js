//enlace con html
var x = document.getElementById("dibujotes");
var papel = x.getContext("2d");
var lineas = 50;
var l = 0;
var xi, yi, xf, yf;
var style = "blue"
//variable con variables por dentro
var teclas = {
    UP: 38, DOWN: 40, RIGHT: 39, LEFT: 37, 
};
//evento para cuando presione y suelte una tecla del teclado
document.addEventListener("keyup", dibujarTeclado);
//funcion de dibujar
function dibujarlineas(color, xinicial, yinicial, xfinal, yfinal, lienzo) {
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 3;
    lienzo.moveTo(xinicial ,yinicial);
    lienzo.lineTo(xfinal, yfinal);
    lienzo.stroke();
    lienzo.closePath();
}
//borde
dibujarlineas(style, 0, 1, 500, 1, papel);
dibujarlineas(style, 499, 1, 499, 500, papel);
dibujarlineas(style, 500, 499, 0, 499, papel);
dibujarlineas(style, 1, 0, 1, 500, papel);
dibujarlineas("brown", 150, 150, 100, 100, papel);

//funcion de cada vez que presione y suelte una tecla se ejecute
function dibujarTeclado(event) {
    //enlace la funcion con la caracteristica sacada del console.log en las 4
    if(event.keyCode == teclas.UP) {
        console.log("Vamo pa Arriba!");
    }
    else if (event.keyCode == teclas.DOWN) {
        console.log("Vamo pa Abajo!");
    }
    else if (event.keyCode == teclas.LEFT) {
        console.log("Vamo para la Izquierda!");
    }
    else if (event.keyCode == teclas.RIGHT) {
        console.log("Vamo para la Derecha!");
    }
    else {
        console.log("No Vamos para ningun lado :c");
    }
}
