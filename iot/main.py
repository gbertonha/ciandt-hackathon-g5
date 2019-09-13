import time, threading, signal
import random
import RPi.GPIO as GPIO
import datetime
import subprocess
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from pytz import timezone


class Main:


    def __init__(self):
        sensor1Pin = 16
        sensor2Pin = 21
        sensor3Pin = 20
        GPIO.setmode(GPIO.BCM)

        # Setup
        GPIO.setup(sensor1Pin, GPIO.IN)
        GPIO.setup(sensor2Pin, GPIO.IN)
        GPIO.setup(sensor3Pin, GPIO.IN)

        # Events
        GPIO.add_event_detect(sensor1Pin, GPIO.BOTH, callback=sensor1, bouncetime=300)
        GPIO.add_event_detect(sensor2Pin, GPIO.BOTH, callback=sensor2, bouncetime=300)
        GPIO.add_event_detect(sensor3Pin, GPIO.BOTH, callback=sensor3, bouncetime=300)

        # Use a service account
        cred = credentials.Certificate('key.json')
        firebase_admin.initialize_app(cred)

    def sensor1(self, channel):
        if GPIO.input(channel):
            print("Sensor1 Detected!")
            sendToFirestore('sensor1', random.randint(1,100))

    def sensor2(self, channel):
        if GPIO.input(channel):
            print("Sensor2 Detected!")
            sendToFirestore('sensor2', random.randint(1,100))

    def sensor3(self, channel):
        if GPIO.input(channel):
            print("Sensor3 Detected!")
            sendToFirestore('sensor3', random.randint(1,100))

    def sendToFirestore(self, collection, value):
        doc_ref = db.collection(collection).get()

        try:
            for doc in doc_ref:
                doc.set({
                    u'value': value
                }, merge=True)
        except e:
            print(e)

    def run(self):
        try:
            while True:
                time.sleep(1)

        finally:
            GPIO.cleanup()

    if __name__ == '__main__':