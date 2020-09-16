import timeit
from gpiozero import DistanceSensor, Motor, AngularServo
# from gpiozero import Motor
# from gpiozero import AngularServo
from gpiozero.tools import sin_values
import time

motor1 = Motor(enable=2, forward=3, backward=4)
motor2 = Motor(enable=17, forward=22, backward=27)

servo1 = AngularServo(14, min_angle=-90, max_angle=90)
servo2 = AngularServo(16, min_angle=-90, max_angle=90)

sensor = DistanceSensor(echo=21, trigger=20)

SPEED = .15
# STARTING_ANGLE = 0
# ANGLE = STARTING_ANGLE
angle = 0
right = True
timestamp = time.time()

# class servo:
#     
#     def __init__(self, init_angle):
#         self.angle = init_angle
#         
#     def sweep(self):
#         self.source = sin_values()

def servosweep(angle):
    if time.time() - timestamp > 1:
        timestamp = time.time()
        if right == True:
            angle = angle + 1
#         print("addition: ", angle + angle)
            if angle == 90:
                angle = angle - 2
                right == False
        if right == False:
            angle = angle - 1
            if angle == -91:
                angle = angle + 2
                right == True
    return angle

while True:
    i = sensor.distance
    
    print("angle: ", servosweep(servo2.angle))
    servo2.angle = servosweep(servo2.angle)
#     print(servo2.angle)

#    if i > .50:
#         print("> .10")
#        motor1.forward(speed=.4)
#        motor2.forward(speed=.4)
#        print(sensor.distance)
        
    if i < .50:
#         print("< .10")
#        print(sensor.distance)
        motor1.stop()
        motor2.stop()
        # backup and turn
        servo1.angle = -90
        motor1.backward(speed=SPEED)
        motor2.backward(speed=SPEED)
        time.sleep(1.5)
        
        # turn wheels other way and move forward a bit
        servo1.angle = 90
        motor1.forward(speed=SPEED)
        motor2.forward(speed=SPEED)
        time.sleep(1.5)
        servo1.angle = 0
#         servo2.source = sin_values()
    else:
        motor1.forward(speed=SPEED)
        motor2.forward(speed=SPEED)
#         servo2.source = sin_values()
#    start = timeit.timeit()
#     servo2.source = sin_values()
    time.sleep(.00000001)
