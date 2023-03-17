#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__  ==  "__main__":
    filename, username, password, db_name = sys.argv
    db = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=username,
                        passwd=password,
                        db=db_name)
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id")
    for names in cur:
        print(names)
    cur.close()
    db.close()
    
