#!/usr/bin/python3
""" This script lists all states from
    the database hbtn_0e_0_usa with name
    starting with N
"""
import MySQLdb as mydb
import sys

def filter_states():
    # initialize the connection to the database
    db = mydb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    #create the object cursor
    cursor = db.cursor()
    state = sys.argv[4]
    #command goes here
    command = ("SELECT * FROM states WHERE name is %s ORDER BY id ASC", (state))
    #execute the command
    cursor.execute(command)
    #fetch all rows
    rows = cursor.fetchall()
    #print rows
    if len(rows) == 0:
        print("no state found", (state))
    else:
        for row in rows:
            print(row)
        
    #close the cursor connection
    cursor.close()
    db.close()

    if __name__ == "__main__":
        filter_states()