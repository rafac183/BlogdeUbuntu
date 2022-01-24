var vp = document.getElementById("villaplatzi");
var hoja = vp.getContext("2d");//dimenciones del canvas
var c = nroAleatorio(2, 10);
var t = nroAleatorio(1, 9);
var d = nroAleatorio(3, 11);


//inicia en falso
var mapa = {
    url: "imagenes/tile.png", //enlace
    cargaOK: false
}
mapa.imagen = new Image(); //crear objetos
mapa.imagen.src = mapa.url;  //indico que la fuente de la imagen es..., despues de crear imagen
mapa.imagen.addEventListener("load", cargarmapa); //se dispara un evento de carga

var vaca = {
    url: "imagenes/vaca.png",
    cargaOK: false
};
vaca.imagen = new Image();//crea donde almacenar la imagen traida
vaca.imagen.src = "imagenes/vaca.png"; //enlazado directamente, url de la imagen creada
vaca.imagen.addEventListener("load", cargarvaca);

var pollo = {
    url: "imagenes/pollo.png",
    cargaOK: false
};
pollo.imagen = new Image();
pollo.imagen.src = pollo.url
pollo.imagen.addEventListener("load", cargarpollo);

var cerdo = {
    url: "imagenes/cerdo.png",
    cargaOK: false
};
cerdo.imagen = new Image();
cerdo.imagen.src = cerdo.url
cerdo.imagen.addEventListener("load", cargarcerdo);

function cargarmapa() { //si el mapa = true ejecuta la funcion dibujar
    mapa.cargaOK = true;
    dibujar();
}
function cargarvaca() {
    vaca.cargaOK = true;
    dibujar();
}
function cargarpollo() {
    pollo.cargaOK = true;
    dibujar();
}
function cargarcerdo() {
    cerdo.cargaOK = true;
    dibujar();
}

function dibujar() {
    var i = 0;
    var xey = {
        xx: 0, yy: 7 
    };

    if(mapa.cargaOK == true) {
        hoja.drawImage(mapa.imagen, 0, 0);//esto primero se coloca la imagen creada, luego las coordenadas desde donde empezara a dibujar
    }
    if(vaca.cargaOK == true) {
        for(i=0; i < c; i++){
            var x = nroAleatorio(xey.xx ,xey.yy);//coloco la variable aqui por que se que la vaca carga sin problemas
            var y = nroAleatorio(xey.xx ,xey.yy);
            var x = x * 60;
            var y = y * 60;
            hoja.drawImage(vaca.imagen, x, y);
            console.log(c);
        }
    }
    if(pollo.cargaOK == true) {
        for(i=0; i < t; i++) {
            var z = nroAleatorio(xey.xx, xey.yy);
            var w = nroAleatorio(xey.xx, xey.yy);
            var z = z * 60;
            var w = w * 60;
            hoja.drawImage(pollo.imagen, z, w);
            console.log(t);
        }
    }
    if(cerdo.cargaOK == true) {
        for(i=0; i < d; i++) {
            var a = nroAleatorio(xey.xx, xey.yy);
            var b = nroAleatorio(xey.xx, xey.yy);
            var b = b * 60;
            var a = a * 60;
            hoja.drawImage(cerdo.imagen, b, a);
            console.log(d);
        }
    }
}




function nroAleatorio(min, max) { //funcion variable aleatoria
    var result;
    result = Math.floor(Math.random() * (max - min + 1)) + min;
    return result
}


//Numeros Aleatorios//
var i = 0;
var n = 10;
var f = 11;
//for de numeros aleatorios
for(i = 0; i <= n; i++) {
    if(i < n) {
        var z = nroAleatorio(50, 200);
        document.write(z + ", ");
    }
    else if(i = n) {
        document.write(z + ".");
    }
}
        
