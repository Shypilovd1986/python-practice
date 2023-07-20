from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqlconnector://root:19865421@localhost:3306/house", echo=True)

Base = declarative_base()


class Project(Base):
    __tablename__ = 'project'
    __table_args__ = {'schema': 'house'}

    project_id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    description = Column(String(length=50))

    def __repr__(self):
        return "<Project: title{0}, description{1} >".format(self.title, self.description)


class Task(Base):
    __tablename__ = 'task'
    __table_args__ = {'schema': 'house'}

    task_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('house.project.project_id'))
    description = Column(String(length=50))

    project = relationship('Project')

    def __repr__(self):
        return "<Project: description{0} >".format(self.description)


Base.metadata.create_all(engine)

session_maker = sessionmaker()
session_maker.configure(bind=engine)
session = session_maker()

organize_closet_project = Project(title="Organize closet", description="Organize closet in our house")
session.add(organize_closet_project)
# this how we can add one object to database
session.commit()

tasks = [
    Task(project_id=organize_closet_project.project_id, description="Install window"),
    Task(project_id=organize_closet_project.project_id, description="Stick wallpaper "),
    Task(project_id=organize_closet_project.project_id, description="Clean room"),
         ]

session.bulk_save_objects(tasks)
#  This is how you can save multiple things to your database in one line.
session.commit()

our_project = session.query(Project).filter_by(title="Organize closet").first()

print(our_project)

our_tasks = session.query(Task).all()

print(our_tasks)
