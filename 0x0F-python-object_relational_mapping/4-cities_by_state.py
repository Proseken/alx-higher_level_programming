#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb
import re

if __name__ == "__main__":
    filename, username, password, db_name = sys.argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    query = "SELECT ROW_NUMBER() OVER (ORDER BY cities.id ASC),\
                cities.name, states.name FROM cities JOIN states\
                ON cities.state_id = states.id"
    cur.execute(query)
    for names in cur:
        print(names)
    cur.close()
    db.close()
