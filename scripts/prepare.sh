#!/usr/bin/env sh

if [ $(docker compose ps |wc -l) -ne 5 ]; then
  echo "error: project is not deployed, run \"docker compose up -d\" before running this script"
  exit -1
fi

curl -L -o /tmp/uk-prices.zip https://www.kaggle.com/api/v1/datasets/download/willianoliveiragibin/uk-property-price-data-1995-2023-04

unzip -d /tmp/spark-shared /tmp/uk-prices.zip

rm /tmp/uk-prices.zip

docker compose cp ./src/prepare.py spark-master:/tmp/prepare.py

docker compose exec spark-master /opt/spark/bin/spark-submit /tmp/prepare.py

