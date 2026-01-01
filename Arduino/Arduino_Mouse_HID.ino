#include <Mouse.h>

// Wir definieren ein Start-Byte zur Sicherheit, falls die Verbindung mal hakt
void setup() {
  // Hohe Baudrate für minimale Verzögerung (muss mit Python übereinstimmen)
  Serial.begin(115200); 
  
  // Initialisiert die USB-Maus-Funktion
  Mouse.begin();
}

void loop() {
  // Wir warten, bis genau 2 Bytes (X-Bewegung und Y-Bewegung) im Puffer liegen
  if (Serial.available() >= 2) {
    // signed char (int8_t) liest Werte von -128 bis 127
    int8_t x = Serial.read();
    int8_t y = Serial.read();
    
    // Führt die physische Mausbewegung aus
    // Mouse.move(x, y, wheel)
    Mouse.move(x, y, 0);
  }
}