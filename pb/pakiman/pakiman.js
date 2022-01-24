class Pakiman { //acumula variables con atributos comunes para no clonarlos
    constructor(nombre, tipo, vida, ataque) {//es como funcion sin nombre //solo con this se añade variable
        this.imagen = new Image();
        this.nombre = nombre;
        this.tipo = tipo;
        this.vida = parseInt(vida);//no hace falta parseint y no hace falta las comillas abajo
        this.ataque = parseInt(ataque);

        this.imagen.src = imagenes[this.nombre];
    }
    hablar() {
        alert(this.nombre);
    }
    mostrar() {
        document.body.appendChild(this.imagen);
        document.write("<p>");        
        document.write("<strong>" + this.nombre + "</strong>" + "<br />");
        document.write("Vida: " + this.vida + "<br />");
        document.write("Tipo: " + this.tipo + "<br />");
        document.write("Ataque: " + this.ataque + "<br />");
        document.write("<p/>");
        document.write("<br /> <hr />"); //hr dibuja una linea separadora
    }
}