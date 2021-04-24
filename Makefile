.PHONY: postgresql

postgresql_release := test-postgresql

run:
	python pygraphql/main.py

postgresql:
	helm install -f postgresql-values.yml ${postgresql_release} bitnami/postgresql

clean:
	helm uninstall ${postgresql_release}

psql-console:
	./psql.sh