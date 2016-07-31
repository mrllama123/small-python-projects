from flask import Flask, render_template
import sqlite3
import pygal
import database

app = Flask(__name__)

DATABASE = "server.db"


def connect_db():
    return sqlite3.connect(DATABASE)


def get_temp():
    db = connect_db()
    temp = []
    cur = db.execute('SELECT temp FROM temparduino')
    for t in cur:
        temp.append(t[0])
    db.close()
    return temp


def get_hu():
    db = connect_db()
    hu = []
    cur = db.execute('SELECT humid FROM temparduino')
    for t in cur:
        hu.append(t[0])
    db.close()
    return hu


def get_date_time():
    db = connect_db()
    dates = []
    cur = db.execute('SELECT date FROM temparduino')
    for d in cur:
        dates.append(d[0])
    db.close()
    return dates


@app.route('/')
def main_page():
    x = get_date_time()
    y = get_temp()
    y2 = get_hu()
    title = 'temperature of room over time'
    line_chart = pygal.Line(width=1200, height=600,
                           explicit_size=True, title=title, disable_xml_declaration=True)
    line_chart.x_labels = x
    line_chart.add('room humidity', y2)
    line_chart.add('room temp', y) 
    return line_chart.render_response()  # render_template('main.html', title=title, line_chart=line_chart)


if __name__ == '__main__':
    database.readserial()
    app.run()
