import java.util.ArrayList;
import java.util.Map;

class UberVan extends Car {
    Map<String, ArrayList<Map<String,Integer>>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    public UberVan(String license, Integer passengers, Account driver, Map<String, ArrayList<Map<String,Integer>>> typeCarAccepted, ArrayList<String> seatsMaterial) {
        super(license, passengers, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}