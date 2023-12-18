
import time
from machine import Pin

led1 = Pin(35,Pin.OUT)
led2 = Pin(36, Pin.OUT)

taster = Pin(20, Pin.IN)
status = False
gedrueckt = False
war_aus = False
entprell = 100

led2.on()
while True:
    gedrueckt = taster.value()          #wertzuweisung status taster
    time.sleep_ms(entprell)             #entstören
    print(gedrueckt)                    #spammt taster wert zur kontrolle 
    
    if gedrueckt and war_aus:           #wenn Tasterstatus wechselt
        status = not status             #Toggle led status wert
        war_aus = False                 #set taster status aus für flanke
    if not gedrueckt:
        war_aus = True                  #reset taster status für flanke
    if status:
        led1.on()                       #wenn status an led an
    else:
        led1.off()                      #sonst aus