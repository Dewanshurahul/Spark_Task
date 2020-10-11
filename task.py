from pyspark.sql import functions as func

class Task:

    # Count Number of Employees in each Region
    def region(self, df):
        return df.groupBy('Region').count()

    # Count Number of Employees in each Country
    def country(self, df):
        return df.groupBy('County').count()

    # Count Number of Employees in each City
    def city(self, df):
        return df.groupBy('City').count()

    # Generate Employee Summary
    def summary(self, df):
        avg = df.agg({'Salary': 'avg'})
        max = df.agg({'Salary': 'max'})
        min = df.agg({'Salary': 'min'})
        return avg, max, min, df.describe()

    # Orderby Gender and Salary
    def orderby_gender_salary(self, df):
        return df.sort('Gender','Salary')

    # Hikes Granted based on Month
    def hikes_granted_based_on_month(self, df):
        return df.groupBy('Month Name of Joining').agg(func.countDistinct('Last % Hike').alias('Hikes Granted'))

    # Employee joined based on Month
    def employee_joined_based_on_month(self, df):
        return df.groupBy('Month Name of Joining').count()

    # Salary Wise sort Employee Data
    def sort_salary(self, df):
        return df.sort('Salary')
