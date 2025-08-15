from pyspark.sql import SparkSession
from pyspark.sql.functions import col, row_number, rank, dense_rank, lag, lead, sum
from pyspark.sql.window import Window

# Start Spark session
spark = SparkSession.builder.appName("WindowFunctions").getOrCreate()

# Sample data
data = [
    ("Alice", "Sales", 3000),
    ("Bob", "Sales", 4000),
    ("Charlie", "Sales", 2500),
    ("David", "HR", 2000),
    ("Eve", "HR", 3500),
    ("Frank", "HR", 1500),
    ("Grace", "IT", 5000),
    ("Heidi", "IT", 6000),
    ("Ivan", "IT", 5200)
]
columns = ["name", "department", "salary"]
df = spark.createDataFrame(data, columns)

# Define window specification
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
running_total_spec = Window.partitionBy("department").orderBy("salary") \
                    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

# Apply window functions
df_result = df \
    .withColumn("row_number", row_number().over(window_spec)) \
    .withColumn("rank", rank().over(window_spec)) \
    .withColumn("dense_rank", dense_rank().over(window_spec)) \
    .withColumn("prev_salary", lag("salary", 1).over(window_spec)) \
    .withColumn("next_salary", lead("salary", 1).over(window_spec)) \
    .withColumn("running_total", sum("salary").over(running_total_spec))

# Show result
df_result.show()
