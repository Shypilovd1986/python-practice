from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('postgresql://postgres:19865421@localhost:5432/test1')


with engine.connect() as connection:
    meta = MetaData(engine)
    house_table = Table('house', meta, autoload=True, autoload_with=engine)

    # insert data into table

    insert_room = house_table.insert().values(room_id=10,
                                              house_room='kitchen',
                                              room_description='for cooking')
    connection.execute(insert_room)

    select_room = house_table.select().limit(10)
    result = connection.execute(select_room)

    for r in result:
        print(r)

    # update room

    update_room = house_table.update().where(house_table.c.room_id == 5).values(room_description='room for children',
                                                                              house_room='playing_room')
    connection.execute(update_room)

    print("**********************")

    # select

    select_info_room = house_table.select().where(house_table.c.house_room == 'bedroom')
    result_2 = connection.execute(select_info_room)
    print(f'founded rows: {result_2.rowcount}')

    for r in result_2:
        print(r)

    # delete room
    delete_room = house_table.delete().where(house_table.c.room_id == 10)
    connection.execute(delete_room)
