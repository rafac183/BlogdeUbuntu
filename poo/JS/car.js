var result = document.getElementById("result");
class Car {
    constructor(license, passengers, driver) {
        this.id;
        this.license = license;
        this.driver = driver;
        this.passengers = passengers;
    }
    printDataCar() {
        result.innerHTML = "Nombre del Conductor: " + this.driver.name + "<br />Documento del Conductor: " + this.driver.document + "<br />Pasajeros: " + this.passengers + "<br />Licencia: " + this.license
        console.log(this.driver.name);
        console.log(this.driver.document); 
        console.log(this.passengers);
        console.log(this.license);       
    }
}

