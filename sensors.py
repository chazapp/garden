from threading import Thread
from time import sleep
from gpiozero import MCP3008

class Sensors():
    def __init__(self):
        self.humidity = MCP3008(channel=0)
        self.temperature = MCP3008(channel=1)
        self.light = MCP3008(channel=2)
        pass

