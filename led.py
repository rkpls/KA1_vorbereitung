from machine import Pin
from time import ticks_ms, ticks_diff, sleep_ms

led1 = Pin(35,Pin.OUT)
led2 = Pin(36,Pin.OUT)
led3 = Pin(47,Pin.OUT)
led4 = Pin(48,Pin.OUT)
taster = Pin(20, Pin.IN)

led1_on = False
led2_on = False
led3_on = False
led4_on = False

status = False
gedrueckt = False
war_aus = False
delay = 10

passed1 = ticks_ms()
passed2 = ticks_ms()
passed3 = ticks_ms()
passed4 = ticks_ms()


while True:
    gedrueckt = taster.value()          #wertzuweisung status taster
    sleep_ms(100)                  #entstören
    
    if gedrueckt and war_aus:           #wenn Tasterstatus wechselt
        status = not status             #Toggle led status wert
        war_aus = False                 #set taster status aus für flanke
    if not gedrueckt:
        war_aus = True                  #reset taster status für flanke
    if status:
        
        time = ticks_ms()
        
        if (ticks_diff(time, passed1) > 2000):
            led1_on = not led1_on
            passed1 = time
        if led1_on == True:
            led1.on()
        else:
            led1.off()
        
        if (ticks_diff(time, passed2) > 1000):
            led2_on = not led2_on
            passed2 = time
        if led2_on == True:
            led2.on()
        else:
            led2.off()
            
        if (ticks_diff(time, passed3) > 500):
            led3_on = not led3_on
            passed3 = time
        if led3_on == True:
            led3.on()
        else:
            led3.off()
            
        if (ticks_diff(time, passed4) > 250):
            led4_on = not led4_on
            passed4 = time
        if led4_on == True:
            led4.on()
        else:
            led4.off()
    else:
        led1.off()
        led2.off()
        led3.off()
        led4.off()