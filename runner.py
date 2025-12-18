
from threading import Thread
import time
from khanjar_engine import KhanjarSupremeV5
from notifier import notify

class KhanjarRunner:
    def __init__(self, cb):
        self.cb = cb
        self.running = False

    def loop(self):
        engine = KhanjarSupremeV5()
        while self.running:
            self.cb('Scanning...')
            engine.run()
            notify('KHANJAR', 'Scan completed')
            time.sleep(60)

    def start(self):
        if self.running: return
        self.running = True
        Thread(target=self.loop, daemon=True).start()

    def stop(self):
        self.running = False
        self.cb('Stopped')
