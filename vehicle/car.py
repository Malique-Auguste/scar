import motors

class Car:

    def __init__(self, motors, sensors):
        self.motors = motors
        self.sensors = sensors

        return self
    
    def move(self, direction):
        for motor in self.motors:
            motor.move()
            