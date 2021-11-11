#!/usr/bin/python3

import subprocess
import re
import sensor_logger
import time


def cpu_temp():
    with open("sys/class/thermal/thermal_zone0/temp") as f:
        raw = f.read()
        return float(raw)/1000


def gpu_temp():
    result = subprocess.run(["/opt/vc/bin/vcgencmd", "measure_temp"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    m = re.search(br"(\d+\.\d+)", result.stdout)
    if m:
        return float(m.groups()[0].decode())
    else:
        print(f"FAIL: gpu temp: {result.stderr}")


class OnBoardSensors(sensor_logger.SensorLogger):
    def schema(self):
        return f"""
CREATE TABLE IF NOT EXISTS onboard (
	timestamp NUMBER PRIMARY KEY NOT NULL,
    cpu_temp NUMBER,
    gpu_temp NUMBER
);
"""

    def run(self):
        while True:
            self.insert(sql="INSERT INTO onboard VALUES (?,?,?)", params=[
                self.now(),
                cpu_temp(),
                gpu_temp()])
            time.sleep(1)
