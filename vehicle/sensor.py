from gpiozero import DistanceSensor

class RealSensor:
    def __init__(self, echo, trigger):
        self.inner = DistanceSensor(echo = echo, trigger = trigger)
        return self
    
