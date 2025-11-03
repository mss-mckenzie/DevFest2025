# DevFest2025
Windsor Google DevFest 2025 - High School Track
## Raspberry Pi Pico 2 Project Development

[1. Download Thonny IDE](https://thonny.org/)

[2. Add MicroPython Firmware](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3)

## Raspberry Pi Pico Pinout

![4. Nano Pinout](pico-2-r4-pinout.svg)

![](nano_on_board.jpg)
  
Raspberry Pi Pico is an inexpensive micro-controller. This means that it is designed to transfer programs to the chip and it will run these programs even when not attached to a computer. It's intended for anyone making interactive projects.

[5. L298N Overview](https://components101.com/modules/l293n-motor-driver-module)

[L298N In Depth](https://howtomechatronics.com/tutorials/arduino/arduino-dc-motor-control-tutorial-l298n-pwm-h-bridge/)

## L298N Pinout
![5. L298N Pinout](L298N-Module-Pinout.jpg)

The L298N is also called an H-Bridge. It is used for 2 reasons.
1. It allows us to direct voltage that is higher than our board can handle. We need this if we can our car to move with any speed at all.
2. It allows us to reverse to polarity on our votage. This allows us to spin the motors in the other direction.
