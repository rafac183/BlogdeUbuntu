<?php
require_once('account.php');
class Car {
    public $id;
    public $license;
    public $driver;
    public $passengers;

    public function __construct($license, $passengers, $driver) {
        $this->license = $license;
        $this->passengers = $passengers;
        $this->driver = $driver;
    }
    public function printDataCar() {
        echo "Licencia: ", $this->license, "<br/>Driver: ", $this->driver->name, "<br/>Pasajeros: ", $this->passengers, "<br/>";    
    }

}
?>