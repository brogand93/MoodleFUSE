from moodlefuse.model_manager import Base
from sqlalchemy import Column, String

 
class User(Base):
    __tablename__ = 'users'
    username = Column(String(255), primary_key=True)
    password = Column(String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password
