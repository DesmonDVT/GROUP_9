import machine, time

led = machine.Pin(32, machine.Pin.OUT)


def set_color(r, g, b):
    machine.bitstream(led, 0, (400, 850, 800, 450), bytearray([g, r, b] * 30))


while True:
    set_color(20, 0, 0)  # red
    time.sleep(0.5)

    set_color(0, 20, 0)  # green
    time.sleep(0.5)

    set_color(0, 0, 20)  # blue
    time.sleep(0.5)