//Primera forma
var numeros = 100;
var i = 1;

for(i; i <= numeros; i++) {
    d = false;
    if(i % 3 == 0) { //%= Saca el residuo de la division
        document.write("Fizz");
    }
    if(i % 5 == 0) {
        document.write("Buzz");
    }
    if(i % 3 != 0 && i % 5 != 0) { //!= es NO
        document.write(i);
    }
    document.write("<br />");
}

document.write("<br/>" + "<br/>" + "<br/>")

//Segunda Forma
var numeroso = 100;
var l = 1;
var d = false;

for(l; l <= numeroso; l++) {
    d = false;
    if(l % 3 == 0) { //%= Saca el residuo de la division
        document.write("Fizz");
        d = true; 
    }
    if(l % 5 == 0) {
        document.write("Buzz");
        d = true;
    }
    if(!d) { //!= es NO
        document.write(l);
    }
    document.write("<br />");
}