import pyspark.sql.functions as F
import re

from spark import get_spark

spark = get_spark()

DELTA_PATH = "data/delta/horse-prices"

df = spark.read.option("header", True).option("inferSchema", True).csv("data/2026_07_14.csv")


# standardise the column names
def clean_column_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_]", "_", name.strip().lower()).replace("__", "_").strip("_")


df = df.toDF(*[clean_column_name(c) for c in df.columns])

# repartiton the the df to match the table
df = df.repartition(F.col("race_type"), F.col("course"))

(df.write.format("delta").mode("overwrite").partitionBy("race_type", "course").save(DELTA_PATH))

print("Delta table created")
