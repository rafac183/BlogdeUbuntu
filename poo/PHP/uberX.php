<?php
class UberX extends Car {
    public $brand;
    public $model;

    public function __construc($license, $passengers, $driver) {
        parent::__construc
        $this->license = $license;
        $this->passengers = $passengers;
        $this->driver = $driver;
    }
}
?>