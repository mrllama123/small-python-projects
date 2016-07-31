import sqlite3
import pygal
database = sqlite3.connect('server.db')
databsepointer = database.cursor()


def get_temp():
    temputures = []
    for t in databsepointer.execute('SELECT temp FROM tempArduino'):
        te = float(t[0])
        temputures.append(te)
    return temputures


def get_date():
    dates = []
    for d in databsepointer.execute('SELECT date FROM tempArduino'):
        date = d[0]

        dates.append(date[:16])
    return dates

# if __name__ == '__main__':
#     x = get_date()
#     y = get_temp()
#
#     title = 'temperature of room over time'
#     line_chart = pygal.Line()
#     # line_chart.x_labels = x
#     line_chart.add('room temp', y)
#     line_chart.render_in_browser()