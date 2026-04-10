import M5
import machine
import time

# 1. Initialize the device and screen
M5.begin()
M5.Lcd.setTextSize(3)  # Make the text larger

# 2. Configure the PIR sensor pin (Top red Grove port is 32)
pir = machine.Pin(32, machine.Pin.IN)

while True:
    if pir.value() == 1:
        # Motion detected: Red background, print "YES!"
        M5.Lcd.clear(0xFF0000)
        M5.Lcd.setCursor(40, 50)
        M5.Lcd.print("YES!")
    else:
        # No motion: Black background, print "NO"
        M5.Lcd.clear(0x000000)
        M5.Lcd.setCursor(40, 50)
        M5.Lcd.print("NO")

    time.sleep(0.3)  # Slight delay to prevent screen flickering