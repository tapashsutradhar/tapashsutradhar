float current = getCurrentReading(); // From ACS712
float voltage = getVoltageReading(); // From voltage divider
sendModbus(voltage, current);
