
#include "scheduler.h"

#define SERIAL_REFRESH_TIME_MS 1000
char c;

void serial_callback(){
  
  if (Serial.available() > 0) {
    c = Serial.read();
    // clear the serial buffer
    while(Serial.available()) {Serial.read();}
  }
  
  Serial.print("Hello world! "); Serial.println(c);

  // enter 's' to stop the serial callbacks
  if (c != 's'){
    run_later(serial_callback, SERIAL_REFRESH_TIME_MS);
  }
}


void setup(){
  initOS();
  blinkLED();
  run_later(serial_callback,1000); // wait until after Serial has finished init
  
  Serial.begin(115200);
  while (!Serial); // wait for Serial to finish startup
}

void loop(){  
  run();
}
