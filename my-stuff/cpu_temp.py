#!/usr/bin/python3

import subprocess
import re

def cpu_temp():
    with open("sys/class/thermal/thermal_zone0/temp") as f:
        raw = f.read()
        return f"{float(raw)/1000:0.2f}"

def gpu_temp():
    result = subprocess.run(["/opt/vc/bin/vcgencmd", "measure_temp"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    m = re.search(br"(\d+\.\d+)",result.stdout)
    if m:
        return m.groups()[0].decode()
    else:
        print(f"FAIL: gpu temp: {result.stderr}")