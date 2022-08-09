<?php 
require_once('payment.php');
class Cash extends Payment{
    public $amount;
    public $email;

    public function __construct($id, $amount, $email) {
        parent::__construct($id);
        $this->amount = $amount;
        $this->email = $email;
    }
}
?>