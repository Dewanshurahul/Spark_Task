import context, task, closing

class Runner(context.Context, task.Task, closing.Closing):

    # Calling Context and Data
    def context_and_data(self):
        spark = self.context()
        df = self.load_data(spark)
        return df

    # Calling all the task executing based on task-Number Input
    def run(self, df):
        while True:
            var = input('Enter for Processing: ')
            if var == 'task-1':
                try:
                    self.region(df).show()
                    self.city(df).show()
                    self.country(df).show()
                except:
                    print("Task-1 didn't Executed")
            elif var == 'task-2':
                try:
                    avg, max, min, desc = self.summary(df)
                    avg.show()
                    max.show()
                    min.show()
                    desc.show()
                except:
                    print("Task-2 didn't Executed")
            elif var == 'task-3':
                try:
                    self.orderby_gender_salary(df).show()
                except:
                    print("Task-3 didn't Executed")
            elif var == 'task-4':
                try:
                    self.employee_joined_based_on_month(df).show()
                    self.hikes_granted_based_on_month(df).show()
                except:
                    print("Task-4 didn't executed")
            elif var == 'task-5':
                try:
                    self.sort_salary(df).show()
                except:
                    print("Task-5 didn't Executed")
            elif var == 'done':
                break
            else:
                print("Wrong Input!!")
                continue


if __name__ == '__main__':
    runner = Runner()
    df = runner.context_and_data()
    runner.run(df)
