//enlace con html
var x = document.getElementById("dibujito");
var lienzo = x.getContext("2d");
var lineas = 50;
var l = 0;
var xi, yi, xf, yf;
var colorcito = "black"

//funcion para dibujar
function dibujarlineas(xinicial, yinicial, xfinal, yfinal, color) {
    lienzo.beginPath();
    lienzo.stroke.Style = color;
    lienzo.moveTo(xinicial ,yinicial);
    lienzo.lineTo(xfinal, yfinal);
    lienzo.stroke();
    lienzo.closePath();
}

//borde del canvas
dibujarlineas(0, 1, 500, 1, colorcito);
dibujarlineas(499, 1, 499, 500  , colorcito);
dibujarlineas(500, 499, 0, 499, colorcito);
dibujarlineas(1, 0, 1, 500, colorcito);

//primero
for(l = 0; l < lineas; l++) {
    xf = 10 * l;
    yf = 0;
    dibujarlineas(250, 250, xf, yf, colorcito);
}
//segundo
for(l = 0; l < lineas; l++) {
    xf = 500;
    yf = 10 * l; 
    dibujarlineas(250, 250, xf, yf, colorcito);
}
//tercero
for(l = 0; l < lineas + 1; l++) {
    xf = 10 * l;
    yf = 500;
    dibujarlineas(250, 250, xf, yf, colorcito);
}
//cuarto
for(l = 0; l < lineas; l++) {
    xf = 0;
    yf = 10 * l; 
    dibujarlineas(250, 250, xf, yf, colorcito);
}
//curva1
for(l = 0; l < lineas; l++) {
    yi = 10 * l;
    xf = 10 * (l + 1);
    dibujarlineas(0, yi, xf, 500, colorcito);
}
//curva2
for(l = 0; l < lineas; l++) {
    xi = 10 * l;
    yf = 500 - (l * 10);
    dibujarlineas(xi, 500, 500, yf, colorcito);
}
//curva3
for(l = 0; l < lineas; l++) {
    yi = 500 - (l * 10);
    xf = 500 - (l * 10);
    dibujarlineas(500, yi, xf, 0, colorcito);
}
//curva4
for(l = 0; l < lineas; l++) {
    xi = 500 - (l * 10);
    yf = 10 * (l + 1);
    dibujarlineas(xi, 0, 0, yf, colorcito);
}