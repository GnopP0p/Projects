#include <RTClib.h>
#include <SevSeg.h>

SevSeg sevseg; 
RTC_DS3231 rtc; 

DateTime dtBegin (2019, 7, 20, 0, 0, 0);
TimeSpan tsPassed;

void showInfo(const DateTime& dt) {
  Serial.print("NOW:");
  
  Serial.print(dt.year(), DEC);
  Serial.print('/');
  Serial.print(dt.month(), DEC);
  Serial.print('/');
  Serial.print(dt.day(), DEC);
  Serial.print(' ');
  Serial.print(dt.hour(), DEC);
  Serial.print(':');
  Serial.print(dt.minute(), DEC);
  Serial.print(':');
  Serial.print(dt.second(), DEC);
  
  Serial.print("\tPASSED:");
  Serial.print(tsPassed.days(), DEC);
  Serial.print(' ');
  Serial.print(tsPassed.hours(), DEC);
  Serial.print(':');
  Serial.print(tsPassed.minutes(), DEC);
  Serial.print(':');
  Serial.print(tsPassed.seconds(), DEC);
  
  Serial.println("");
}

//=========================================
//
//=========================================
void delayWithUpdate(uint32_t parDelay){
  uint32_t started=millis();
  while (millis()< started+parDelay){
    sevseg.refreshDisplay();
  }
}
//=========================
//=========================
void setup(){
  Serial.begin(9600);
  Serial.println(__TIME__);
  
  if (! rtc.begin()) {
        Serial.println("Couldn't find RTC");

        while (1);
  }
      
  delay(1000);    

  
//rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));   
      

  byte numDigits = 4;
  byte digitPins[] = {7, 8, 9, 10};
  //SEG:  A B C D E F G .
  //PIN:  11  7 4 2 1 10  5 3
  //ARDU: 2 3 4 5 11  12  13  6
  //byte segmentPins[] = {2, 3, 4, 5, 11, 12, 13, 6};
  byte segmentPins[] = {2, 3, 4, 5, 11, 12, 13, 6};
  bool resistorsOnSegments = false; // 'false' means resistors are on digit pins
  byte hardwareConfig = COMMON_ANODE; // See README.md for options
  bool updateWithDelays = true; // Default 'false' is Recommended
  bool leadingZeros = false; // Use 'true' if you'd like to keep the leading zeros
  bool disableDecPoint = true; // Use 'true' if your decimal point doesn't exist or isn't connected
  
  sevseg.begin(hardwareConfig, numDigits, digitPins, segmentPins, resistorsOnSegments,
  updateWithDelays, leadingZeros, disableDecPoint);
  sevseg.setBrightness(-90);
  
  
  
  sevseg.setNumber(1234, 1);
  delayWithUpdate(1000);
  
  
  sevseg.setNumber(8888, 1);
  delayWithUpdate(1000);
  
}
//=========================
//=========================
void loop(){
  sevseg.refreshDisplay();
  
  DateTime now = rtc.now();
  
  tsPassed = now-dtBegin;
  
  static uint32_t nextReportMillis=0;
  static uint16_t prevDaysPassed=0;
  
  if (tsPassed.days() != prevDaysPassed){
    prevDaysPassed=tsPassed.days();
    sevseg.setNumber(prevDaysPassed, 0);
  }

  
  sevseg.refreshDisplay();
  
  if (millis()>nextReportMillis){
    showInfo(now);
    nextReportMillis=millis()+5000;
  }
  
}
