void setup() {
  pinMode(throttlePin, INPUT);
  pinMode(pwmPin, OUTPUT);
  pinMode(hallPin, INPUT_PULLUP); // Hall sensor input

  attachInterrupt(digitalPinToInterrupt(hallPin), hallInterrupt, RISING);

  Serial.begin(9600); // For debugging and data monitoring
}
