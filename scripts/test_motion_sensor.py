import RPi.GPIO as GPIO
import time

def wake_up_from_sensor(self, cb):
    self.motion_detected += 1
    print("motion detected")
    time.sleep(3)


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

PIN = 26


GPIO.setmode(GPIO.BCM)
GPIO.remove_event_detect(PIN)
GPIO.cleanup()

GPIO.setup(PIN, GPIO.IN)
GPIO.add_event_detect(PIN, GPIO.RISING,
                        callback=wake_up_from_sensor,
                        bouncetime=3000)
