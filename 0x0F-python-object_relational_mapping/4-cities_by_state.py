#!/usr/bin/python3
"""
This script lists all cities from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the cities
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT cities.id, cities.name, states.name FROM \
            cities INNER JOIN states ON \
            cities.state_id = states.id ORDER BY cities.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
