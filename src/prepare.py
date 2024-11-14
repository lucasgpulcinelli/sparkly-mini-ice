#!/usr/bin/env python3

import pyspark.sql

spark = (
    pyspark.sql.SparkSession.Builder()
    .master("local[*]")
    .appName("Prepare Script")
    .getOrCreate()
)

schema = """
    Transaction_unique_identifier   string,
    price                           long,
    Date_of_Transfer                date,
    postcode                        string,
    Property_Type                   string,
    OldNew                          string,
    Duration                        string,
    PAON                            string,
    SAON                            string,
    Street                          string,
    Locality                        string,
    City                            string,
    District                        string,
    County                          string,
    PPDCategory_Type                string,
    Record_Status                   string
"""

df = spark.read.csv("/tmp/spark-shared/202304.csv", schema=schema)

spark.sql(f"""
    CREATE OR REPLACE TABLE uk_pricing (
        {schema}
    )
    USING iceberg
    PARTITIONED BY (year(Date_of_Transfer))
    TBLPROPERTIES ('format-version'='2')
""")

spark.sql("""
    ALTER TABLE uk_pricing
    WRITE ORDERED BY City
""")

df.registerTempTable("csv_data")

spark.sql("""
    INSERT INTO uk_pricing
    SELECT * FROM csv_data
""")

print("done!")
