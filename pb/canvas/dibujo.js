//enlace con html
var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");
//funcion de dibujar
function dibujarLineas(color, xinicial, yinicial, xfinal, yfinal) {
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(xinicial, yinicial);
    lienzo.lineTo(xfinal, yfinal);
    lienzo.stroke();
    lienzo.closePath();
}
dibujarLineas("blue", 0, 0, 300, 300);
dibujarLineas("red", 300, 0, 0, 300);
dibujarLineas("green", 150, 0, 150, 300);
dibujarLineas("yellow", 0, 150, 300, 150);
dibujarLineas("pink", 75, 0, 225, 300);
dibujarLineas("orange", 225, 0, 75, 300);
dibujarLineas("#AAAAFF", 0, 75, 300, 225);
dibujarLineas("black", 0, 225, 300, 75);
