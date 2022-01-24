<?php
function places($condition = "", $question = "") {
  $weather = array("Bogota" => "cold", "Monteria" => "hot", "Medellin" => "mild");
  $ubication = array("Guajira" => "north", "Leticia" => "south", "Santander" => "east", "Antioquia" => "west");
  $tourist = array("Santa Maria" => "sea", "Villavicencio" => "plains", "Riohacha" => "Desert", "Quindío" => "valley");

  switch($condition) {
    case "weather":
      $search = $weather;
    break;
    case "ubication":
        $search = $ubication;
    break;
    case "tourist":
        $search = $tourist;
    break;
    default:
      echo "Welcome to Colombia";
  }
  echo "The Perfect Place for You Is ".array_search($question, $search);
}
places("weather", "cold");



