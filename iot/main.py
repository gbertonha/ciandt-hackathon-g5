"""This is the main program"""
import time

import RPi.GPIO as GPIO

import Adafruit_DHT

from vendor.Adafruit_BMP085.Adafruit_BMP085 import BMP085

import firebase_admin
from firebase_admin import credentials, firestore

class Iot(object):
    """This is the Iot main class.

    Args:
        object (Object): Class reference.
    """

    # Be careful to change this value, because Firebase free acc has a limit.
    #This represents the read interval in seconds.
    interval = 300
    database = None
    temperatureAndHumidityPin = 18
    bmp = BMP085(0x77)

    def __init__(self):
        # setup
        GPIO.setmode(GPIO.BCM)
        # Use a Firebase service account
        cred = credentials.Certificate('key.json')
        firebase_admin.initialize_app(cred)
        self.database = firestore.client()

    def temperature_and_humidity_sensor(self):
        """This method gets the temperature and humidity values
           from the sensors and sends them to Firebase.

           Args:
                self (Context): Context reference
        """
        humidity, temperature = Adafruit_DHT.read_retry(11, self.temperatureAndHumidityPin)
        print(humidity)
        print(temperature)
        if temperature is not None:
            self.send_to_firestore('temperature', round(temperature, 2))
        if humidity is not None:
            self.send_to_firestore('humidity', round(humidity, 2))

    def pressure_sensor(self):
        """This method gets the pressure value
           from the sensors and sends them to Firebase.

           Args:
                self (Context): Context reference.
        """

        pressure = self.bmp.readPressure()
        print(pressure)
        if pressure is not None:
            self.send_to_firestore('pressure', int(round(pressure / 100.0, 2)))

    def send_to_firestore(self, collection, value):
        """This method sends the values
           to the Firebase Firestore collection.

           Args:
                self (Context): Context reference.
                collection (String): Firestore collection name.
                value (int): sensor value to be stored
        """

        doc_ref = self.database.collection(collection).stream()

        try:
            for doc in doc_ref:
                item = self.database.collection(collection).document(doc.id)
                item.set({
                    u'value': value
                }, merge=True)
        except Exception as exception:
            print(str(exception))

    def run(self):
        """This method runs the sensors and collects data.

           Args:
                self (Context): Context reference.
        """
        try:
            while True:
                self.temperature_and_humidity_sensor()
                self.pressure_sensor()
                time.sleep(self.interval)

        finally:
            GPIO.cleanup()

if __name__ == '__main__':
    MAIN = Iot()
    MAIN.run()
