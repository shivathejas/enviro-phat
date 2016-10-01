from .i2c_bus import bus, altbus
from .ads1015 import ads1015
from .bmp280 import bmp280
from .leds import leds
from .lsm303d import lsm303d
from .tcs3472 import tcs3472

leds = leds()

try:
    light = tcs3472(bus)
    weather = bmp280(bus)
    analog = ads1015(bus)
    motion = lsm303d(bus)
except IOError:
    light = tcs3472(altbus)
    weather = bmp280(altbus)
    analog = ads1015(altbus)
    motion = lsm303d(altbus) 
