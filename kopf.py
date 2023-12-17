"""
Autor: Riko Pals
Kurs: ETS23 Microcontroller - Micropython
Klausur 1
Datum: 19.12.2023

Ein Programm welches eine LED proportional zur Umgebungshelligkeit dimmt. Das Programm kann über einen Taster ein und ausgeschaltet werden.

Benötigt:
 - Espressif ESP32 S3
 - Pulldown Taster
 - Helligkeitssensor mit I2c bus
 - LED zur Programmstatusanzeige
 - LED zum Dimmen
    - LEDs  benötigen Vorwiderstände zur Strombegrenzung
"""

# ---------- BIBS ----------

from machine import Pin, PWM, SoftI2C
from time import sleep_ms, ticks_ms, ticks_diff

import bh1750
import ahtx0

# ---------- INIT + VARS ----------
status = False
gedrueckt = False
war_aus = False
entprell = 10
pwm_freq = 1000
passed = ticks_ms()
run = False
temp = 0
humid = 0

# Pin Setup
led_status = Pin(35,Pin.OUT)
led1 = Pin(36,Pin.OUT)
led2 = Pin(47,Pin.OUT)
led3 = Pin(48,Pin.OUT)
LED_dimm = PWM(led1)
taster = Pin(20, Pin.IN)

# ESP32 <-> i2c <-> Sensor Setup
i2c0_sda = Pin(39)
i2c0_scl = Pin(38)
i2c0 = SoftI2C(sda=i2c0_sda, scl=i2c0_scl)
bh_1750 = bh1750.BH1750(0x23, i2c0)
i2c1_sda = Pin(44)
i2c1_scl = Pin(41)
i2c1 = SoftI2C(sda=i2c1_sda, scl=i2c1_scl)
aht_10 = ahtx0.AHT10(i2c1)

# ---------- FUNCTIONS ----------

def ausschalten(i):
    # das programm wird einmal ausgeschaltet
    if i == True:
        led_status.off()
        led1.off()
        led2.off()
        led3.off()

def read_brightness():                          #helligkeit auslesen und weitergeben
    try:
        brightness = bh_1750.measurement
        return brightness
    except:
        print("Helligkeit via I2C konnte nicht gelesen werden")

def read_ambient(i):                            #temp oder hunid auslesen und weitergeben
    try:
        global temp, humid
        temp = aht_10.temperature
        humid = aht_10.relative_humidity
    except:
        print("Temperatur oder Feuchte via I2C konnte nicht gelesen werden")

def dimmer(duty):
    if duty >= 1024:
        duty = 1023
    try:
        LED_dimm.duty(duty)
    except:
        print("LED dimmen via PWM konnte nicht ausgeführt werden")
    
# ---------- LOOP ----------

while True:
    gedrueckt = taster.value()                              #taster einlesen
    LED_dimm.freq(pwm_freq)
    sleep_ms(entprell)
    # Taster toggle zum ein- und ausschalten
    if gedrueckt and war_aus:
        status = not status 
        war_aus = False
    if not gedrueckt:
        war_aus = True
    if status:
        time = ticks_ms()
        if (ticks_diff(time, passed) > 100):                #programm wird jede 0.1s ausgeführt ohne sleep
            run = not run
            led_status.on()
            # helligkeit auslesen und led dimmen
            brightness = (read_brightness())
            duty = brightness * 0.2
            dimmer(duty)
            # aktuelle messwerte abfragen zur verwendung
            read_ambient()
            # bei kritische werte LEDs schalten
            if temp <= 25 and humid <= 70:
                led2.on()
                led3.off()
            else:
                led3.on()
                led2.off()
            passed = time
        else:
            pass
    else:
        # ausschalten für reset
        ausschalten(war_aus)