from gpiozero import Button
import sensor_logger


class RainSensor(sensor_logger.SensorLogger):
    def __init__(self):
        super().__init__()
        self.button = Button("GPIO6")

    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS rain (
	timestamp NUMBER PRIMARY KEY NOT NULL
);"""

    def run(self):
        while True:
            print("waiting")
            self.button.wait_for_press()
            print("pressed!")
            self.button.wait_for_release()
            print("released!")
            self.insert(sql="INSERT INTO rain VALUES (?)", params=[self.now()])
