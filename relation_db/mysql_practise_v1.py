"""module for creating db and table """

import mysql.connector as mysql


def create_db(db_name, host, user, password):
    """function for creating db"""
    try:
        con = mysql.connect(host=host, user=user, password=password)
        cur = con.cursor()
        cur.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
        con.close()
    except mysql.Error:
        print('database cannot be created')


def connect_to_db(db_name):
    """function for connecting with db"""
    try:
        con = mysql.connect(host='localhost', user='root', password='19865421', database=db_name)
        print(f'You successfully connected to {db_name} database')
    except mysql.Error:
        print('You cannot connect to db')
    return con


def create_table_teacher():
    """for creating table teacher with columns id, name, surname, age"""
    con = connect_to_db('practise_v1')
    try:
        con.cursor().execute('''CREATE TABLE IF NOT EXISTS teacher(id INT PRIMARY KEY AUTO_INCREMENT,
                             name VARCHAR(20) NOT NULL,
                             surname VARCHAR(20) NOT NULL, 
                             age INT NOT NULL);''')
    except mysql.Error:
        print('Table cannot be created')
    con.close()


def create_table_pupil():
    """for creating table pupil"""
    con = connect_to_db('practise_v1')
    try:
        con.cursor().execute('''CREATE TABLE IF NOT EXISTS pupil(id INT PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(20) NOT NULL, 
                            surname VARCHAR(20) NOT NULL,
                            age INT NOT NULL);''')
    except mysql.Error:
        print('Table cannot be created')
    con.close()


def update_credential_teacher(teacher_id, name, surname, age,):
    """for updating teacher"""
    con = connect_to_db('practise_v1')
    cur = con.cursor()
    credentials_list = (name, surname, age, teacher_id)
    cur.execute('''UPDATE teacher SET name=%s, surname=%s, age=%s WHERE id=%s''', credentials_list)
    con.commit()
    con.close()


def read_all_items(table_name):
    """for reading items from teacher table"""
    con = connect_to_db('practise_v1')
    cur = con.cursor()
    cur.execute(f'''SELECT * FROM {table_name}''')
    print(cur.lastrowid)
    print(cur.fetchall())
    con.close()


if __name__ == '__main__':
    create_db('practise_v1', 'localhost', 'root', '19865421')
    create_table_teacher()
    create_table_pupil()
    update_credential_teacher(4, 'Dmitriy', 'Shypilov', 37)
    read_all_items('teacher')
