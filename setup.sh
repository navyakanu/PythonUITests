#!/usr/bin/env bash

counter=1
for var in $@
do
    IFS='=' read -ra args <<< "$var"
    argument[$counter]=${args[1]}
    ((counter ++))
done

test_type=${argument[1]}

with_docker=${argument[2]-False}


if $with_docker
then
    with_docker=True
    docker-compose up --build -d

    response=$(curl --write-out %{http_code} --silent --output /dev/null http://localhost:4444/status)

    while [ ${response} != "200" ]
    do
        response=$(curl --write-out %{http_code} --silent --output /dev/null http://localhost:4444/status)
    done

    echo "Grid is Up"
else
    with_docker=False
fi
