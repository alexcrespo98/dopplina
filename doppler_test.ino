#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

const int signalPin = 34;

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define PLOT_WIDTH SCREEN_WIDTH
int plotData[PLOT_WIDTH];
int plotIndex = 0;

int minValue = 4095;
int maxValue = 0;

// Helper function to update min and max for auto scaling
void updateMinMax() {
  minValue = 4095;
  maxValue = 0;
  for (int i = 0; i < PLOT_WIDTH; i++) {
    if (plotData[i] < minValue) minValue = plotData[i];
    if (plotData[i] > maxValue) maxValue = plotData[i];
  }
  if (maxValue == minValue) maxValue = minValue + 1;
}

void setup() {
  Serial.begin(115200);
  pinMode(signalPin, INPUT);

  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;);
  }

  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(1);
  display.setCursor(0, 0);
  display.println("HB100 Doppler Radar Test");
  display.display();
  delay(1000);
}

void loop() {
  int rawValue = analogRead(signalPin);

  // Store raw data for plotting
  plotData[plotIndex] = rawValue;
  plotIndex = (plotIndex + 1) % PLOT_WIDTH;

  updateMinMax();

  display.clearDisplay();

  // Draw waveform with auto scaling
  for (int i = 0; i < PLOT_WIDTH - 1; i++) {
    int x0 = i;
    int y0 = map(plotData[(plotIndex + i) % PLOT_WIDTH], minValue, maxValue, SCREEN_HEIGHT - 1, 0);
    int x1 = i + 1;
    int y1 = map(plotData[(plotIndex + i + 1) % PLOT_WIDTH], minValue, maxValue, SCREEN_HEIGHT - 1, 0);
    display.drawLine(x0, y0, x1, y1, SSD1306_WHITE);
  }

  // Show current raw value
  display.setCursor(0, 0);
  display.setTextSize(1);
  display.print("Val: ");
  display.print(rawValue);

  display.display();

  Serial.println(rawValue);

  delay(10);
}
