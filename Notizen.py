

"""
Notizen
----------
Pinbelegung 
----------
AHT10
VIN - +3.3
GND - 0
SCL - 41
SDA - 42
----------
BH1750
VIN - +3.3
GND - 0
SCL - 38
SDA - 39
ADDR - none
---------
LEDs
35
36
47
48

PIN -> LED -> 220R -> GND
oder
PIN -> 220R -> LED -> GND
---------
Taster 
Pin 20
PullDOWN: (standard, Pin an GND "gezogen")
            Pin | 1k / 2k R -> GND
+ 3.3 -> Taster | 
PullUP:
          Pin | 1k / 2k R <- +3.3
GND <- Taster | 
----------

"""