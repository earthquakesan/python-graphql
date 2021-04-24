import json
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from models.car import CarModel

import config

class Car(SQLAlchemyObjectType):
    class Meta:
        model = CarModel

class Query(graphene.ObjectType):
    cars = graphene.List(Car)

    def resolve_cars(self, info):
        query = Car.get_query(info)
        return query.all()

def get_cars():
    schema = graphene.Schema(query=Query)

    query = '''
        query {
            cars {
                Name,
                Price
            }
        }
    '''
    result = schema.execute(query, context_value={'session': config.get_sql_session()})
    return result.to_dict()
