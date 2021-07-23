# scheduler
> The simplest C task scheduler for microcontrollers (Arduino)

Write asynchronous code for Arduino! Read my blog post to learn more about why you may want to incorporate async into your microcontroller code including Raspberry Pi Pico (using `uasyncio`). 
https://yiweimao.github.io/blog/async_microcontroller/

You only need to know ***one*** function and that is `run_later` which schedules a callback function to be run at a later time. The callback function must be of type `void` with no arguments. 

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

Run `initOS` before scheduling any tasks and fill up the scheduler before you run the even loop; for example, within the `void setup()` block. See the examples folder for a blink and serial sketch using this scheduler.

To run the event loop, end your sketch with
```c
void loop() {
  run();
}
```

### A Note on Other Schedulers

There are other schedulers for Arduino. See [a list of five](https://all3dp.com/2/best-arduino-operating-system/) including [FreeRTOS](https://freertos.org/) and [CoopThreads](https://github.com/pstolarz/CoopThreads). The closest implementation to what is present here is probably [TaskManagerIO](https://github.com/davetcc/TaskManagerIO). 

All of these have more featured APIs if you want more advanced features other than the simplistic `run_later` call. 