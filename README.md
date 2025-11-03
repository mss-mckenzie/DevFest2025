# DevFest2025
Windsor Google DevFest 2025 - High School Track
## Raspberry Pi Pico Project Development

[1. Download Thonny IDE](https://thonny.org/)

[2. Add MicroPython Firmware](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3)

[3. Arduino Language Reference](https://www.arduino.cc/reference/en/)

[4. Arduino Nano Overview](https://docs.arduino.cc/hardware/nano)

## Nano Pinout

![4. Nano Pinout](nano_pinout.png)

![](nano_on_board.jpg)
  
Arduino is an open-source electronics platform based on easy-to-use hardware and software. It's intended for anyone making interactive projects.

They produce a wide variety of boards for a wide variety of needs. We will be using the Arduino nano. This is an inexpensive board that is perfect for small projects.

[5. L298N Overview](https://components101.com/modules/l293n-motor-driver-module)

[L298N In Depth](https://howtomechatronics.com/tutorials/arduino/arduino-dc-motor-control-tutorial-l298n-pwm-h-bridge/)

## L298N Pinout
![5. L298N Pinout](L298N-Module-Pinout.jpg)

The L298N is also called an H-Bridge. It is used for 2 reasons.
1. It allows us to direct voltage that is higher than our board can handle. We need this if we can our car to move with any speed at all.
2. It allows us to reverse to polarity on our votage. This allows us to spin the motors in the other direction.
