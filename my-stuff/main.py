import multiprocessing
from fake import FakeSensor
from rain_bucket import RainBucketSensor
from wind_speed import WindSpeedSensor
from ds18b20 import DS18B20Sensor
from onboard import OnBoardSensor
from bme280_sensor import BME280Sensor
import queue
import sqlite3

DATABASE = "data.db"


if __name__ == '__main__':
    ctx = multiprocessing.get_context('spawn')
    q = ctx.Queue(maxsize=10000)
    sensors = [
        FakeSensor(q),
        RainBucketSensor(q),
        WindSpeedSensor(q),
        DS18B20Sensor(q),
        OnBoardSensor(q),
        BME280Sensor(q),
    ]
    processes = [
        multiprocessing.Process(target=s)
        for s in sensors
    ]
    for p in processes:
        p.start()
    print("processes started")
    while True:
        con = sqlite3.connect(DATABASE)
        con.executescript("\n".join(s.schema() for s in sensors))
        try:
            item = q.get(block=True, timeout=5)
            print(f"item! '{item}'")

            con.execute(item["sql"],item["parameters"])
        except queue.Empty:
            pass
        con.commit()
        con.close()
        # TODO: run backup
