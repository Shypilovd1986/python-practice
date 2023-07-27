"""practise with sqlalchemy core"""
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData


engine = create_engine('mysql+mysqlconnector://root:19865421@localhost:3306/practise_v1')

# engine = create_engine('postgresql://postgres:19865421@localhost/practise_v1')


with engine.connect() as connection:
    meta = MetaData(engine)
    teacher = Table('teacher', meta, autoload=True, autoload_with=engine)
    show_all = teacher.select()
    result = connection.execute(show_all)
    for res in result:
        print(res)

    add_teacher = teacher.insert().values(
        id=5,
        name='Masha',
        surname='Shypilova',
        age=8
    )

    connection.execute(add_teacher)

    print('**************************')

    result = connection.execute(show_all)
    for res in result:
        print(res)

    delete_Maria_teacher = teacher.delete().where(teacher.c.id == 5)
    connection.execute(delete_Maria_teacher)
