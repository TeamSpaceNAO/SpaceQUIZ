#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClient.h>

WiFiClient wifiClient;
 
const char* ssid = "WebPocket-DE9B";
const char* password = "ZHGH1MXC";

const int rosso=4;
const int blu=5;
const int verde=14;
const int connection=12;

char* rispostaA="A";
char* rispostaB="B";
char* rispostaC="C";
char* id="2;";

HTTPClient http;  //Declare an object of class HTTPClient
 
void setup (){ 
  pinMode(rosso, INPUT);
  pinMode(blu, INPUT);
  pinMode(verde, INPUT);
   pinMode(connection, OUTPUT);
  
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
    digitalWrite(connection, LOW);
  }
  
  http.begin(wifiClient,"http://192.168.1.69:8081");
}
 
void loop(){
    if(WiFi.status() == WL_CONNECTED) { 
       digitalWrite(connection, HIGH); 
       int buttonState = digitalRead(rosso);
       int buttonState1 = digitalRead(blu);
       int buttonState2 = digitalRead(verde);
 
       if(buttonState==HIGH && buttonState1==LOW && buttonState2==LOW) {
         strcat(id, rispostaA);
         int httpCode= http.POST(id); 
         Serial.println('A');
         delay(3000);
         digitalWrite(connection, LOW); 
         ESP.restart();
       } 
       if(buttonState1==HIGH&& buttonState==LOW && buttonState2==LOW) {
         strcat(id, rispostaB);
         int httpCode = http.POST(id); 
         Serial.println('B');
         delay(3000);
         digitalWrite(connection, LOW);
         ESP.restart();
       }
       if(buttonState2==HIGH && buttonState1==LOW && buttonState==LOW) {
         strcat(id, rispostaC);
         int httpCode = http.POST(id); 
         Serial.println('C');
         delay(3000);
         digitalWrite(connection, LOW);
         ESP.restart();
       }
    }
}
  
