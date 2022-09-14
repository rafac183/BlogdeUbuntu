import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, ArrayList<Map<String,Integer>>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    public UberVan(String license, Account driver, Map<String, ArrayList<Map<String,Integer>>> typeCarAccepted, ArrayList<String> seatsMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
    //Cree esto para no complicarme con los arrays
    public UberVan(String license, Account driver) {
        super(license, driver);
    }
    //Polimorfismo para sobre escribir cosas para que hagas otras cosas
    @Override
    public void setPassengers(Integer passengers) {
        if(passengers == 6){
            this.passengers = passengers;
        }
        else{
            System.out.println("Necesitas asignar 6 pasajeros");
        }
    }
}