import db_config
import sqlite3
#db_name = 'fuel_mileage.db'
#conn = sqlite3.connect(db_name)

db_conn = db_config.cursor()
try:
    db_conn.execute('''CREATE TABLE fuel
                        (mileage float, gallons float, pricepergallon float,
                        mpg float, vehicle int)''')
except Exception, e:
    #print 'some db error'
    print 'error =>', e


def store_current_mileage(miles):
    the_miles = (miles,)
    db_conn.execute('INSERT INTO fuel (mileage) VALUES (?)', the_miles)
    db_config.commit()
