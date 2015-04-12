from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
 
 
Base = declarative_base()
 
 
class User(Base):
    __tablename__ = 'users'
    apikey = Column(String(255), primary_key=True)
    secretkey = Column(String(255), unique=True)

    def __init__(self, username, password):
        self.username = username
        self.password = password