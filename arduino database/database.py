import sqlite3
import serial
from datetime import datetime
import time

port = "/dev/ttyACM0"
arduino_serial = serial.Serial(port, 115200)
arduino_serial.flush()
time.sleep(2)
database = sqlite3.connect('server.db')
databsepointer = database.cursor()

databsepointer.execute('CREATE TABLE  IF NOT EXISTS tempArduino(temp FLOAT, date TEXT)')


def readserial():
    while 1:
        if arduino_serial.inWaiting() > 0:
            inputA = arduino_serial.read(5)
            time.sleep(2)
            databsepointer.execute("INSERT INTO tempArduino(temp, date) VALUES (?,?)", (inputA, str(datetime.now())))
            database.commit()


if __name__ == "__main__":
    readserial()
