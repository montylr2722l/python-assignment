from pyspark.sql import SparkSession

# SparkSession banayein
spark = SparkSession.builder \
    .appName("MeraPehlaSparkApp") \
    .master("local[*]") \
    .getOrCreate()

print(f"Spark Version: {spark.version}")
print("Spark Session successfully created!")

# Session band karein
spark.stop()   