if (batteryVoltage < 11.8) {
  digitalWrite(loadRelay, LOW);  // Disconnect load
} else if (batteryVoltage > 12.0) {
  digitalWrite(loadRelay, HIGH); // Reconnect load
}

if (batteryVoltage > 14.4) {
  digitalWrite(chargeRelay, LOW);  // Stop charging
} else {
  digitalWrite(chargeRelay, HIGH); // Allow charging
}
