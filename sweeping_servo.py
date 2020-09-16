from gpiozero import DistanceSensor, Motor, AngularServo
import time

servo2 = AngularServo(16, min_angle=-90, max_angle=90)

initial_angle = -89
SWEEP_SPEED = .005

class Servo:
    
    def __init__(self):
        self.angle = initial_angle
        self.right = True
        self.timestamp = time.time()
    
    def timer(self):
        if time.time() - self.timestamp > SWEEP_SPEED:
            self.timestamp = time.time()
            return True
    
    def sweep(self):
        if self.right == True:
            self.angle += 1
            if self.angle >= 88:
                self.angle -= 2
                self.right = False
        if self.right == False:
            self.angle -= 1
            if self.angle <= -88:
                self.angle += 2
                self.right = True

def main():
    sweep = Servo()
    while True:
        if sweep.timer() == True:
            sweep.sweep()
        servo2.angle = sweep.angle


if __name__ == '__main__':
    main()