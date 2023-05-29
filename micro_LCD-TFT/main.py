from machine import Pin
import time

led_board = Pin(25, Pin.OUT)  # LED in board
led_external = Pin(16, Pin.OUT)  # LED external through a GPIO

led_board(0) # init LED in board

while True:
    led_external(1)
    time.sleep(0.5)
    led_external(0)
    time.sleep(0.25)
