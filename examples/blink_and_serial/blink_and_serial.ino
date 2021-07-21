
#include "scheduler.h"

#define SERIAL_REFRESH_TIME_MS 500
char c;

void serial_callback(){
  // enter 's' to stop the serial callbacks
  if (c != 's'){
    run_later(serial_callback, SERIAL_REFRESH_TIME_MS);
  }
  
  if (Serial.available() > 0) {
    c = Serial.read();
    Serial.flush();
  }
  
  Serial.print("Hello world! "); Serial.println(c);
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




