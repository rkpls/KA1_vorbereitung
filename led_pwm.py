from machine import Pin
from machine import PWM
import time


pwm_freq = 200

led1 = Pin(35,Pin.OUT)
pwm1 = machine.PWM(led1)

for i in range(0,1000,50):
    pwm1.freq(pwm_freq)
    pwm1.duty(i)
    time.sleep(0.1)
for i in range(1000,0,-50):
    pwm1.freq(pwm_freq)
    pwm1.duty(i)
    time.sleep(0.1)