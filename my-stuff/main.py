import multiprocessing
import time
from fake import FakeSensor
import queue
import sqlite3

DATABASE = "data.sqlite.db"


if __name__ == '__main__':
    ctx = multiprocessing.get_context('spawn')
    q = ctx.Queue(maxsize=10000)
    sensors = [
        FakeSensor(q),
        FakeSensor(q),
    ]
    processes = [
        multiprocessing.Process(target=s)
        for s in sensors
    ]
    for p in processes:
        p.start()
    while True:
        time.sleep(5)
        con = sqlite3.connect(DATABASE)
        con.executescript("\n".join(s.schema() for s in sensors))
        try:
            item = q.get(block=True, timeout=5)
            con.execute(**item)
            print(f"item! '{item}'")
        except queue.Empty:
            pass
        con.commit()
        con.close()
        # TODO: run backup
