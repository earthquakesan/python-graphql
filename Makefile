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

web:
	FLASK_APP=pygraphql/web.py flask run

add-car-curl:
	curl -X POST -F 'Name=Toyota' -F 'Price=45000' http://localhost:5000/car

get-cars-curl:
	curl -X GET http://localhost:5000/cars | python -m json.tool
