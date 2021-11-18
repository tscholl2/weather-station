import bme280
import smbus2
import sensor_logger
import time


class BME280Sensor(sensor_logger.SensorLogger):
    def setup(self):
        port = 1
        self.address = 0x77  # Adafruit BME280 address. Other BME280s may be different
        self.bus = smbus2.SMBus(port)
        self.calibration = bme280.load_calibration_params(self.bus, self.address)

    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS bme280 (
	timestamp NUMBER PRIMARY KEY NOT NULL,
    humidity NUMBER,
    pressure NUMBER,
    temperature NUMBER
);"""

    def run(self):
        while True:
            now = self.now()
            bme280_data = bme280.sample(self.bus, self.address,self.calibration)
            humidity = bme280_data.humidity
            pressure = bme280_data.pressure
            temperature = bme280_data.temperature
            self.insert(sql="INSERT INTO bme280 (timestamp,humidity,pressure,temperature) VALUES (?,?,?,?)",
                        parameters=[now, humidity, pressure, temperature, ])
            time.sleep(30)
