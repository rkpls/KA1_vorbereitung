import utime
from machine import Pin, SoftI2C

import ahtx0

# I2C for the Wemos D1 Mini with ESP8266
i2c = SoftI2C(scl=Pin(41), sda=Pin(42))

# Create the sensor object using I2C
aht10 = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.0f C" % aht10.temperature)
    print("Humidity: %0.0f %%" % aht10.relative_humidity)
    utime.sleep(2)