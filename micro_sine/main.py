# Example of using PIO for function generation using hacked PWM example
# pio_dac taken from: https://blog.rareschool.com/2021/02/raspberry-pi-pico-simple-projects.html
# tanks to romilly

from machine import ADC
from time import sleep_us, sleep_ms
import _thread

from pio_dac import PIOPWM

# # test routine using board led
# led = Pin(25, Pin.OUT)
# while True:
#     led(1)
#     time.sleep(1)
#     led(0)
#     time.sleep(1)

# Pin GP22 is output
pwm = PIOPWM(0, 22, max_count=250, count_freq=10_000_000)

sines = [
    124, 127, 130, 133, 136, 139, 142, 145, 148, 152,
    155, 158, 161, 164, 167, 170, 172, 175, 178, 181,
    184, 186, 189, 192, 194, 197, 200, 202, 204, 207,
    209, 211, 214, 216, 218, 220, 222, 224, 226, 227,
    229, 231, 232, 234, 235, 237, 238, 239, 240, 241,
    242, 243, 244, 245, 246, 246, 247, 247, 248, 248,
    248, 248, 249, 249, 248, 248, 248, 248, 247, 247,
    246, 246, 245, 244, 243, 242, 241, 240, 239, 238,
    237, 235, 234, 232, 231, 229, 227, 226, 224, 222,
    220, 218, 216, 214, 211, 209, 207, 204, 202, 200,
    197, 194, 192, 189, 186, 184, 181, 178, 175, 172,
    170, 167, 164, 161, 158, 155, 152, 148, 145, 142,
    139, 136, 133, 130, 127, 124, 120, 117, 114, 111,
    108, 105, 102, 99, 95, 92, 89, 86, 83, 80,
    77, 75, 72, 69, 66, 63, 61, 58, 55, 53,
    50, 48, 45, 43, 40, 38, 36, 33, 31, 29,
    27, 25, 23, 21, 20, 18, 16, 15, 13, 12,
    10, 9, 8, 7, 6, 5, 4, 3, 2, 1,
    1, 0, 0, -1, -1, -1, -1, -1, -1, -1,
    -1, -1, -1, 0, 0, 1, 1, 2, 3, 4,
    5, 6, 7, 8, 9, 10, 12, 13, 15, 16,
    18, 20, 21, 23, 25, 27, 29, 31, 33, 36,
    38, 40, 43, 45, 48, 50, 53, 55, 58, 61,
    63, 66, 69, 72, 75, 77, 80, 83, 86, 89,
    92, 95, 99, 102, 105, 108, 111, 114, 117, 120,
]


pot = ADC(26)
delay = [400]


def read_pot():
    while True:
        v = pot.read_u16()
        delay[0] = 20 + (400 * v)// 65000
        sleep_ms(100)


_thread.start_new_thread(read_pot, ())

while True:
    for i in range(0, 250, 25):
        pwm.set(sines[i])
        sleep_us(delay[0])
