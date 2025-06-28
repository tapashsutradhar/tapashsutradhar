void loop() {
  // Read throttle (0-1023)
  throttleValue = analogRead(throttlePin);

  // Convert to PWM (0-255)
  pwmOutput = map(throttleValue, 0, 1023, 0, 255);
  analogWrite(pwmPin, pwmOutput);

  // Calculate RPM every 1000 ms
  if (millis() - lastTime >= 1000) {
    detachInterrupt(digitalPinToInterrupt(hallPin));
    currentRPM = hallPulseCount * 60.0; // 1 pulse per rotation
    hallPulseCount = 0;
    lastTime = millis();
    attachInterrupt(digitalPinToInterrupt(hallPin), hallInterrupt, RISING);

    // Display telemetry
    Serial.print("Throttle: ");
    Serial.print(throttleValue);
    Serial.print(" | PWM: ");
    Serial.print(pwmOutput);
    Serial.print(" | RPM: ");
    Serial.println(currentRPM);
  }
}
