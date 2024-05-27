import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import SparkSession

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Create a SparkSession
spark = SparkSession.builder.appName("S3ReadWrite").getOrCreate()

# Define source and destination S3 paths (replace with your bucket names)
source_path = "s3://aws-gluedemo1/input/info.csv"
destination_path = "s3://aws-gluedemo1/output/data.csv"

# Read data from S3 (replace 'csv' with your file format if different)
data = spark.read.format("csv").option("header", True).load(source_path)

# Write data to S3 in Parquet format (replace with your desired format)
data.write \
  .format("csv") \
  .mode("overwrite") \
  .save(destination_path)

# Stop the SparkSession
spark.stop()




job.commit()