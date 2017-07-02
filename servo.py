import RPi.GPIO as GPIO


class Servo(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.pwm = GPIO.PWM(18, 100)
        self.pwm.start(5)

    def set_angle(self, angle):
        duty = float(angle) / 10.0 + 2.5
        self.pwm.ChangeDutyCycle(duty)
