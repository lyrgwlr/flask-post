from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column,SmallInteger,Integer

class SQLAlchemy(_SQLAlchemy):
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
#    create_time = Column('create_time',Integer)
#    status = Column(SmallInteger,default=1)
    
    def set_attrs(self,attrs_dict):
        for key,value in attrs_dict.items():
            if hasattr(self,key) and key != 'id':
                setattr(self,key,value)