#!/usr/bin/python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import config
import utils
from models.car import CarModel

session = config.get_sql_session()

session.add_all(
   [CarModel(Name='Audi', Price=52642),
    CarModel(Name='Mercedes', Price=57127),
    CarModel(Name='Skoda', Price=9000),
    CarModel(Name='Volvo', Price=29000),
    CarModel(Name='Bentley', Price=350000),
    CarModel(Name='Citroen', Price=21000),
    CarModel(Name='Hummer', Price=41400),
    CarModel(Name='Volkswagen', Price=21600)])
session.commit()

rs = session.query(CarModel).all()

for car in rs:
    print(car.Name, car.Price)
