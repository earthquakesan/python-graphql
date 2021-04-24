#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

import config

def create_tables():
    Base = declarative_base()
    Base.metadata.bind = config.get_sql_engine()
    Base.metadata.create_all()
