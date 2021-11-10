#!/usr/bin/python3

from gpiozero import Button
import sensor_logger

import sqlite3
import datetime

class RainSensor:
  def connect(self):
    print("reconnecting")
    self.button = button = Button("GPIO6")
    self.con = sqlite3.connect('example.db')
    self.cur = self.con.cursor()
    self.cur.execute(open("schema.sql").read())
    self.con.commit()

  def run(self):
    while True:
      try:
        print("waiting")
        self.button.wait_for_press()
        print("pressed!")
        self.button.wait_for_release()
        print("released!")
        t = datetime.datetime.now().timestamp()
        self.cur.execute("INSERT INTO rain VALUES (?)",t)
      except sqlite3.OperationalError:
        self.connect()

if __name__ == "__main__":
  print("ok")
