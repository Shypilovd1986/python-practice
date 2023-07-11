import psycopg2


conn = psycopg2.connect(database="test1",
                 user="postgres",
                 password="19865421",
                 host="localhost",
                 port="5432")

cursor = conn.cursor()

try:
    cursor.execute('''CREATE TABLE house(
        ROOM_ID INT PRIMARY KEY,
        HOUSE_ROOM TEXT,
        ROOM_DESCRIPTION TEXT);''')
except Exception:
    print("Table can not be created")


conn.commit()


def insert_into_table(con, room_id, house_room, room_description):
    room_info = (room_id, house_room, room_description)
    cur = con.cursor()
    cur.execute('''INSERT INTO house(ROOM_ID, HOUSE_ROOM, ROOM_DESCRIPTION) VALUES(%s, %s, %s)''', room_info)


def delete_from_table(con, value):
    cur = con.cursor()
    delete_id = (value,)
    cur.execute('''DELETE FROM house WHERE ROOM_ID=%s''', delete_id)


insert_into_table(conn, 7, 'bedroom', 'room for sleeping')
delete_from_table(conn, 4)

conn.commit()
conn.close()
