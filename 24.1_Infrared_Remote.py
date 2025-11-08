import time
from machine import Pin
from ir_rx.nec import NEC_16  # for 16-bit NEC remotes

def callback(data, addr, ctrl):
    if data < 0:
        print("Repeat code")
    else:
        print(f"Data: {data:02x}, Addr: {addr:04x}")

ir = NEC_16(Pin(16, Pin.IN), callback)

while True:
    time.sleep_ms(500)
