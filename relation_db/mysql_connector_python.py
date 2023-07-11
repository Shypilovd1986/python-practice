import mysql.connector as mysql


def connect(db_name):
    try:
        my_db = mysql.connect(
            host='localhost',
            user='root',
            password='19865421',
            database=db_name,
            allow_local_infile=True
        )
        return my_db
    except Exception :
        print('You can\'t connect to database')


def add_new_user(my_cursor, user_name, user_surname,):
    user_credentials = (user_name, user_surname)
    my_cursor.execute('''INSERT INTO users(name, surname) VALUES(%s, %s)''', user_credentials)


def add_new_tasks(cursor, user_id, task_name, task_description):
    task_list = (user_id, task_name, task_description)
    cursor.execute('''INSERT INTO tasks(user_id, task_name, description) VALUES(%s, %s, %s)''', task_list)


if __name__ == '__main__':
    db = connect('project')
    cursor = db.cursor()
    add_new_user(cursor, 'Katrin', 'Gosliiin')
    cursor.execute('SELECT * FROM users')
    all_result = cursor.fetchall()
    for user in all_result:
        print(user)
    add_new_tasks(cursor, 7, 'clean house', 'wash all house')
    cursor.execute('''SELECT * FROM tasks''')
    print(cursor.fetchall())

    db.commit()
    db.close()
