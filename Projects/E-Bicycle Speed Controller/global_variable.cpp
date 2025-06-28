volatile unsigned int hallPulseCount = 0; // Used in interrupt
unsigned long lastTime = 0;
float currentRPM = 0;

int throttleValue = 0;
int pwmOutput = 0;