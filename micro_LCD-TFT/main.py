from machine import Pin
import time

led_board = Pin(25, Pin.OUT)  # LED in board
led_external = Pin(16, Pin.OUT)  # LED external through a GPIO

led_board(1)  # init LED in board
led_external(0)  # init LED external

while True:
    led_external(1)
    time.sleep(2)
    led_external(0)
    time.sleep(2)
