#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create connection string and engine
    connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(connection_string.format(mysql_username,
                                                     mysql_password,
                                                     database_name),
                           pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query for all states with a name containing 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete the states from the session and commit the transaction
    for state in states:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
