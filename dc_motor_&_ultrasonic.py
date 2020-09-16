from gpiozero import DistanceSensor
from gpiozero import Motor
from time import sleep

sensor = DistanceSensor(echo=21, trigger=20)

motor1 = Motor(enable=2, forward=4, backward=3)
motor2 = Motor(enable=17, forward=27, backward=22)

while True:
#     i = sensor.distance
    if sensor.distance < .10:
        motor1.forward(speed=.2)
        motor2.forward(speed=.2)
        print(sensor.distance)

    if sensor.distance > .10:
        motor1.backward(speed=.2)
        motor2.backward(speed=.2)
        print(sensor.distance)
        