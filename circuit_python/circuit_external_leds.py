"""
Example for pico using circuit pythin.
Many external LEDs blinking.
"""
import time
import board
import digitalio

led_01 = digitalio.DigitalInOut(board.GP10)
led_01.direction = digitalio.Direction.OUTPUT

led_02 = digitalio.DigitalInOut(board.GP11)
led_02.direction = digitalio.Direction.OUTPUT

led_03 = digitalio.DigitalInOut(board.GP12)
led_03.direction = digitalio.Direction.OUTPUT

led_04 = digitalio.DigitalInOut(board.GP13)
led_04.direction = digitalio.Direction.OUTPUT

led_05 = digitalio.DigitalInOut(board.GP14)
led_05.direction = digitalio.Direction.OUTPUT

led_06 = digitalio.DigitalInOut(board.GP15)
led_06.direction = digitalio.Direction.OUTPUT

leds = [led_01, led_02, led_03, led_04, led_05, led_06]

while True:
    for led in leds:
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)
        print('hola')