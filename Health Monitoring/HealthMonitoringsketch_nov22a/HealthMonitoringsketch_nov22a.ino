#include <WiFi.h>
#include <ThingSpeak.h>
#include <OneWire.h>
#include <DallasTemperature.h>

// Wi-Fi and ThingSpeak details
const char *ssid = "shravani";              
const char *password = "12345678";        
unsigned long myChannelNumber = 2758621;     
const char *myWriteAPIKey = "BU5PBGG6D2ME9RWA"; 

WiFiClient client;

// DS18B20 Temperature Sensor setup
#define ONE_WIRE_BUS 4  // GPIO4 for DS18B20 data pin
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Heart Rate Sensor setup
#define HEART_RATE_PIN 32  // GPIO32 for HW-827 signal pin

void setup() {
  // Start serial communication
  Serial.begin(115200);

  // Connect to Wi-Fi
  Serial.print("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected!");

  // Initialize ThingSpeak
  ThingSpeak.begin(client);

  // Enable internal pull-up resistor for DS18B20 data pin
  pinMode(ONE_WIRE_BUS, INPUT_PULLUP);

  // Initialize DS18B20 sensor
  sensors.begin();

  // Initialize heart rate sensor pin
  pinMode(HEART_RATE_PIN, INPUT);
}

void loop() {
  // Read temperature from DS18B20
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  Serial.print("Temperature (°C): ");
  Serial.println(temperature);

  // Read heart rate sensor raw value
  int heartRateRaw = analogRead(HEART_RATE_PIN);

  // Filter unexpected high readings
  if (heartRateRaw > 4000) { // Threshold for ADC saturation
    heartRateRaw = 0;  // Ignore invalid readings
  }

  Serial.print("Heart Rate Raw Value: ");
  Serial.println(heartRateRaw);

  // Send data to ThingSpeak
  ThingSpeak.setField(1, heartRateRaw); // Field 1: Heart Rate
  ThingSpeak.setField(2, temperature); // Field 2: Temperature

  int statusCode = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
  if (statusCode == 200) {
    Serial.println("Data sent to ThingSpeak successfully!");
  } else {
    Serial.print("Error sending data to ThingSpeak. Status code: ");
    Serial.println(statusCode);
  }

  // Delay to match ThingSpeak's rate limit (15 seconds)
  delay(15000);
}
