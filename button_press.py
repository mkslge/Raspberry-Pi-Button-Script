import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pin_value = 19 #CHANGE THIS TO THE PIN YOU'RE TESTING
GPIO.setup(pin_value, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Success Message!
def button_pressed(channel):
        print("Button has been pressed")

#add event listener
GPIO.add_event_detect(pin_value, GPIO.FALLING, callback=button_pressed, bouncetime=100)

#Wait until button is pressed
try:
        print("Press the button!")
        while True:
                time.sleep(0.1)

except KeyboardInterrupt:
        printf("Bye Bye ):")
finally:
        GPIO.cleanup()
