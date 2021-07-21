# scheduler
> The simplest C task scheduler for microcontrollers

You only need to know **one** function and that is `run_later` which schedules a callback function to be run at a later time. The callback function must be of type `void` with no arguments. 

To create a task that reschedules itself, simply call `run_later` on itself with a specified wait time. For example, this is how the blink function is written. 

```c
void blinkLED(){
    short toggle_delay = 250; // ms
    run_later(blinkLED, toggle_delay);

    pinMode(LED_BUILTIN,OUTPUT);
    digitalWrite(LED_BUILTIN,!digitalRead(LED_BUILTIN));
}
```

After you call `blinkLED`, the builtin LED will continue to blink in the background and you will have clock cycles to run other code using `run_later`. 
