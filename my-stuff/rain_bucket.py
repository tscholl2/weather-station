import time
from gpiozero import Button
import sensor_logger
import atomic_counter


class RainBucketSensor(sensor_logger.SensorLogger):
    def setup(self):
        self.button = Button("GPIO6")
        self.counter = atomic_counter.AtomicCounter()
        self.button.when_pressed = self.when_pressed

    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS rain_bucket (
	timestamp NUMBER PRIMARY KEY NOT NULL,
    count NUMBER
);"""

    def when_pressed(self):
        self.counter.increment()

    def run(self):
        while True:
            now = self.now()
            val = self.counter.reset()
            self.insert(sql="INSERT INTO rain_bucket VALUES (?,?)",
                        parameters=[now, val])
            time.sleep(5)
