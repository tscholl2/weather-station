#!/usr/bin/python3

import sqlite3
import datetime

class SensorLogger:
  def __init__(self,database="data.db"):
    self.db = database
    self.reconnect()
    self.cur.execute(self.schema())
    self.con.connect()
  
  def reconnect(self):
    self.con = sqlite3.connect(self.db)
    self.cur = self.con.cursor()

  def now(self):
      return datetime.datetime.now().timestamp()

  def schema():
    raise Exception("unimplemented")
  
  def insert(*args,**kwargs):
    raise Exception("unimplemented")

  def run(self):
    raise Exception("unimplemented")
