#!/usr/bin/python3
"""
This script lists all cities from the
database `hbtn_0e_0_usa`.
It takes state as an argument and lists all cities of that state
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
    query = "SELECT cities.id, cities.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %(state_name)s \
            ORDER BY cities.id ASC"
    db_cursor.execute(query, {'state_name': argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row[1])
