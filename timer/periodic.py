import time
from threading import Timer

def cb():
    print '{}'.format(time.ctime())

class PeriodicTask(object):
    def __init__(self, interval, callback, daemon=False, *args,  **kwargs):
        self.interval = interval
        self.callback = callback
        self.daemon   = daemon
        self.kwargs   = kwargs
        self.args     = args

    def run(self):
        self.callback(*self.args, **self.kwargs)
        t = Timer(self.interval, self.run)
        t.daemon = self.daemon
        t.start()

if __name__ == '__main__':
    task = PeriodicTask(interval = 3, callback = cb)
    task.run()
