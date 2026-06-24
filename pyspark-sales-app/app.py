from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesDataFrameApp") \
    .getOrCreate()

# Read CSV File
df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

# ------------------------------------------------
# 1. Sort products by sales descending
# ------------------------------------------------
print("\n===== Products Sorted By Sales =====")

sorted_df = df.orderBy(col("sales").desc())

sorted_df.show()

# ------------------------------------------------
# 2. Display Top 3 Products
# ------------------------------------------------
print("\n===== Top 3 Products =====")

top3 = sorted_df.limit(3)

top3.show()

# ------------------------------------------------
# 3. Filter sales > 80000
# ------------------------------------------------
print("\n===== Products With Sales > 80000 =====")

filtered_df = df.filter(col("sales") > 80000)

filtered_df.show()

# Save filtered output as CSV
filtered_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", True) \
    .csv("output/filtered_sales")

print("\nFiltered sales saved successfully in output/filtered_sales")

# Stop Spark Session
spark.stop()