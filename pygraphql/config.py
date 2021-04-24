import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_postgresql_user():
    # see postgresql-values.yml
    return "postgres"

def get_postgresql_password():
    # see postgresql-values.yml
    return "postgres"

def get_postgresql_host():
    # minikube, node ip, can get programmatically with kubectl
    return "192.168.52.172"

def get_postgresql_port():
    # node port, can get programmatically with kubectl
    return "30432"

def get_postgresql_db():
    # see postgresql-values.yml
    return "test"

def get_postgresql_connection_string():
    return "postgresql://{}:{}@{}:{}/{}".format(
        get_postgresql_user(),
        get_postgresql_password(),
        get_postgresql_host(),
        get_postgresql_port(),
        get_postgresql_db()
    )

def get_sql_engine():
    return create_engine(
        get_postgresql_connection_string()
    )

def get_sql_session():
    Session = sessionmaker(bind=get_sql_engine())
    return Session()
