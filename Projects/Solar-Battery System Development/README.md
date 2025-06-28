# Solar-Battery System Development

Led the design and testing of a compact solar-battery system for off-grid applications in rural settings. Responsibilities included: <br>
•	Designing the wiring layout and selecting circuit protection devices to ensure field safety and maintainability. <br>
•	Developing basic charge/discharge control logic tailored for low-cost deployment. <br>
•	Assisting in prototype construction, conducting performance and safety testing, and compiling detailed documentation: wiring schematics, bill of materials, and test data. <br>
This project emphasized the critical role of clarity, safety, and reliability in real-world system deployment.

## Objective
To design and build a small-scale, cost-effective solar-battery system capable of powering basic loads in rural or remote areas without access to the electrical grid. The system focuses on reliability, safety, and field-replicability using accessible components.

## System Overview

The system includes:
- 200W Solar Panel
- 12V LiFePO₄ Battery
- MPPT Charge Controller
- DC Load Ports (lighting, USB)
- Real-Time Monitoring with Arduino and INA219 Sensors
- Modbus RTU (RS-485) Communication for Monitoring

## Component List

Solar Panel	
MPPT Charge Controller
Battery LiFePO₄
Arduino Uno	Microcontroller
INA219 Sensors	Current & Voltage Measurement
RS-485 Module	Modbus RTU Communication
DC Loads	12V LED lights, USB ports
Fuses & Disconnects	Safety protection

## System Design

- Sizing: Based on ~600Wh/day energy demand
- Solar Panel: Chosen to recharge battery in 4–5 hours of sunlight
- Battery: Sized for 1 day of autonomy
- Charge Controller: MPPT for efficiency, protects against over/under-voltage
- Load: DC lighting and USB ports for device charging
- Monitoring: Arduino reads current/voltage, logs data, and communicates via RS-485

<<<<<<< HEAD
## Explanation of Key Components and Connections

1. Solar Panel
Connects directly to PV input of the MPPT charge controller.

Use MC4 connectors or proper DC screw terminals.

Typical output: 18V DC (unregulated).

2. MPPT Charge Controller
Regulates charging of the battery based on solar input.

Has three terminals:

PV input (from panel)

Battery output (to battery)

Load output (to DC devices or fuse box)

3. Battery (LiFePO₄ 12V 50Ah)
Stores energy from the panel via the charge controller.

Should have a built-in BMS for overcharge/discharge protection.

Connect battery + to controller battery + and same for –.

4. DC Loads
Connect via load terminal of the charge controller or directly from the battery through a fused DC bus.

Includes:

LED lights (12V)

USB charging module (12V to 5V buck converter)

5. Sensors (INA219)
INA219 #1: Connected between solar panel and controller to measure input voltage/current.

INA219 #2: Connected between battery and load to monitor load usage.

Both sensors communicate with Arduino using I2C (SDA/SCL) and require Vcc + GND.

6. Arduino Uno
Collects sensor data and sends it to:

Serial monitor

RS-485 Modbus interface (optional)

Uses basic code to compute power (V x I), log data, and flag issues (e.g., low battery).

7. RS-485 Module (Modbus)
Transmits Arduino data to a remote PC, dashboard, or microserver.

Optional — for telemetry or upgrades.
=======
![Basic ASCII Circuit Diagram](https://github.com/tapashsutradhar/tapashsutradhar/blob/main/Projects/Solar-Battery%20System%20Development/Basic%20ASCII%20Circuit%20Diagram.less)
>>>>>>> 2123890cc1e68b4bdaa321adb6cf5e5cfc20a19f

## Wiring Diagram

![/Projects/Solar-Battery System Development/Schematic diagram Solar Project.png](https://github.com/tapashsutradhar/tapashsutradhar/blob/main/Projects/Solar-Battery%20System%20Development/Schematic%20diagram%20Solar%20Project.png)

## Testing

- Load Tests: Simulated day/night cycles with constant and variable loads
- Performance Logging: Charge/discharge cycles, voltage drops, efficiency
- Protection Testing: Fuse blowout, low-voltage disconnect, reverse polarity

## Results

- The system consistently powered 6–8 hours of lighting + device charging
- Battery voltage stayed within safe bounds
- Sensor readings were within ±3% accuracy of multimeter
- Monitoring data was successfully transmitted using Modbus
## Challenges
- Noise in sensor readings under load switching
- Inconsistent battery BMS cut-off during over-discharge (later resolved)

## Future Improvements
- Add over-the-air (OTA) monitoring via GSM/LoRa
- Upgrade dashboard with real-time web interface
- Expand to AC inverter compatibility
