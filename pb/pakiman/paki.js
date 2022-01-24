var imagenes = [];//asi se añade a un array 
imagenes["Cauchin"] = "imagenes/cauchin.png";
imagenes["Pokacho"] = "imagenes/pokacho.png";
imagenes["Tocinauro"] = "imagenes/tocinauro.png";
console.log(imagenes);

/*var imagenes = {   esto es lo mismo
    cauchin = imagenes/cauchin.png
};*/

var pakimanes = [];
pakimanes.push(new Pakiman("Cauchin", "Tierra", "100", "30"));
pakimanes.push(new Pakiman("Pokacho","Agua", "80", "50"));
pakimanes.push(new Pakiman("Tocinauro","Fuego", "120", "40"));
/*pakimanes.push(tocinardo);asi se sube una variable al array sin los corchetes*/



/*var tocinauro = new Pakiman("Tocinauro","Fuego", "120", "40");...para que esto ocurra tengo que construir la clase con constructor*/
//console.log(cauchin, pokacho, tocinauro);
/*cauchin.hablar(); asi se invoca una funcion con clases*/
for(var pakin in pakimanes) {
    pakin.mostrar();
}