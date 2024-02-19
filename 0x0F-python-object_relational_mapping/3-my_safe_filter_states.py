#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa` where name matches the argument passed.
and is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states WHERE name LIKE BINARY \
            %(name)s ORDER BY states.id ASC", {"name": argv[4]})
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
