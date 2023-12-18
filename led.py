from machine import Pin
from time import ticks_ms, ticks_diff, sleep_ms

led1 = Pin(35,Pin.OUT)
taster = Pin(20, Pin.IN)

led1_on = False

status = False
gedrueckt = False
war_aus = False
delay = 10

passed = ticks_ms()


while True:
    gedrueckt = taster.value()          #wertzuweisung status taster
    sleep_ms(100)                       #entstören
    
    if gedrueckt and war_aus:           #wenn Tasterstatus wechselt
        status = not status             #Toggle led status wert
        war_aus = False                 #set taster status aus für flanke
    if not gedrueckt:
        war_aus = True                  #reset taster status für flanke
    if status:
        
        time = ticks_ms()
        
        if (ticks_diff(time, passed) > 500):
            led1_on = not led1_on
            passed1 = time
        if led1_on == True:
            led1.on()
        else:
            led1.off()
    else:
        led1.off()