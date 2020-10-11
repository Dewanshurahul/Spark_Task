class Task:

    def region(self, df):
        try:
            df1 = df.select('Region')
            df2 = df1.groupBy('Region').count()
        except:
            print("Data didn't get injested")
	return df2


    def country(self, df):
        return df.groupBy('County').count()
