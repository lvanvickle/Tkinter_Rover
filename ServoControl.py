import RPi.GPIO as GPIO
import time

class ServoControl:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, 50)
        self.pwm.start(0)

    def set_servo_angle(self, angle):
        duty_cycle = (angle / 18.0) + 2
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)
        self.pwm.ChangeDutyCycle(0)  # Avoid jitter

    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()
