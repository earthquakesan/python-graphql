#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

import config

Base = declarative_base()

class CarModel(Base):
    __tablename__ = "Cars"

    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Price = Column(Integer)

Base.metadata.bind = config.get_sql_engine()
Base.metadata.create_all()
