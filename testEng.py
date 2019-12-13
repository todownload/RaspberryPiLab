
import wiringpi

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

def init():
    wiringpi.wiringPiSetupGpio()
    # pin Mode
    wiringpi.pinMode(left_high,wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(left_low,wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(right_high,wiringpi.GPIO.OUTPUT)
    wiringpi.pinMode(right_low,wiringpi.GPIO.OUTPUT)
    # create PWM
    wiringpi.softPwmCreate(left_high,0,100)
    wiringpi.softPwmCreate(left_low,0,100)
    wiringpi.softPwmCreate(right_high,0,100)
    wiringpi.softPwmCreate(right_low,0,100)

def forward():# car forward
    wiringpi.softPwmWrite(left_high,speed_scale)
    wiringpi.softPwmWrite(left_low,0)
    wiringpi.softPwmWrite(right_high,speed_scale)
    wiringpi.softPwmWrite(right_low,0)

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

def test():
    forward()
    wiringpi.delay(200)
    turnRight(2)
    back(2)
    turnLeft(2)
    stop(10)

def main():
    init()
    test()

if __name__ == "__main__":
    main()
