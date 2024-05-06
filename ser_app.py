import serial
import RPi.GPIO as GPIO
import time

# Setup for GPIO
speaker_pin = 17  # Change as per your connection
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbering
GPIO.setup(speaker_pin, GPIO.OUT)

# Open serial port
ser = serial.Serial('/dev/ttyUSB0', 9600)

def beep(duration):
    GPIO.output(speaker_pin, GPIO.HIGH)  # Turn speaker on
    time.sleep(duration)  # Duration of beep
    GPIO.output(speaker_pin, GPIO.LOW)  # Turn speaker off
    time.sleep(duration)  # Time between beeps

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            distance = int(data)  # Assuming data is just the distance in cm
            print(f"Distance: {distance} cm")

            # Check distance threshold
            if distance < 20:  # Threshold distance in cm
                beep(0.1)  # Beep for 0.1 seconds if too close
except KeyboardInterrupt:
    print("Program terminated!")
finally:
    ser.close()
    GPIO.cleanup()  # Cleanup GPIO to ensure all pins are reset