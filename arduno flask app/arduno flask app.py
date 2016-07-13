from flask import Flask, render_template, g
import sqlite3
import pygal

DATABASE = 'server.db'


def get_db():
    db = g.getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


app = Flask(__name__)


@app.route('/')
def main_page():
    # databsepointer.execute("SELECT * FROM tempArduino")
    # y = databsepointer.fetchone()
    # databsepointer.execute("SELECT date FROM tempArduino")
    # x = databsepointer.fetchall()

    title = 'temperature of room over time'
    line_chart = pygal.Line(width=1200, height=600,
                            explicit_size=True, title=title, disable_xml_declaration=True)

    line_chart.x_labels = map(str, range(2000, 2014))
    line_chart.add('room temp', [95, 12, 45, 10, 77, 11, 73, 64, 10, 80, 52, 60, 54, 18])
    # line_chart.render()

    return render_template('main.html', title=title, line_chart=line_chart)


if __name__ == '__main__':
    app.run()
