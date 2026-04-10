import os, sys, io
import M5
from M5 import Widgets
from hardware import Pin, I2C
from unit import ENVUnit
import time

# Global variable assignment
i2c0 = None
env3_0 = None
label_title = None
label_temp = None
label_hum = None

def setup():
    global i2c0, env3_0, label_title, label_temp, label_hum

    M5.begin()
    # Landscape display
    M5.Lcd.setRotation(1)
    Widgets.fillScreen(0x222222)

    # Larger font, centered position for clearer and more complete display
    label_title = Widgets.Label("ENV III", 35, 5, 1.5, 0xFFFFFF, 0x222222, Widgets.FONTS.DejaVu18)
    label_temp = Widgets.Label("Temp: --.- C", 10, 35, 1.4, 0xFF5555, 0x222222, Widgets.FONTS.DejaVu18)
    label_hum  = Widgets.Label("Hum:  --.- %", 10, 70, 1.4, 0x55FFFF, 0x222222, Widgets.FONTS.DejaVu18)

    # StickC Plus I2C pins
    i2c0 = I2C(0, scl=Pin(33), sda=Pin(32), freq=100000)
    env3_0 = ENVUnit(i2c=i2c0, type=3)

def loop():
    global env3_0, label_temp, label_hum

    M5.update()

    temp = env3_0.read_temperature()
    hum = env3_0.read_humidity()

    label_temp.setText("Temp: {:.1f} C".format(temp))
    label_hum.setText("Hum:  {:.1f} %".format(hum))

    time.sleep_ms(500)

if __name__ == '__main__':
    try:
        setup()
        while True:
            loop()
    except (Exception, KeyboardInterrupt) as e:
        try:
            from utility import print_error_msg
            print_error_msg(e)
        except ImportError:
            print("Firmware dependency error. Please update to latest UIFlow 2.0 firmware.")