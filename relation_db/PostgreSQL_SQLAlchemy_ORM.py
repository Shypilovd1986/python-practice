from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://postgres:19865421@localhost:5432/test1')
Base = declarative_base(engine)
Base.metadata.reflect(engine)
# Base.metadata.reflect and pass in the engine. What this call means is communicate with the database, read it, and have
# our base object reflect that database and the data that's in it. So that includes the tables, the columns, all of that
# good stuff. Why is it useful? Well, when we create our Sales class, we can just read in that table data with the
# base.metadata.tables and pass in the name of the table that we want to read the data from. This will pass in all the
# metadata about that sales table, so that when we create this class, all we have to do is write a two string function
# or a string representation of this object.


class House(Base):
    __table__ = Base.metadata.tables['house']

    def __repr__(self):
        return '''<Rom in the house: {0}, description of room: {1}>'''.format(self.house_room, self.room_description)


def loadSession():
    ''' This configures the session that we can use to interact with our database. '''
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__ == '__main__':
    session = loadSession()

    # Read
    house_info = session.query(House).order_by(House.room_id).limit(10)
    for room in house_info:
        print(room)
    print(house_info[1].room_id)

    # Insert
    insert_room = House(room_id=14, house_room='wardrobe', room_description='for storing cloth')
    print(insert_room)
    session.add(insert_room)
    session.commit()

    # Update
    update_room = session.query(House).filter(House.room_id == 6).first()
    update_room.room_description = 'children bath'
    session.commit()

    # Delete
    session.delete(session.query(House).filter(House.room_id == 14).first())
    session.commit()
