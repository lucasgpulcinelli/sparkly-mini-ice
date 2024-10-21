#!/usr/bin/env sh

if [ $(docker compose ps |wc -l) -ne 5 ]; then
  echo "error: project is not deployed, run \"docker compose up -d\" before running this script"
  exit -1
fi

docker compose cp ./src/main.py spark-master:/tmp/main.py

docker compose exec spark-master /opt/spark/bin/spark-submit /tmp/main.py

