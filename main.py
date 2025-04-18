import stepper
from machine import Pin
from time import sleep

# PINS
motor = stepper.HalfStepMotor.frompins(16, 17, 18, 19)
forward = Pin(14, Pin.IN, Pin.PULL_DOWN)
backward = Pin(15, Pin.IN, Pin.PULL_DOWN)
halt = Pin(13, Pin.IN, Pin.PULL_DOWN)
led = Pin("LED", Pin.OUT)

# Set current angle to 0
motor.reset()

clockwise = [0, 90, 180, 270, 0]
c_clockwise = [0, 270, 180, 90, 0]

def clockwise_turn(turns):
    for i in range(turns):
        for angle in clockwise:
            motor.step_until_angle(angle)

        
def c_clockwise_turn(turns):
    for i in range(turns):
        for angle in c_clockwise:
            motor.step_until_angle(angle)

        

try:
    led.high()
    while True:
        with open("turns.txt", "r") as file:
            turns = int(file.read())
        if forward.value() == 1:
            led.low()
            clockwise_turn(5)
            with open("turns.txt", "w") as f:
                f.write(str(turns + 5))
            led.high()
                
        if backward.value() == 1:
            led.low()
            c_clockwise_turn(1)
            with open("turns.txt", "w") as f:
                f.write(str(turns - 1))
            led.high()
        if halt.value() == 1:
            break
    
    led.low()
    motor.step_until_angle(0)
        
except:
    led.low()
    motor.step_until_angle(0)