"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm
from sqlalchemy.schema import *
from sqlalchemy.orm import *
from sqlalchemy.types import *
from sqlalchemy.sql.expression import and_, or_, not_
from walkr.model.meta import Base
from walkr.model import meta
from walkr.model.user import *

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)

    meta.Session.configure(bind=engine)
    meta.engine = engine


    # User tables
    global user_table
    user_table = Table('user', Base.metadata,
        Column('uid', Integer, primary_key=True, autoincrement=True),
        Column('username', Unicode(31), unique=True, nullable=False),
        Column('password', Unicode(255), nullable=False),
        Column('fullname', Unicode(127)),
        Column('email', Unicode(255), nullable=False),
        mysql_engine='innodb')

    
    global roles_table
    roles_table = Table("roles", Base.metadata,
        Column("uid", ForeignKey("user.uid"), primary_key=True),
        Column("name", String(31), primary_key=True, unique=True, nullable=False),
        mysql_engine='innodb')


    mapper(User, user_table, 
        properties={
            '_roles':relation(Role, cascade="all,delete-orphan"),
        })
    
    mapper(Role, roles_table, 
        properties={"users": relation(User)})

