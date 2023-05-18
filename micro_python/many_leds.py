from machine import Pin
import utime

led_00 = Pin(25, Pin.OUT)
led_01 = Pin(10, Pin.OUT)
led_02 = Pin(11, Pin.OUT)
led_03 = Pin(12, Pin.OUT)
led_04 = Pin(13, Pin.OUT)
led_05 = Pin(14, Pin.OUT)
led_06 = Pin(15, Pin.OUT)
leds = [led_00, led_01, led_02, led_03, led_04, led_05, led_06]

# initializing
for led in leds:
        led.value(0)

# sweep through leds
while True:
    for led in leds:
        led.toggle()
        utime.sleep(0.1)