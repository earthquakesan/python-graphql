#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import config
import utils
from models.car import CarModel

utils.create_tables()
session = config.get_sql_session()

session.add_all(
   [CarModel(Id=1, Name='Audi', Price=52642),
    CarModel(Id=2, Name='Mercedes', Price=57127),
    CarModel(Id=3, Name='Skoda', Price=9000),
    CarModel(Id=4, Name='Volvo', Price=29000),
    CarModel(Id=5, Name='Bentley', Price=350000),
    CarModel(Id=6, Name='Citroen', Price=21000),
    CarModel(Id=7, Name='Hummer', Price=41400),
    CarModel(Id=8, Name='Volkswagen', Price=21600)])
session.commit()

rs = session.query(CarModel).all()

for car in rs:
    print(car.Name, car.Price)
