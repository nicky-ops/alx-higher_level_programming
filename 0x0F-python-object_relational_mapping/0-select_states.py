#!/usr/bin/python3
import MySQLdb
import sys
"""
This script lists all states from the database hbtn_0e_0_usa

ARGUMENTS:
    mysql username - username for the database
    mysql password - password for the database
    database name  - name of the database


uses the module MySQLdb:
    import MySQLdb
connects to a MySQL server running on localhost at port 3306

RETURNS:
    results sorted in ascending order by states.id
"""

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
