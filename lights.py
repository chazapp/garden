from datetime import time

from flask import g
from gpiozero import TimeOfDay, PWLED

class Lights:
    def __init__(self):
        self.daytime = TimeOfDay(time(8), time(20))
        self.daytime.when_activated = self.onActivate
        self.daytime.when_deactivated = self.onDeactivate
        self.red = PWLED(16)
        self.green = PWLED(20)
        self.blue = PWLED(21)

    def onActivate(self):
        self.r.value = 1
        self.g.value = 1
        self.b.value = 1

    def onDeactivate(self):
        self.r.value = 0
        self.g.value = 0
        self.b.value = 0
