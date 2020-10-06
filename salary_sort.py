import os
os.environ["PYSPARK_PYTHON"] = '/usr/bin/python3'
from pyspark import SparkContext
from pyspark.sql import SQLContext
sc = SparkContext()
spark = SQLContext(sc)

df = spark.read.csv("hdfs://localhost:54310/hadoop/input/HR2m.csv",header=True,inferSchema = True)
df.sort('Salary').show()
