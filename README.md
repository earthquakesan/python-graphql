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