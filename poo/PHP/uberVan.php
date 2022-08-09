<?php
require_once('car.php');
class UberVan extends Car{
    public $typeCarAccepted = array();
    public $seatsMaterial = array();

    public function __construct($license, $passengers, $driver, $typeCarAccepted, $seatsMaterial){
        parent::__construct($license, $passengers, $driver);
        $this->typeCarAccepted = $typeCarAccepted;
        $this->seatsMaterial = $seatsMaterial;
    }
}
?>