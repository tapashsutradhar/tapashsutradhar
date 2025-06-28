# E-Bicycle Speed Controller 

<em>The E-Bicycle Speed Controller project aims to design and implement a microcontroller-based system for efficient and safe speed regulation of an electric bicycle. This system combines both hardware and software elements to provide real-time monitoring and control of the motor speed based on input from sensors and throttle position.</em>

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

### Software Components

Arduino IDE (for programming microcontroller) <br>
Embedded C/C++ <br>
Serial Monitor for debugging <br>
PWM Control for motor speed <br>
Interrupt-based Hall sensor feedback for RPM calculation <br>

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

## Circuit Diagram

```
[Throttle] --> [ADC Pin - MCU] --> [PWM Signal] --> [Motor Driver] --> [BLDC Motor]
                                           ↑
[Hall Sensor RPM Feedback] --> [Interrupt Pin - MCU]

```

## Controller Programming (Arduino)

cpp
```
// Pin configuration
const int throttlePin = A0;
const int pwmPin = 9;
const int hallPin = 2;

volatile int rpmCount = 0;
unsigned long lastReadTime = 0;
float rpm = 0;

void setup() {
  pinMode(throttlePin, INPUT);
  pinMode(pwmPin, OUTPUT);
  pinMode(hallPin, INPUT_PULLUP);

  attachInterrupt(digitalPinToInterrupt(hallPin), countRPM, RISING);
  Serial.begin(9600);
}

void loop() {
  // Throttle input (0-1023)
  int throttleVal = analogRead(throttlePin);

  // Map throttle to PWM (0-255)
  int pwmVal = map(throttleVal, 0, 1023, 0, 255);
  analogWrite(pwmPin, pwmVal);

  // Calculate RPM every second
  if (millis() - lastReadTime >= 1000) {
    detachInterrupt(digitalPinToInterrupt(hallPin));
    rpm = rpmCount * 60.0;  // assuming 1 pulse per revolution
    rpmCount = 0;
    lastReadTime = millis();
    attachInterrupt(digitalPinToInterrupt(hallPin), countRPM, RISING);

    Serial.print("Throttle: ");
    Serial.print(throttleVal);
    Serial.print(" | PWM: ");
    Serial.print(pwmVal);
    Serial.print(" | RPM: ");
    Serial.println(rpm);
  }
}

void countRPM() {
  rpmCount++;
}
```