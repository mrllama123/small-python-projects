from flask import Flask, render_template, g
import sqlite3
import pygal

DATABASE = 'server.db'

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)


# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     db.row_factory = sqlite3.Row
#     return db
#
# def query_db(query, args=(), one=False):
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     cur.close()
#     return (rv[0] if rv else None) if one else rv
#
# def get_temp():
#     temputures = []
#     for t in query_db('SELECT temp FROM tempArduino'):
#         temputures.append(float(t[0]))
#     return temputures

# app.config.from_object(__name__)
#
# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])
#
#
#
def get_temp():
    db = connect_db()
    cur = db.execute('SELECT temp FROM temparduino')
    temputures = cur.fetchall()
    db.close()
    return temputures


# def get_date_time():
#     g.db = connect_db()
#     dates = []
#     for d in g.db.execute('SELECT dates FROM tempArduino'):
#         dates = d[:15]
#     return dates


@app.route('/')
def main_page():
    # x = test.get_date_time()
    y = get_temp()

    title = 'temperature of room over time'
    line_chart = pygal.Line(width=860, height=300,
                            explicit_size=True, title=title, disable_xml_declaration=True)

    line_chart.add('room temp', [82,13,39,50,50,77,55,36,70,7,56,7,59,64,14,79,92,75,76,62,13,13,6,45,86,95,89,11,100,56,10,28,82,10,30,45,83,76,88,91])
    # line_chart.render()

    return render_template('main.html', title=title, line_chart=line_chart)


if __name__ == '__main__':
    app.run()
