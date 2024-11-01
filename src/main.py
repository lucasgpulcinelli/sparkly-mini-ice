#!/usr/bin/env python3

import pyspark.sql

spark = (
    pyspark.sql.SparkSession.Builder()
    .appName("Pyspark With S3 and Iceberg Example")
    .getOrCreate()
)

df = spark.sql("""
    WITH max_no_transfers AS (
        SELECT
            COUNT(*) AS no_of_transfers, postcode
        FROM testtable
        WHERE City = 'LONDON' AND postcode IS NOT NULL
        GROUP BY postcode
        ORDER BY no_of_transfers DESC
        LIMIT 1
    )
    SELECT t.Transaction_unique_identifier, t.postcode, t.Date_of_Transfer, t.price
    FROM testtable t
        JOIN max_no_transfers m ON t.postcode = m.postcode
    ORDER BY t.Date_of_Transfer DESC
""")

arr = df.collect()

for row in arr:
    print(row)
