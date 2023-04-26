#!/usr/bin/python3
"""
Changes the name of the State where id = 2 to "New Mexico"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the database for the State with id = 2
    state = session.query(State).filter(State.id == 2).first()

    # If the State exists, update its name to "New Mexico"
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
