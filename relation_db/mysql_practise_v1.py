import mysql.connector as mysql


def create_db(db_name, host, user, password):
    try:
        con = mysql.connect(host=host, user=user, password=password)
        cur = con.cursor()
        cur.execute(f'CREATE DATABASE IF NOT EXISTS {db_name};')
        con.close()
    except:
        print('database cannot be created')


def connect_to_db(db_name):
    try:
        con = mysql.connect(host='localhost', user='root', password='19865421', database=db_name)
        print(f'You successfully connected to {db_name} database')
    except:
        print('You cannot connect to db')
    return con


def create_table_teacher():
    con = connect_to_db('practise_v1')
    con.cursor().execute('''CREATE TABLE IF NOT EXISTS teacher(id INT PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(20) NOT NULL,
                            surname VARCHAR(20) NOT NULL, 
                            age INT NOT NULL);''')


def create_table_pupil():
    con = connect_to_db('practise_v1')
    con.cursor().execute('''CREATE TABLE IF NOT EXISTS pupil(id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(20) NOT NULL, 
                        surname VARCHAR(20) NOT NULL,
                        age INT NOT NULL);''')


if __name__ == '__main__':
    create_db('practise_v1', 'localhost', 'root', '19865421')
    create_table_teacher()
    create_table_pupil()
