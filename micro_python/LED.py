import machine
import utime

#led_onboard = machine.Pin(25, machine.Pin.OUT)
led_red = machine.Pin(15, machine.Pin.OUT)
led_green = machine.Pin(14, machine.Pin.OUT)

while True:
    #led_onboard.value(1)
    led_red.value(1)
    led_green.value(0)
    utime.sleep(1)
    
    #led_onboard.value(0)
    led_red.value(0)
    led_green.value(1)
    utime.sleep(1)