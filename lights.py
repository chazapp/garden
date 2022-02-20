from datetime import time

from flask import g
from gpiozero import TimeOfDay, PWMLED

class Lights:
    def __init__(self):
        self.daytime = TimeOfDay(time(8), time(20))
        self.daytime.when_activated = self.onActivate
        self.daytime.when_deactivated = self.onDeactivate
        self.red = PWMLED("GPIO16")
        self.green = PWMLED("GPIO20")
        self.blue = PWMLED("GPIO21")

    def onActivate(self):
        self.red.value = 1
        self.green.value = 1
        self.blue.value = 1
        self.red.on()
        self.green.on()
        self.blue.on()
        
    def onDeactivate(self):
        self.red.value = 0
        self.green.value = 0
        self.blue.value = 0
        self.red.off()
        self.green.off()
        self.blue.off()
