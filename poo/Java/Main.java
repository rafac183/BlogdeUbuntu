class Main {
    public static void main(String[] args) {
        System.out.println("Hola Mundo\n");//Print en Java

        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123", "a.herrera@gmail.com"), "Chevrolet", "Spark"); //Guardar datos en clases de otro archivo
        uberX.setPassengers(4);
        uberX.printDataCar();//Llamar funcion de otro archivo
        //uberX.passengers = 5;//como passengers esta en privado no lo muestra en otro paquete

        UberVan uberVan = new UberVan("FGH789", new Account("Rafael Contreras", "AND159", "rafa@gmail.com"));
        uberVan.setPassengers(6);
        uberVan.printDataCar();
    }
}