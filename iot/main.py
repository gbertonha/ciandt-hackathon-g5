import time, threading, signal
import random
import RPi.GPIO as GPIO
import datetime
import subprocess
import firebase_admin
import Adafruit_DHT
from firebase_admin import credentials
from firebase_admin import firestore
from pytz import timezone
from vendor.Adafruit_BMP085.Adafruit_BMP085 import BMP085

class Iot(object):
    # Be careful to change this value, because Firebase free acc has a limit
    interval = 20
    db = None
    sensor1Pin = 18
    bmp = BMP085(0x77, debug=True)

    def __init__(self):
        # setup
        GPIO.setmode(GPIO.BCM)
        # Use a service account
        cred = credentials.Certificate('key.json')
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def sensor1(self):
        humidity, temperature = Adafruit_DHT.read_retry(11, self.sensor1Pin)
        print(humidity)
        print(temperature)
        if temperature is not None:
          self.sendToFirestore('sensor1', round(temperature, 2))
        if humidity is not None:
          self.sendToFirestore('sensor2', round(humidity, 2))
    
    def sensor2(self):
        pressure = self.bmp.readPressure()
        print(pressure)
        if pressure is not None:
            print("Sensor2 Detected!")
            self.sendToFirestore('sensor3', int(round(pressure / 100.0, 2)))

    def sensor3(self, channel):
        if GPIO.input(channel):
            print("Sensor3 Detected!")
            self.sendToFirestore('sensor3', random.randint(1,100))

    def sendToFirestore(self, collection, value):
        doc_ref = self.db.collection(collection).get()

        try:
            for doc in doc_ref:                
                item = self.db.collection(collection).document(doc.id)
                item.set({
                    u'value': value
                }, merge=True)
        except Exception as e:
            print(str(e))

    def run(self):
        try:
            while True:
                self.sensor1()
                self.sensor2()
                time.sleep(self.interval)

        finally:
            GPIO.cleanup()

if __name__ == '__main__':
    m = Iot()
    m.run()
