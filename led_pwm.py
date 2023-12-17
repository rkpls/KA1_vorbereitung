from machine import Pin
from machine import PWM
import time


pwm_freq = 200

led1 = Pin(35,Pin.OUT)
pwm1 = PWM(led1)

while True:
    for i in range(0,800,10):
        pwm1.freq(pwm_freq)
        pwm1.duty(i)
        time.sleep(0.02)
    for i in range(800,0,-10):
        pwm1.freq(pwm_freq)
        pwm1.duty(i)
        time.sleep(0.02)
