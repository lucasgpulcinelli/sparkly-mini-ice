# Sparkly Mini Ice
This repository is a toy deployment of Apache Spark in standalone mode using docker-compose, with MinIO as a storage backend and Apache Iceberg as the default catalog, with a local filesystem metadata management (on the master node)

The objective of the repo is to show an example of what Spark is capable of in a presentation for the university discipline "Distributed Computing Systems".

## Deploying

To deploy spark and two worker nodes, plus the necessary MinIO backend, first add the required JAR files in the extra-jars/ directories using `./scripts/download-jars.sh` at the root of the repo. To use that, make sure you have curl installed.

After that, you should be able to run `docker compose up`, acess http://localhost:8080 and see the Spark UI with two workers active, and acess http://localhost:900 and see the MinIO UI (to login, use minio-spark-example as both the login and password).

## Preparing dataset
The dataset we will use is about UK housing prices from 1995 to 2023, the objective is to do some queries using the dataset such as different aggregations by region and date

## Running the code
To send the python code to be executed by the workers, use `./scripts/send-py.sh ./src/main.py` (run as root if docker is not in rootless mode)

## Made fully by
- Lucas Eduardo Gulka Pulcinelli
