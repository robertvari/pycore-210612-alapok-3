class Employee:
    def __init__(self, name):
        self._name = name

    # protected method
    def _calc_salary(self):
        print("_calc_salary called")

    # private method
    def __calc_work_days(self):
        print("__calc_work_days called")


robert = Employee("Robert")