//prompt es como el alert pero con cuadro de texto
var result = document.getElementById("result");
var usuario = prompt("Cual es tu peso?");
var planeta = parseInt(prompt("Elige tu planeta\n1 es Marte y 2 es Jupiter"));
var peso = parseInt(usuario);
var gMarte = 3.7;
var gTierra = 9.8;
var gJupiter = 24.8;
var pesoFinal;
var nombre = "";
if(planeta == 1) {
    pesoFinal = (peso * gMarte) / gTierra;
    nombre = "Marte"
}
else if(planeta ==2) {
    pesoFinal = (peso * gJupiter) / gTierra;
    nombre = "J&uacutepiter"
}
else {
    pesoFinal = 4000000
    nombre = "Krypton"
}
pesoFinal = parseInt(pesoFinal)
/*strong usa negritas
br es como un enter
*/
result.innerHTML += "Tu peso en " + nombre + " es " + pesoFinal + "<strong>Kg</strong>";