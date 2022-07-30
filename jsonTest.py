#!/usr/bin/env python3

# Import modules
import json
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        # Promt status
        print("Waiting for you to scan an RFID sticker/card")
        
        # Read card
        id = reader.read()[0]
        print("The ID for this card is:", id)
        
        # Read JSON data
        with open('RFIDs.json', 'r') as myfile:
            data=myfile.read()

        # Load the json data
        rfids = json.loads(data)

        # Define a search function
        def search_rfid (rfid):
        for keyval in rfids:
        if rfid.lower() == keyval['RFId'].lower():
        return keyval['SpotifyId']

        # Check if RFID is stored and return SpotifyId
        if (search_rfid(rfid) != None):
        print("The SpotifyId is:", search_rfid(rfid))

finally:
        GPIO.cleanup()