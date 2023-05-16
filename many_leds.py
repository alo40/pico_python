import machine
import utime

led_00 = machine.Pin(25, machine.Pin.OUT)
led_01 = machine.Pin(10, machine.Pin.OUT)
led_02 = machine.Pin(11, machine.Pin.OUT)
led_03 = machine.Pin(12, machine.Pin.OUT)
led_04 = machine.Pin(13, machine.Pin.OUT)
led_05 = machine.Pin(14, machine.Pin.OUT)
led_06 = machine.Pin(15, machine.Pin.OUT)
leds = [led_00, led_01, led_02, led_03, led_04, led_05, led_06]

# initializing
for led in leds:
        led.value(0)

# sweep through leds
while True:
    for led in leds:
        led.toggle()
        utime.sleep(0.1)