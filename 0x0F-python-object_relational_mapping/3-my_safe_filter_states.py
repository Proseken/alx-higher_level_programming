#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb
import re

if __name__ == "__main__":
    filename, username, password, db_name, state_name = sys.argv

    # regular expression pattern to match SQL keywords and special characters
    reg = r"\b(SELECT|UPDATE|DELETE|DROP|CREATE|INSERT|ALTER|TRUNCATE)\b|[;']"
    sql_pattern = re.compile(reg)

    # Check if search_term matches the pattern
    if sql_pattern.search(state_name):
        print("Invalid search term")
    else:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=db_name)
        cur = db.cursor()
        query = "SELECT id, name FROM states WHERE name LIKE %s ORDER BY id"
        cur.execute(query, (f"{state_name}%",))
        for names in cur:
            print(names)
        cur.close()
        db.close()
