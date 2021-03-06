#include <TimerOne.h>
#include <ArduinoJson.h>

#define LINE_BUFFER_LENGTH 512

int l1 = 6;
void setup() {
    Timer1.initialize(10000000); // 1 second
  Timer1.attachInterrupt(sendData);
  Serial.begin( 115200 );
  pinMode(l1,OUTPUT);
}

void loop() 
{
  delay(100);
  char line[ LINE_BUFFER_LENGTH ];
  char c;
  int lineIndex = 0;
  bool lineIsComment, lineSemiColon;
 while (Serial.read() >= 0)
   ; // do nothing

  while (1) {
    // Serial reception - Mostly from Grbl, added semicolon support
    while ( Serial.available()>0 ) {
      c = Serial.read();
      if (( c == '\n') || ( c == '\r') ) {             // End of line reached
        if ( lineIndex > 0 ) {                        // Line is complete. Then execute!
          line[ lineIndex ] = '\0';                   // Terminate string
            //Serial.println( line ); 
          }
          lineIndex = 0;
          getData(line);
        } else {
          if ( lineIndex >= LINE_BUFFER_LENGTH-1 ) {
            //Serial.println( "ERROR - lineBuffer overflow" );
            lineIsComment = false;
            lineSemiColon = false;
          } 
          else if ( c >= 'a' && c <= 'z' ) {        // Upcase lowercase
            line[ lineIndex++ ] = c-'a'+'A';
          } 
          else {
            line[ lineIndex++ ] = c;
          }
        
      }
    }
    //Serial.println(analogRead(A5));
    delay(100);
    //delay(30000);
    //Serial.println("over voltage");
  }


}

  void getData(char* line){
   // Serial.println( line ); 
    /* if(!strcmp(line,"OFF")){
            digitalWrite(6,LOW);
          }else if(!strcmp(line,"ON")){
            digitalWrite(6,HIGH);
          }*/
         char *token,*token1,*token2;
         const char s[2] = " ";
   
   /* get the first token */
         token = strtok(line, s);
         //Serial.println(token);
         token1 = strtok(NULL,s);
         //Serial.println(token1);
         token2 = strtok(NULL,s);
         //Serial.println(token2);
          if(!strcmp(token,"D")){
              digitalWrite(atoi( token1 ),atoi( token2 ));
          }else if(!strcmp(token,"P")){
              analogWrite(atoi( token1 ),atoi( token2 ));
          }


  }
  void sendData(){
      StaticJsonDocument<200> doc;
      doc["pot"] = analogRead(A5);
      serializeJson(doc, Serial);
      Serial.println();
      //Serial.println(analogRead(A5));
  }
/*
static const unsigned long REFRESH_INTERVAL = 1000; // ms
  static unsigned long lastRefreshTime = 0;
  
  if(millis() - lastRefreshTime >= REFRESH_INTERVAL)
  {
    lastRefreshTime += REFRESH_INTERVAL;
                refreshDisplay();
  }

*/
