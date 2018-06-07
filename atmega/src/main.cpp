#include <Arduino.h>
#define DETECT_LOST_CONNECTION_MS 3000
#define MOTOR_L_B 4
#define MOTOR_L_F 5
#define MOTOR_L_PWM 6
#define MOTOR_R_B 7
#define MOTOR_R_F 8
#define MOTOR_R_PWM 9
#define MOTOR_STBY 10

unsigned long lastCommunicatedAt = 0;
unsigned long detectLostAt = 0;
String currentMotorL = "";
String currentMotorR = "";

void updateLastCommunicatedAt() {
  lastCommunicatedAt = millis();
  detectLostAt = lastCommunicatedAt + (unsigned long) DETECT_LOST_CONNECTION_MS;
}

void setup() {
  Serial.begin(115200);
  pinMode(MOTOR_L_B, OUTPUT);
  pinMode(MOTOR_L_F, OUTPUT);
  pinMode(MOTOR_L_PWM, OUTPUT);
  pinMode(MOTOR_R_B, OUTPUT);
  pinMode(MOTOR_R_F, OUTPUT);
  pinMode(MOTOR_R_PWM, OUTPUT);
  pinMode(MOTOR_STBY, OUTPUT);
}

String splittedValue(String value, int index) {
  char splitChar = ' ';
  int spaceIndex;

  // Skip values before index
  for (int i = 0; i < index; ++i) {
    spaceIndex = value.indexOf(splitChar);
    if (spaceIndex == -1) {
      return "";
    }
    value = value.substring(spaceIndex + 1);
  }

  // Get target index value
  spaceIndex = value.indexOf(splitChar);
  if (spaceIndex == -1) {
    return value;
  }
  return value.substring(0, spaceIndex);
}

void setMotorSpeed(String value, int b_pin, int f_pin, int pwm_pin) {
  if (value == "b" || value == "brake") {
    digitalWrite(f_pin, HIGH);
    digitalWrite(b_pin, HIGH);
    analogWrite(pwm_pin, 0);
    return;
  }
  int intValue = value.toInt();
  if (intValue == 0) {
    digitalWrite(f_pin, LOW);
    digitalWrite(b_pin, LOW);
  } else if (intValue > 0) {
    digitalWrite(f_pin, HIGH);
    digitalWrite(b_pin, LOW);
  } else {
    digitalWrite(f_pin, LOW);
    digitalWrite(b_pin, HIGH);
  }
  analogWrite(pwm_pin, abs(intValue));
}

void setMotorsSpeed(String left, String right) {
  digitalWrite(MOTOR_STBY, HIGH);
  setMotorSpeed(left, MOTOR_L_B, MOTOR_L_F, MOTOR_L_PWM);
  setMotorSpeed(right, MOTOR_R_B, MOTOR_R_F, MOTOR_R_PWM);
}

void sleepMotors() {
  setMotorsSpeed("0", "0");
  digitalWrite(MOTOR_STBY, LOW);
}

void executeCommand(String command) {
  if (command.startsWith("motors ")) {
    String left = splittedValue(command, 1);
    String right = splittedValue(command, 2);
    if (left.length() > 0 && right.length() > 0) {
      currentMotorL = left;
      currentMotorR = right;
      setMotorsSpeed(left, right);
      updateLastCommunicatedAt();
    }
  } else if (command == "sleep") {
    sleepMotors();
    updateLastCommunicatedAt();
  } else if (command == "status") {
    Serial.println("Show status");
    Serial.println("L: " + currentMotorL);
    Serial.println("R: " + currentMotorR);
    updateLastCommunicatedAt();
  }
}

void loop() {
  static String command = "";
  if (Serial.available() > 0) {
    while (Serial.available() > 0) {
      char c = Serial.read();
      if (c == ';') {
        executeCommand(command);
        command = "";
      } else if (c == '\n' || c == '\r' || c == '\t' || c == ' ') {
        // replace change line or tab as a white space
        if (command.length() > 0 && !command.endsWith(" ")) {
          command += ' ';
        }
      } else {
        command += c;
      }
    }
  } else {
    delay(10);
  }
  if (detectLostAt < millis()) {
    currentMotorL = "";
    currentMotorR = "";
    sleepMotors();
  }
  // Serial.println("command: " + command);
  // for (int i = 0; i < 5; ++i) {
  //   Serial.println(command.indexOf(' '));
  //   Serial.println(String(i) + " [" + splittedValue(command, i) + "]");
  // }
}
