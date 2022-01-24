var numeroso = 100;
var l = 1;
var d = false;

for(l; l <= numeroso; l++) {
    d = false;
    if(esDivisible(l, 3)) { //%= Saca el residuo de la division
        document.write("Fizz");
        d = true; 
    }
    if(esDivisible(l, 5)) {
        document.write("Buzz");
        d = true;
    }
    if(!d) { //!= es NO
        document.write(l);
    }
    document.write("<br />");
}

function esDivisible(num, divisor) {
    if(num % divisor == 0){
        return true
    }
    else {
        return false
    }
}