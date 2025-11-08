from machine import Pin
import time

ir_pin = Pin(15, Pin.IN)  # IR receiver output connected to GP15

def read_pulse():
    """Wait for a pulse and measure its length in microseconds"""
    while ir_pin.value() == 1:
        pass
    start = time.ticks_us()
    while ir_pin.value() == 0:
        pass
    end = time.ticks_us()
    return time.ticks_diff(end, start)

def read_ir_signal():
    """Read and decode an IR signal"""
    pulses = []
    start_time = time.ticks_ms()

    while time.ticks_diff(time.ticks_ms(), start_time) < 100:  # read for 100 ms
        pulse = read_pulse()
        pulses.append(pulse)
    
    print("Pulses:", pulses)

while True:
    print("Waiting for IR signal...")
    read_ir_signal()
    time.sleep(1)
