import machine
import utime

PWM_signal = machine.PWM(machine.Pin(16))
PWM_signal.freq(1000)  # default 1000

max_duty_cycle = 65535

# main routine
# duty_cycle = round(max_duty_cycle * 0.5)
# PWM_signal.duty_u16(duty_cycle)

while True:

    # ramp up
    duty_cycle = 0
    while duty_cycle <= max_duty_cycle:
        duty_cycle += 10
        PWM_signal.duty_u16(duty_cycle)
        utime.sleep(0.001)

    # ramp down
    duty_cycle = max_duty_cycle
    while duty_cycle >= 0:
        duty_cycle -= 10
        PWM_signal.duty_u16(duty_cycle)
        utime.sleep(0.001)

# # end routine
# PWM_signal.duty_u16(1)
# PWM_signal.deinit()