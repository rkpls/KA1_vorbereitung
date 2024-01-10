
from utime import sleep
from machine import Pin, SoftI2C

import ahtx0

i2c = SoftI2C(scl=Pin(41), sda=Pin(42))
aht10 = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.0f C" % aht10.temperature)
    print("Humidity: %0.0f %%" % aht10.relative_humidity)
    sleep(2)