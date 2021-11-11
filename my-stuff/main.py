import multiprocessing
import time
from fake import FakeSensor
import queue

DATABASE = "data.sqlite.db"


if __name__ == '__main__':
    ctx = multiprocessing.get_context('spawn')
    q = ctx.Queue(maxsize=1000)
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
    time.sleep(5)
    while True:
        try:
            item = q.get(block=True, timeout=5)
            print(f"item! '{item}'")
        except queue.Empty:
            pass

"""
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
"""
