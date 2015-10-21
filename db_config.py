import sqlite3
db_name = 'fuel_mileage.db'
conn = sqlite3.connect(db_name)

def cursor():
  return conn.cursor()

def commit():
    conn.commit()

def stuffs():
     print 'this works'
