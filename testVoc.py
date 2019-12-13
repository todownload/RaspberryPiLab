import wiringpi
import time

trig_pin = 3
echo_pin = 4
sampleNum = 2

wiringpi.wiringPiSetupGpio() # set up
wiringpi.pinMode(trig_pin, wiringpi.GPIO.OUTPUT)
wiringpi.pinMode(echo_pin, wiringpi.GPIO.INPUT)

def getDistance():
    wiringpi.digitalWrite(trig_pin,1) # write HIGH
    time.sleep(0.000015) # send 15 us
    wiringpi.digitalWrite(trig_pin,0) # write LOW
    while not wiringpi.digitalRead(echo_pin):
        pass
    t1 = time.time() # start at HIGH begin
    while wiringpi.digitalRead(echo_pin):
        pass
    t2 = time.time() # end at HIGH end
    distance = (t2-t1)*34000/2
    return distance

def getAvaDistance(): # get ava distance
    avaDistance = 0
    for i in range(0,sampleNum):
        avaDistance += getDistance()
    return (avaDistance/2)

while True:
    x = getAvaDistance()
    print(x)
    wiringpi.delay(1000)
