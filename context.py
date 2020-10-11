import os
os.environ["PYSPARK_PYTHON"] = '/usr/bin/python3'
from pyspark import SparkContext
from pyspark.sql import SQLContext

class Context:

    # function for creating SparkContext
    def context(self):
        try:
            sc = SparkContext()
            spark = SQLContext(sc)
        except:
            print("Context doesn't get Created")
        return spark

    # Load Data from Csv File
    def load_data(self, spark):
        try:
            df = spark.read.csv("hdfs://localhost:54310/hadoop/input/Hr2m.csv",header=True,inferSchema = True)
        except:
            print("Data didn't get loaded")
        return df
