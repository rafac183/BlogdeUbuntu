<?php
function places($condition = "", $question = "") {
  $weather = array("Bogota" => "cold", "Monteria" => "hot", "Medellin" => "mild");
  $ubication = array("Guajira" => "north", "Leticia" => "south", "Santander" => "east", "Antioquia" => "west");
  $tourist = array("Santa Maria" => "sea", "Villavicencio" => "plains", "Riohacha" => "Desert", "Quindío" => "valley");

  switch($condition) {
    case "weather":
      echo array_search($question, $weather);
    break;
    case "ubication":
      echo array_search($question, $ubication);
    break;
    case "tourist":
      echo array_search($question, $tourist);
    break;
    default:
      echo "Welcome to Colombia";
  }
}
places("weather", "hot");