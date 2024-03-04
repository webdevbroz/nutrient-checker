#!/bin/bash

# stop existing docker container

docker stop postgres-local

# wait for container to stop

sleep 2

# remove existing docker container

docker rm postgres-local

# wait for docker to finish cleaning up

sleep 2

# run psql docker container

docker run --name postgres-local -e POSTGRES_PASSWORD=$DB_PW -p 5432:5432 -d postgres

# Wait for container to become available

sleep 2

# Run backup.sql on the docker install

sudo cat backup.sql | sudo docker exec -i postgres-local psql -U postgres

# # Alter postgres PW

# echo "ALTER ROLE postgres PASSWORD '$DB_PW'" | sudo docker exec -i postgres-local psql -U postgres 