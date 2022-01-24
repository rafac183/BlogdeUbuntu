class Cajero {
    constructor (v, c) {
        this.valor = v;
        this.cantidad = c;
    }
}

var txt = document.getElementById("dinero");
var boton = document.getElementById("botoncito");
boton.addEventListener("click", sacaDinero);
var result = document.getElementById("result");
var caja = [];
var entregado = [];
caja.push(new Cajero(100, 20));
caja.push(new Cajero(50, 50));
caja.push(new Cajero(20, 30));
caja.push(new Cajero(10, 40));
caja.push(new Cajero(5, 25));
var dinero = 0
var div = 0;
var papeles = 0;

function sacaDinero() {
    dinero = parseInt(txt.value);
    for(var bi of caja) {
        if(dinero > 0) {
            div = Math.floor(dinero / bi.valor);

            if(div > bi.cantidad) {
                papeles = bi.cantidad;
            }

            else {
                papeles = div;
            }
            entregado.push( new Cajero(bi.valor, papeles));
            dinero = dinero - (bi.valor * papeles);
        }
    }
    if (dinero > 0) {
        result.innerHTML = "No hay mas Fondos :("; /*innerHTML(es una variable no una funcion) usa el id extraido de html e inserta el texto  sin sobreescribir el JS, lo escribe en donde esta el id, ess como un document pero mejor*/
    }
    else {
        for (var e of entregado) {
            if (e.cantidad == 1) {
                result.innerHTML = result.innerHTML + e.cantidad + " Billete de $ " + e.valor + "<br />"; // si pongo solo un innert mostrara un solo billete , si son los 2 concatenara el valor anterior que tenia
            }
            else if (e.cantidad > 1){
                result.innerHTML += e.cantidad + " Billetes de $ " + e.valor + "<br />"; //+= indica que "suma lo anterior a esto tambien" es lo mismo que lo de arriba
            }
        }    
    }
}


/*Cuando ocurre todo el codigo de JS ocurre un evento llamado oneload y cierra el js, y si coloco un document y sobreescribe al html*/

