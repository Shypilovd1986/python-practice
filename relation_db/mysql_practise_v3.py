from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import declarative_base


engine = create_engine('mysql+mysqlconnector://root:19865421@localhost:3306/practise_v1')

Base = declarative_base(engine)
Base.metadata.reflect(engine)


class Teacher(Base):
    __table__ = Base.metadata.tables['teacher']

    def __repr__(self):
        return f'''<Teacher {self.name} {self.surname} , {self.age} age >'''


def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


if __name__=='__main__':
    session = create_session()
    show_all = session.query(Teacher).limit(10)

    for i in show_all:
        print(i)
    # try:
    #     teacher_Ksusha = Teacher(id=6, name='Ksusha', surname='Shypilova', age=13)
    #     session.add(teacher_Ksusha)
    #     session.commit()
    # except :
    #     print('This teacher already exists')


#     will update teacher information
#
#     find_teacher = session.query(Teacher).filter(Teacher.name == 'Vovka').first()
#     print(type(find_teacher))
#     print(find_teacher)
#     find_teacher.name = 'Vovka1'
#     session.commit()
#
#     show_all = session.query(Teacher).limit(10)
#
#     for i in show_all:
#         print(i)

