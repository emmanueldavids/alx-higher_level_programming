#!/usr/bin/python3
""" 
    Once again, write a script that takes in arguments and displays all values 
    in the states table of hbtn_0e_0_usa where name matches the argument. 
    But this time, write one that is safe from MySQL injections!
"""
import MySQLdb as mydb
import sys

#  mysql username, mysql password, database name and state name searched
# the function that work on safe mysql filter
def safe_filter():

    # MySQL connection initialization
    db = mydb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # create the cursor object
    cursor = mydb.cursor()
    state = sys.argv[4]
    #input the command to query the database
    command = ("SELECT * FROM states WHERE name is %s ORDER BY id ASC", (state))
    #execute the command
    cursor.execute(command)
    # fetch all the rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()

    if __name__ == "__main__":
        safe_filter()