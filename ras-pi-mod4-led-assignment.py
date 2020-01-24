import RPi.GPIO as GPIO
import time

PinForLed    = 11    
PinForButton = 12    
SleepTime    = 0.5
def loop():
    while True:
        if GPIO.input(PinForButton)==GPIO.LOW: # if button is pressed
            GPIO.output(PinForLed,GPIO.HIGH)   # turn on led
            print ('led turned on >>>')     
        else : # if button is relessed
            GPIO.output(PinForLed, GPIO.HIGH)  # make led Pin output HIGH to turn led on
            print ('led turned on >>>')     
            time.sleep(SleepTime)              # Wait for given second
            GPIO.output(PinForLed, GPIO.LOW)   # make led Pin output LOW to turn led off
            print ('led turned off <<<')
            time.sleep(SleepTime)              # Wait for given second

def release_resource():
    GPIO.output(PinForLed, GPIO.LOW)     # turn off led 
    GPIO.cleanup()                       # Release GPIO resource

if __name__ == '__main__':
    #Setup mode for the PIN
    GPIO.setmode(GPIO.BOARD)          #use PHYSICAL GPIO Numbering
    GPIO.setup(PinForLed, GPIO.OUT)   #led pin as OUTPUT mode
    GPIO.setup(PinForButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #button pin as PULL UP/DOWN INPUT mode
    
    try:
        loop()
    except KeyboardInterrupt:  #ctrl-c to end the program.
        release_resource()
