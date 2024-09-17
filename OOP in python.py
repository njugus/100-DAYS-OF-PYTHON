# composition and aggregation
# composition
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay * 12) + self.bonus


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary

    def total_salary(self):
        return self.obj_salary.annual_salary()

salary = Salary(1500000, 30000)
employee_1 = Employee("Kelvin", 21, salary)
print(employee_1.total_salary())
