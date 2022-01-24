var teclas = {
    UP: 38, DOWN: 40, RIGHT: 39, LEFT: 37, 
};
//evento para cuando presione una tecla del teclado seguido de la funcion
document.addEventListener("keydown", dibujarTeclado);
//enlace con html
var x = document.getElementById("dibujotes");
var papel = x.getContext("2d");
var x = 100;
var y = 100;
var style = "black";
//borde
dibujarlineas(style, 0, 1, 500, 1, papel);
dibujarlineas(style, 499, 1, 499, 500, papel);
dibujarlineas(style, 500, 499, 0, 499, papel);
dibujarlineas(style, 1, 0, 1, 500, papel);
//dibujar lineas
function dibujarlineas(color, xinicial, yinicial, xfinal, yfinal, lienzo) { //significa en donde dibujará
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.lineWidth = 3;
    lienzo.moveTo(xinicial ,yinicial);
    lienzo.lineTo(xfinal, yfinal);
    lienzo.stroke();
    lienzo.closePath();
}
//funcion del evento
function dibujarTeclado(event) {
    var colores = "red";
    var mov = 10;
//switch de cuando ocurra este evento
    switch (event.keyCode) {
        //en el caso de que ocurra esto...
        case teclas.UP:
            dibujarlineas(colores, x, y, x, y - mov, papel);
            //para que recuerde la variable
            y = y - mov;
        break;
        case teclas.DOWN:
            dibujarlineas(colores, x, y, x, y + mov, papel);
            y = y + mov;
        break;
        case teclas.RIGHT:
            dibujarlineas(colores, x, y, x + mov, y, papel);
            x = x + mov;
        break;
        case teclas.LEFT:
            dibujarlineas(colores, x, y, x - mov, y, papel);
            x = x - mov;
        //si no ocurre ninguno pasa esto...
        default:
            console.log("Ningun lado");
    }
}