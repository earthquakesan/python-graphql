# python-graphql
Trying out SQLAlchemy with GraphQL

## Requirements

You will need libpq-dev and python3-dev to install psycopg2 library. On Ubuntu 20.04:

```
sudo apt-get update 
sudo apt install libpq-dev python3-dev
```

## Spin Up PostgreSQL in Minikube

Use [bitnami helm chart for PostgreSQL](https://github.com/bitnami/charts/tree/master/bitnami/postgresql/#installing-the-chart):

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install local-psql bitnami/postgresql
```

## Running The Code

1. Populate PostgreSQL with initially 8 cars (taken from example [here](https://zetcode.com/db/sqlalchemy/orm/)):

```
python pygraphql/populate_cars.py
```

Note: Ids were removed from the objects. If you define Ids in the code, PostgreSQL internal "Cars_Id_seq" will not be incremented. "Cars_Id_seq" is used to generate Ids. This means, that if you insert 8 cars with Ids={1..8} and then try to insert one without Id, PostgreSQL will generate Id=1. And it will fail due to duplicate primary_key.

2. Start flask server.

```
make web
```

3. Read cars from the server ([using graphql](pygraphql/graphqlmodels/cars.py)):

```
make get-cars-curl
```

4. Insert a car into the database:

```
make add-car-curl
```

Query again to see that the car was added.