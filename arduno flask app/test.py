import sqlite3

database = sqlite3.connect('server.db')
databsepointer = database.cursor()

for t in databsepointer.execute('SELECT temp FROM tempArduino'):
    print(t)