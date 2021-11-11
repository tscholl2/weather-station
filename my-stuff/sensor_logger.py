import datetime
import multiprocessing


class SensorLogger:
    def __init__(self, Q: multiprocessing.Queue):
        self.queue = Q

    def now(self):
        return datetime.datetime.now().timestamp()

    def insert(self, sql="", params=[]):
        self.queue.put({"sql": sql, "params": params})

    def schema(self):
        raise Exception("unimplemented")

    def run(self):
        raise Exception("unimplemented")

    def __call__(self):
        self.run()
