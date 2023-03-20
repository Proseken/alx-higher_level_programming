#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    a, b, c = sys.argv[1], sys.argv[2], sys.argv[3]
    data = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(data.format(a, b, c), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    newS = State("Louisiana")
    session.add(newS)
    session.commit()
    result = session.query(State).filter_by(name=newS.name).all()
    if result:
        for re in result:
            print(f"{re.id}")
    else:
        print("Not found")
    session.close()
