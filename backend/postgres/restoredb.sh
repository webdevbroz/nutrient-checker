#!/bin/bash

is_container_running() {
    status=$(docker container inspect -f '{{.State.Status}}' postgres-local)
    [ "$status" == "running" ]
}

run_container() {
    # run psql docker container
    echo "Starting psql docker container"
    docker run --name postgres-local -e POSTGRES_PASSWORD=$DB_PW -p 5432:5432 -d postgres
    
    sleep 2
    
    if is_container_running; then
        # Run backup.sql on the docker install
        echo "Run backup.sql"
        sudo cat backup.sql | sudo docker exec -i postgres-local psql -U postgres
    else
        echo "Error with starting up the container."
        exit 0
    fi
}

# Check if the container exists.
if docker ps -a --format '{{.Names}}' | grep -q postgres-local; then
    # Check if the container is running.
    if is_container_running; then
        echo "Container is running, preparing to stop it."
        docker stop postgres-local
        # wait for the container to stop.
        sleep 2
        echo "Container has stopped."
    fi
    # remove existing docker container.
    docker rm postgres-local
    
    # Check if the container was removed.
    if docker ps -a --format '{{.Names}}' | grep -q "postgres-local"; then
        echo "Container was not successfully removed."
        exit 0
    else
        echo "Container has been removed."
        sleep 2
        
        run_container
    fi
else
    echo "Container is not available. Try running from image."
    exit 0
fi
