#include <WiFi.h>
#include <ThingSpeak.h>

// WiFi credentials
const char* ssid = "IAAP-2.4G";
const char* password = "mapping8812";

// ThingSpeak credentials
const char* thingspeakApiKey = "QH5WD7QS4BVOG75G";
const unsigned long THINGSPEAK_CHANNEL_ID = 2461907;


// Temperature sensor settings
const int tempPin = 32;  // Pin connected to the temperature sensor

// Variables
WiFiClient client;

void setup() {
  Serial.begin(115200);
  delay(1000); // Allow time for serial monitor to open

  // Connect to WiFi
  Serial.println("Connecting to WiFi...");
  connectToWiFi();
}

void loop() {
  // Check WiFi connection
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected. Reconnecting...");
    connectToWiFi();
    return;
  }

  // Read temperature sensor value
  float temperature = readTemperature();
  
  // Print temperature
  Serial.print("Temperature: ");
  Serial.println(temperature);
  
  // Send temperature data to ThingSpeak
  sendDataToThingSpeak(temperature);

  // Delay before next reading and upload
  delay(1000); // 15 seconds delay
}

void connectToWiFi() {
  WiFi.begin(ssid, password);
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(300);
    Serial.print(".");
    if (++attempts >= 20) {
      Serial.println("WiFi connection failed. Please check your credentials and try again.");
      return;
    }
  }
  Serial.println("\nWiFi connected");
}

float readTemperature() {
  // Replace this with your code to read temperature from your sensor
  // For demonstration purposes, let's assume we're reading from an analog sensor
  int rawValue = analogRead(tempPin);
   Serial.println("rawvalue");
    Serial.println(rawValue);
    float temperature;
    if(rawValue<=330)
    {
      temperature=20.0;
    float v=(float)(rawValue*5)/330;
    temperature=temperature+v;

    }
    else if(rawValue>330 && rawValue<=1000)
    {
      temperature=36.0;
    float v=(float)(rawValue*2)/1500;
    temperature=temperature+v;

    }
    else
    {
    temperature=39.0;
    float v=(float)(rawValue*3)/1500;
    temperature=temperature+v;



    }
    temperature=1.8*temperature+32;

    
 // float temperature = map(rawValue, 0, 4095, 0, 100);  // Map the raw value to temperature range (0-100 degrees Celsius)
  return temperature;
}

void sendDataToThingSpeak(float temperature) {
  // Establish connection to ThingSpeak
  if (!client.connect("api.thingspeak.com", 80)) {
    Serial.println("Connection to ThingSpeak failed.");
    return;
  }

  // Prepare the API URL
  String url = "/update?api_key=";
  url += thingspeakApiKey;
  url += "&field1=";
  url += String(temperature);

  // Send GET request to ThingSpeak
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: api.thingspeak.com\r\n" +
               "Connection: close\r\n\r\n");

  // Wait for response from ThingSpeak
  unsigned long timeout = millis();
  while (client.available() == 0) {
    if (millis() - timeout > 5000) {
      Serial.println("No response from ThingSpeak.");
      client.stop();
      return;
    }
  }

  // Print response from ThingSpeak
  while (client.available()) {
    char c = client.read();
    //serial.print(c);
  }

  // Close connection
  Serial.println("\nData sent to ThingSpeak.");
  client.stop();
}
