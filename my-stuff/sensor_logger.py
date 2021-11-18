import abc
import datetime
import multiprocessing


class SensorLogger(abc.ABC):
    def __init__(self, Q: multiprocessing.Queue):
        self.queue = Q
        self.setup()

    @abc.abstractmethod
    def setup(self):
        raise Exception("unimplemented")

    def now(self):
        return datetime.datetime.now().timestamp()

    def insert(self, **kwargs):
        self.queue.put(kwargs)

    @abc.abstractmethod
    def schema(self):
        raise Exception("unimplemented")

    @abc.abstractmethod
    def run(self):
        raise Exception("unimplemented")

    def __call__(self):
        self.run()
