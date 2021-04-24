#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base

import config
from models.car import CarModel

def add_car(car_name, car_price):
    session = config.get_sql_session()
    session.add_all(
        [CarModel(Name=car_name, Price=car_price)]
    )
    session.commit()
