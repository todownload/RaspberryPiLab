"""
Test file
"""
import wiringpi

red_pin = 2

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(red_pin, wiringpi.GPIO.INPUT) # set Input


while True:
    x = wiringpi.digitalRead(red_pin)      # Read pin
    print(x)
    wiringpi.delay(1000)



