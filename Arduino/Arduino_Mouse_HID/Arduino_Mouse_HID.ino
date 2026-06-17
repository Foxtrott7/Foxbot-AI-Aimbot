#include <Mouse.h>

void setup() {
  Serial.begin(115200); 
  
  Mouse.begin();
}

void loop() {
  if (Serial.available() >= 3) {
    int8_t x = Serial.read();
    int8_t y = Serial.read();
    int8_t click_state = Serial.read();
    
    if (x != 0 || y != 0) {
      Mouse.move(x, y, 0);
    }
    
    if (click_state == 1) {
      Mouse.click(MOUSE_LEFT);
    }
  }
}