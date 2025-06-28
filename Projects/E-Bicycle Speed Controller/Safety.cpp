// Safety: If RPM too high, shut down
if (currentRPM > 120) {
  analogWrite(pwmPin, 0);
  Serial.println("!!! Over-speed detected. Motor stopped.");
  delay(1000); // Safety cooldown
}
