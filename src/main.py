#!/usr/bin/env python3

import pyspark.sql

spark = (
    pyspark.sql.SparkSession.Builder()
    .appName("Pyspark With S3 and Iceberg Example")
    .getOrCreate()
)

df = spark.sql("""
    WITH
    count_transfers AS (
        SELECT
            postcode,
            EXTRACT(YEAR FROM Date_of_Transfer) AS year,
            COUNT(*) AS count
        FROM uk_pricing
        WHERE postcode IS NOT NULL
        GROUP BY postcode, year
    ),
    max_count_transfers AS (
        SELECT FIRST(c.postcode) AS postcode, c.year, c.count
        FROM count_transfers c
            JOIN (
                SELECT year, MAX(count) AS count
                FROM count_transfers
                GROUP BY year
            ) cm
                ON cm.count = c.count AND cm.year = c.year
        GROUP BY c.year, c.count
    )
    SELECT p.Transaction_unique_identifier, p.Date_of_Transfer, p.postcode, p.price
    FROM uk_pricing p
        JOIN max_count_transfers m

            ON p.postcode = m.postcode
            AND m.year = EXTRACT(YEAR FROM p.Date_of_Transfer)
    ORDER BY p.Date_of_Transfer DESC
""")

arr = df.collect()

for row in arr:
    print(row)
