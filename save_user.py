#!/usr/bin/env python

//These imports will allow us to use prewritten libraries to execute certain functions easier
import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import mysql.connector
import Adafruit_CharLCD as LCD

//This initializes connection to the SQL database
db = mysql.connector.connect(
  host="localhost",
  user="attendanceadmin",
  passwd="pimylifeup",
  database="attendancesystem"
)

cursor = db.cursor()
reader = SimpleMFRC522()
lcd = LCD.Adafruit_CharLCD(4, 24, 23, 17, 18, 22, 16, 2, 4);

//If there is no current card, request one
try:
  while True:
    lcd.clear()
    lcd.message('Place Card to\nregister')
    id, text = reader.read()
    cursor.execute("SELECT id FROM users WHERE rfid_uid="+str(id))
    cursor.fetchone()
    
    //Once a card is recognized, check for exiting info and ask for overwrite permission if card isn't blank
    if cursor.rowcount >= 1:
      lcd.clear()
      lcd.message("Overwrite\nexisting user?")
      overwrite = input("Overwite (Y/N)? ")
      if overwrite[0] == 'Y' or overwrite[0] == 'y':
        lcd.clear()
        lcd.message("Overwriting user.")
        time.sleep(1)
        // All of the sql clls here insert the data from the card into the SQL server
        sql_insert = "UPDATE users SET name = %s WHERE rfid_uid=%s"
      else:
        continue;
    else:
      sql_insert = "INSERT INTO users (name, rfid_uid) VALUES (%s, %s)"
    lcd.clear()
    lcd.message('Enter new name')
    new_name = input("Name: ")

    cursor.execute(sql_insert, (new_name, id))
    
    //This officially commits the data in the script to the SQL database
    db.commit()

    lcd.clear()
    lcd.message("User " + new_name + "\nSaved")
    time.sleep(2)
finally:
  GPIO.cleanup()
