<?php 
require_once('payment.php');
class Cash extends Payment{
    public $amount;
    public $typeCard;

    public function __construct($id, $amount, $typeCard) {
        parent::__construct($id);
        $this->amount = $amount;
        $this->typeCard = $typeCard;
    }
}
?>