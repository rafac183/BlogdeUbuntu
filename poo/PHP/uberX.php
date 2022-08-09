<?php
require_once("car.php");
class UberX extends Car{
    public $brand;
    public $model;

    public function __construct($license, $passegers, $driver, $brand, $model){
        parent::__construct($license, $passegers, $driver);
        $this->brand = $brand;
        $this->model = $model;
    }
}
?>