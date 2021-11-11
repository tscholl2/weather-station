import sensor_logger
import multiprocessing
import time
import random


class FakeSensor(sensor_logger.SensorLogger):
    def __init__(self, Q: multiprocessing.Queue):
        super().__init__(Q)
        self.name = random.randint(0, 10)

    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS fake (
	timestamp NUMBER PRIMARY KEY NOT NULL
);
"""

    def run(self):
        while True:
            time.sleep(1)
            self.insert(sql="INSERT INTO fake VALUES (?,?)",
                        params=[self.now(), self.name])


if __name__ == "__main__":
    f = FakeSensor()
    f.run()
