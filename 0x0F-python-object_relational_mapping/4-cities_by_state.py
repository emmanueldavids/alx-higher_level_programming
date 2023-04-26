#!/usr/bin/python3
""" 
a script that lists all cities from the database 
hbtn_0e_4_usa
"""
import MySQLdb as mydb
import sys

#  mysql username, mysql password, database name and state name searched
# the function that work on safe mysql filter
def city_by_state():

    # MySQL connection initialization
    db = mydb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # create the cursor object
    cursor = mydb.cursor()
    #input the command to query the database
    command = ("SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
    #execute the command
    cursor.execute(command)
    # fetch all the rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    cursor.close()
    db.close()

    if __name__ == "__main__":
        city_by_state()