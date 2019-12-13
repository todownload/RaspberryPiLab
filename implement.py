
import wiringpi
import time

"""
Connect it. Make it when left_high=HIGH left_low=LOW right_high=HIGH right_low=LOW
the car is forward.
"""

# all the below are use GPIO
left_high = 13
left_low = 19
right_high = 18
right_low = 12
speed_scale = 40 # PWM speed

# about Voice
trig_pin = 3
echo_pin = 4
sampleNum = 2

# about Red
red_pinL = 2 # Left one
red_pinR = 14 # Right One

# about border
right_d = 40 # turn right distance
left_dL = 1000 # turn left consider the distance will be very big when very close

def init():
    wiringpi.wiringPiSetupGpio()
    # pin Mode about car
    wiringpi.pinMode(left_high,wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(left_low,wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(right_high,wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(right_low,wiringpi.GPIO.OUTPUT)
    # pin Mode about Red
    wiringpi.pinMode(red_pinL, wiringpi.GPIO.INPUT)
    wiringpi.pinMode(red_pinR, wiringpi.GPIO.INPUT)
    # pin Mode about Voc
    wiringpi.pinMode(trig_pin, wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(echo_pin, wiringpi.GPIO.INPUT)
    # create PWM
    wiringpi.softPwmCreate(left_high,0,100)
    wiringpi.softPwmCreate(left_low,0,100)
    wiringpi.softPwmCreate(right_high,0,100)
    wiringpi.softPwmCreate(right_low,0,100)

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


def forward(t):# car forward
    wiringpi.softPwmWrite(left_high,speed_scale)
    wiringpi.softPwmWrite(left_low,0)
    wiringpi.softPwmWrite(right_high,speed_scale)
    wiringpi.softPwmWrite(right_low,0)
    wiringpi.delay(t*100)

def back(t): # back
    wiringpi.softPwmWrite(left_high,0)
    wiringpi.softPwmWrite(left_low,speed_scale)
    wiringpi.softPwmWrite(right_high,0)
    wiringpi.softPwmWrite(right_low,speed_scale)
    wiringpi.delay(t*100)

def stop(t): # stop
    wiringpi.softPwmWrite(left_high,0)
    wiringpi.softPwmWrite(left_low,0)
    wiringpi.softPwmWrite(right_high,0)
    wiringpi.softPwmWrite(right_low,0)
    wiringpi.delay(t*100)

def turnRight(t): # turn right the car
    wiringpi.softPwmWrite(left_high,speed_scale)
    wiringpi.softPwmWrite(left_low,0)
    wiringpi.softPwmWrite(right_high,0)
    wiringpi.softPwmWrite(right_low,0)
    wiringpi.delay(t*100)

def turnLeft(t): # turn left the car
    wiringpi.softPwmWrite(left_high,0)
    wiringpi.softPwmWrite(left_low,0)
    wiringpi.softPwmWrite(right_high,speed_scale)
    wiringpi.softPwmWrite(right_low,0)
    wiringpi.delay(t*100)


def main():
    init()

    while True:
        distance = getAvaDistance() # get ava distance
        lf = wiringpi.digitalRead(red_pinL) # left Red
        rf = wiringpi.digitalRead(red_pinR) # right Red
        if (distance>right_d):
            turnRight(5)
        elif lf==0 and rf==0 and (distance<right_d or distance>left_dL):
            back(1)
            turnLeft(5)
        elif lf==0 and rf==1:
            back(0.5)
            turnRight(1)
        elif rf==0 and lf==1:
            back(0.5)
            turnLeft(1)
        else:
            forward(5)


if __name__ == "__main__":
    main()
