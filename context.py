import os
os.environ["PYSPARK_PYTHON"] = '/usr/bin/python3'
from pyspark import SparkContext
from pyspark.sql import SQLContext

class Context:

    def context(self):
        try:
            sc = SparkContext()
            spark = SQLContext(sc)
        except:
            print("Context doesn't get Created")
        return spark


    def load_data(self):
        try:
            df = spark.read.csv("hdfs://localhost:54310/hadoop/input/HR2m.csv",header=True,inferSchema = True)
        except:
            print("Data didn't get loaded")
        return df
