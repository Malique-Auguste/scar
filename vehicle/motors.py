from gpiozero import Motor

class Direction:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class VirtualMotor:
    def __init__(self):
        self.direction = Direction(0,0)
    
    def move(self, direction):
        self.direction = direction

class RealMotor:

    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.direction = Direction(0,0)
        return self
    
    def move(self, direction):
        #Initialises driving speed of vehicle to forward direction
        left_motor_speed = direction.y
        right_motor_speed = direction.y

        #If vehicle is turning right (>0), left_motor goes forward and right motor backwards, and vice versa
        if direction.x > 0:
            left_motor_speed += direction.x
            right_motor_speed -= direction.x
        elif direction.x < 0:
            left_motor_speed -= direction.x
            right_motor_speed += direction.x

        #If the left motor speed is >=0 it is rotating forward, however if it is <0 it is rotating backward. 
        # The input variable of the backward function is positive and thus the polarity of the input must be flipped 
        if left_motor_speed >= 0.0:
            self.left_motor.forward(left_motor_speed)
        else:
            self.left_motor.backward(left_motor_speed * -1.0)
        

        if right_motor_speed >= 0.0:
            self.right_motor.forward(right_motor_speed)
        else:
            self.right_motor.backward(right_motor_speed * -1.0)

    