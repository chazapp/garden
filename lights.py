from threading import Thread

class LightsThread(Thread):
    def __init__(self):
        pass

    def run(self):
        self.running = True
        while self.running:
            pass
        pass