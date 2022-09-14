class Car {
    private Integer id;
    private String license;
    private Account driver;//Heredaré el nombre(o la clase) de account
    Integer passengers;//

    public Car(String license, Account driver) {//Parámetros Obligatorios
        this.license = license;
        this.driver = driver;
    }

    void printDataCar() {//Funcion de Imprimir los datos
        if(passengers != null){
            System.out.println("Licencia: " + license + "\nName Driver: " + driver.name + "\nPasajeros: " + passengers);
        }
    }

    public Integer getPassengers(){
        return passengers;
    }
    public void setPassengers(Integer passengers){
        if(passengers == 4){
            this.passengers = passengers;
        }
        else {
            System.out.println("Necesitas asignar 4 pasajeros");
        }
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
    
}