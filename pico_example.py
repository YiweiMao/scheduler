
""" 
An example to flash two LEDs using asyncio
The method used is to have coros reschedule themselves.

Author: Yiwei Mao
Email: yiwei.mao@sydney.edu.au
"""

from machine import Pin
import uasyncio as asyncio

# create LED objects
builtin_led = Pin(25,Pin.OUT)
LED_TOGGLE_TIME_MS = 50

second_led  = Pin(16,Pin.OUT)
SECOND_LED_TOGGLE_TIME_MS = 200

# Create Tasks to be run asynchronously
def set_global_exception():
    """Allow for exception handling in event loop."""
    def handle_exception(loop, context):
        import sys
        sys.print_exception(context["exception"])
        sys.exit()
    loop = asyncio.get_event_loop()
    loop.set_exception_handler(handle_exception)

def reschedule_every_ms(t):
    """Decorator for a callback that will keep rescheduling itself."""
    def inner_decorator(cb):
        async def wrapped(*args, **kwargs):
            while True:
                await asyncio.sleep_ms(t)
                cb(*args, **kwargs)
        return wrapped 
    return inner_decorator

# create coros for blinking each LED
@reschedule_every_ms(LED_TOGGLE_TIME_MS)
def blink_deco():
    builtin_led.toggle()

@reschedule_every_ms(SECOND_LED_TOGGLE_TIME_MS)
def second_blink_deco():
    second_led.toggle()
    

# Add Coros into the Event Loop
async def main():
    set_global_exception() # Debug aid

    asyncio.create_task(blink_deco())
    asyncio.create_task(second_blink_deco())

    while True: # run forever
        await asyncio.sleep_ms(1000)

# Run the Event Loop
try:
    asyncio.run(main())
except KeyboardInterrupt: 
    print("Keyboard Interrupted")
except asyncio.TimeoutError: 
    print("Timed out")
finally:
    asyncio.new_event_loop()  # Clear retained state

