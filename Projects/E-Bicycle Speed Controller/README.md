# E-Bicycle Speed Controller 


## Containts



## Project Overview

The E-Bicycle Speed Controller project aims to design and implement a microcontroller-based system for efficient and safe speed regulation of an electric bicycle. This system combines both hardware and software elements to provide real-time monitoring and control of the motor speed based on input from sensors and throttle position.

## Objective

Develop a reliable speed control system for an e-bicycle.
Implement embedded hardware and software integration.
Enable speed regulation based on throttle input and motor feedback.
Enhance safety and battery efficiency.

## System Components

### Hardware Components
|   Component          |   Specification / Description |
|----------------------|-------------------------------|
|   Microcontroller    |   Arduino UNO / STM32 / ESP32 |
|   Motor Driver       |   BTS7960 / L298N / VESC      |
|   Brushless DC Motor |   250W/500W BLDC Motor        |
|   Throttle           |   Hall Effect Based Throttle  |
|   Speed Sensor       |   Hall Effect + Magnet        |
|   Battery Pack       |   24V / 36V Lithium Ion       |
|   Display (optional) |   OLED / LCD (I2C)            |
|   Miscellaneous      |   Connectors, wires, switches |

|       |  |
| ----------- | ----------- |
|       |        |
|    |         |

### Software Components

Arduino IDE (for programming microcontroller)
Embedded C/C++
Serial Monitor for debugging
PWM Control for motor speed
Interrupt-based Hall sensor feedback for RPM calculation


## Embedded System Architecture

The embedded system architecture integrates the following subsystems:

- Input System:
Throttle (analog signal via ADC)
Speed sensor (digital input via interrupt)

- Processing Unit:
Microcontroller processes analog throttle value
Computes desired speed and compares with actual speed

- Output System:
Motor driver receives PWM signal
Motor speed is adjusted accordingly

- Feedback Loop:
Speed sensor provides real-time RPM
Feedback helps dynamically adjust PWM to maintain smooth control