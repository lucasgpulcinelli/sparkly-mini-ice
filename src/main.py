#!/usr/bin/env python3

import pyspark.sql

spark = (
    pyspark.sql.SparkSession.Builder()
    .appName("Pyspark With S3 and Iceberg Example")
    .getOrCreate()
)

df = spark.read.format("iceberg").load("testtable")

df.show()

