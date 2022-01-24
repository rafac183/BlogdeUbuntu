int amarillo = 13;
int rojo = 7;
int azul = 5;
int ms = 300;

void setup() { // codigo para encender
  pinMod(amarillo, OUTPUTS);
}
void loop() { // codigo para correr
  digitalWrite(amarillo, HIGH);
  delay(ms);
  digitalWrite(amarillo, LOW);
  delay(ms);
  digitalWrite(rojo, HIGH);
  delay(ms);
  digitalWrite(rojo, LOW);
  delay(ms);
  digitalWrite(azul, HIGH);
  delay(ms);
  digitalWrite(azul, LOW);
  delay(ms);
}