class Car {
    Integer id;
    String license;
    Account driver;//Heredaré el nombre(o la clase) de account
    Integer passengers;//

    public Car(String license,Integer passengers, Account driver) {//Parámetros Obligatorios
        this.license = license;
        this.passengers = passengers;
        this.driver = driver;
    }

    void printDataCar() {//Funcion de Imprimir los datos
        System.out.println(" \nLicencia: " + license + "\nName Driver: " + driver.name + "\nPasajeros: " + passengers + "\n");
    }
}