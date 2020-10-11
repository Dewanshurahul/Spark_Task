import context, region, employee_joined_by_month, salary_sort, country, city, summary, closing

class Runner(Context, region, employee_joined_by_month, salary_sort, country, city, summary, Closing):

    def run(self):
        self.context()
        self.load_data()
        self.region()
        self.employee()
        self.closing()

runner = Runner()
runner.run()
