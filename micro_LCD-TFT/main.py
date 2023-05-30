import machine  # import Pin
import utime

led_board = machine.Pin(25, machine.Pin.OUT)  # LED in board
led_external = machine.Pin(16, machine.Pin.OUT)  # LED external through a GPIO

led_board(0)  # init LED in board
led_external(0)  # init LED external

while True:
    led_external(1)
    utime.sleep(1)
    led_external(0)
    utime.sleep(1)
