<?php
require_once('car.php');
class UberPool extends Car{
    public $brand;
    public $model;

    public function __construct($license, $passenger, $driver, $brand, $model){
        parent::__construct($license, $passenger, $driver);
        $this->brand = $brand;
        $this->model = $model;
    }
}
?>