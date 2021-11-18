#!/usr/bin/python3
import re
import time
import sys
import sensor_logger


def sample():
    # https://jumpnowtek.com/rpi/Using-DS18B20-1-wire-Temp-Sensors-with-the-Raspberry-Pi.html
    # The 28 means DS18B20
    # The 00000003e658 is the HW id
    for _ in range(3):
        with open("/sys/bus/w1/devices/28-00000003e658/w1_slave") as f:
            lines = f.readlines()
            if not re.search("YES$", lines[0]):
                print("CRC fail")
                continue
            m = re.search(r"t=([0-9]+)", lines[1])
            if not m:
                print("no temp found")
                continue
            return float(m.group(1))/1000


class DS18B20Sensor(sensor_logger.SensorLogger):
    def setup(self):
        pass

    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS ds18b20 (
	timestamp NUMBER PRIMARY KEY NOT NULL,
    temperature NUMBER
);"""

    def run(self):
        while True:
            try:
                now = self.now()
                temp = sample()
                assert(temp is not None)
                self.insert(sql="INSERT INTO ds18b20 (timestamp,temperature) VALUES (?,?)",
                            parameters=[now, temp])
            except Exception as e:
                print("Cant read DS18B20", file=sys.stderr)
            time.sleep(30)
