import db_config
import sqlite3

db_conn = db_config.cursor()
try:
    db_conn.execute('''CREATE TABLE fuel
                        (mileage float, gallons float, pricepergallon float,
                        mpg float, vehicle int)''')
except Exception, e:
    #print 'some db error'
    print 'error =>', e


def store_current_data(miles, gallons, price_per_gallon):
    the_miles = (miles, gallons, price_per_gallon)
    db_conn.execute('''INSERT INTO fuel (mileage, gallons, pricepergallon)
    VALUES (?, ?, ?)''', the_miles)
    db_config.commit()

def get_all_data():
  return db_conn.execute('SELECT * FROM fuel')

def get_last_entry():
  return db_conn.execute('SELECT * from fuel where oid = (select max(oid) from fuel)')
