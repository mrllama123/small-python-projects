import sqlite3
import serial
from datetime import datetime
import time

port = "/dev/ttyUSB0"
arduino_serial = serial.Serial(port, 115200)
arduino_serial.flush()
time.sleep(2)
database = sqlite3.connect('server.db')
databsepointer = database.cursor()
databsepointer.execute("CREATE TABLE  IF NOT EXISTS temparduino(temp REAL,humid REAL, date TEXT)")

def readserial():

    while 1:
        if arduino_serial.inWaiting() > 0:
            data = arduino_serial.readline()
            # ["b'42.80", "42.80\\r\\n'"]
            # ['2016-07-15', '13:24:02.886386']
            d = str(data)
            values = d.split(" ")
            v1 = values[0]
            v2 = values[1]
            temp_val = float(v1[2:])
            humid_val = float(v2[:5])
            date = str(datetime.now())
            time_stamp = date.split(" ")
            current_time = time_stamp[1]
            time_val = time_stamp[0]+" "+current_time[:5]
            databsepointer.execute("INSERT INTO temparduino(temp,humid,date) VALUES (?,?,?)", (temp_val, humid_val,time_val))
            database.commit()
            time.sleep(1800)


if __name__ == "__main__":
    readserial()
