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
    db = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states")
    results = cur.fetchall()
    for result in results:
        print(result)


    cur.close()
    connection.close()
