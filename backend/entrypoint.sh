#!/bin/bash
set -e

echo "Waiting for Postgres at $DB_HOST:$DB_PORT..."

until PGPASSWORD="$DB_PASSWORD" pg_isready \
  -h "$DB_HOST" \
  -p "$DB_PORT" \
  -U "$DB_USER" \
  -d "$DB_NAME"; do
  echo "Waiting for Postgres..."
  sleep 1
done

echo "Postgres is ready! Running migrations..."

alembic upgrade head

echo "Starting FastAPI..."
exec "$@"