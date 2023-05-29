import machine
import utime

PWM_signal = machine.PWM(machine.Pin(2))  # GP2
PWM_signal.freq(100)  # default 1000

max_duty_cycle = 65535

# main code
duty_cycle = round(max_duty_cycle * 0.5)
PWM_signal.duty_u16(duty_cycle)

# # restart (not used)
# PWM_signal.duty_u16(1)
# PWM_signal.deinit()



