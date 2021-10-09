#!/bin/sh

set -e
set -x

docker-compose down --rmi all
docker-compose up
