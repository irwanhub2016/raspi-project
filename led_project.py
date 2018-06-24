import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11
kipasPin = 13

def setup():
  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  GPIO.setup(LedPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.setup(kipasPin, GPIO.OUT)   # Set LedPin's mode is output
  GPIO.output(LedPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led
  GPIO.output(kipasPin, GPIO.HIGH) # Set LedPin high(+3.3V) to turn on led


def blink():
  while True:
    print('Program start ...')    
    GPIO.output(LedPin, GPIO.HIGH)  # led on
    time.sleep(0.05)
    GPIO.output(LedPin, GPIO.LOW) # led off
    time.sleep(0.05)
    GPIO.output(kipasPin, GPIO.HIGH)  # led on
    time.sleep(0.05)
    GPIO.output(kipasPin, GPIO.LOW) # led off
    time.sleep(0.05)

def destroy():
  GPIO.output(LedPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource
  GPIO.output(kipasPin, GPIO.LOW)   # led off
  GPIO.cleanup()                  # Release resource

if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()
