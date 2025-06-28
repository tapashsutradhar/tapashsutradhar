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
