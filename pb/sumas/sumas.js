var txt = document.getElementById("texto");
var boton = document.getElementById("boton");
boton.addEventListener("click", click);
var num = Math.floor(Math.random());
var l = 2;
var result = document.getElementById("result");

function nroAleatorio(min, max) { //funcion variable aleatoria
    var result;
    result = Math.floor(Math.random() * (max - min + 1)) + min;
    return result
}
var minimo = {
    min: 0, 
    max: 100
};

function sumar(numeros) {
    for(var i = 0; i < l; i++) {
        numeros = numeros + (nroAleatorio(minimo.min, minimo.max));
    }
    return numeros;
}

result.innerHTML = "Esto dio " + sumar(num);
console.log(sumar(num));