#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

export POSTGRES_PASSWORD=$(kubectl get secret --namespace default test-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services test-postgresql)

PGPASSWORD="$POSTGRES_PASSWORD" psql --host $NODE_IP --port $NODE_PORT -U postgres -d test
