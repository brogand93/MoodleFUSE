#!/usr/bin/env python
# encoding: utf-8

"""Class to handle moodlefuse user models
"""

from sqlalchemy import Column, String

from moodlefuse.model_manager import Base


class User(Base):
    __tablename__ = 'users'
    username = Column(String(255), primary_key=True)
    password = Column(String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password
