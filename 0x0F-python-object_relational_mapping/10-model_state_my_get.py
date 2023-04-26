#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    # Create a new Engine instance
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database for the state with the given name
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    # Print the state's id or "Not found" if no state with the given name exists
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
