# Objective: Develop a Human Resource Management System (HRMS) to manage employee information,
# departments, and projects within an organization using Object-Oriented Programming (OOP) principles,
# specifically focusing on composition and aggregation.

class Employee:
    def __init__(self, id, name, position, email):
        self.id = id
        self.name = name
        self.position = position
        self.email = email

    def employee_info(self):
        print(f"Employee Id : {self.id} \n Employee Name : {self.name} \n Employee position : {self.position}\n"
              f"Employee Contacts : {self.email}")


class Department:
    def __init__(self, name):
        self.name = name
        self.dep_employees = []  # composition

    def dep_info(self):
        print(f"Department Name : {self.name}\n"
              f"{[employee.id for employee in self.dep_employees]}")

    def no_of_employees(self):
        return len(self.dep_employees)

    def add_dep_employees(self, employee):
        self.dep_employees.append(employee)


class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.employees_assigned_to_project = []  # composition

    def project_details(self):
        print(f"Project Name : {self.name} \n Project Description : {self.description}\n"
              f"Project Employees : {[employee for employee in self.employees_assigned_to_project]}")

    def add_employees_to_project(self, employee):
        self.employees_assigned_to_project.append(employee)

    def remove_employees_from_a_project(self, employee):
        self.employees_assigned_to_project.remove(employee)

    def no_of_project_assignees(self):
        return len(self.employees_assigned_to_project)


employee_1 = Employee(234891, "Kelvin Njuguna", "Senior Backend Developer", "kevinnjugush95@gmail.com")
employee_2 = Employee(345667, "Dennis Mutuku", "Finance Manager", "mutuku123@gmail.com")
employee_3 = Employee(345668, "Ruth Wangui", "Accountant", "wangui@gmail.com")
employee_4 = Employee(234894, "Antony Ngunjiri", "Machine Learning Expert", "antonyphoenix123@gmail.com")
employee_5 = Employee(112114, "Saraphine Muigai", "Operations Research Manager", "sara@gmail.com")
employee_6 = Employee(112115, "Lennox Githinji", "Country Manager", "lenox365@gmail.com")

# departments
department_1 = Department("Finance")
department_2 = Department("IT")
department_3 = Department("Production and Operations")

# add employees to their various departments
department_1.add_dep_employees(employee_2)
department_1.add_dep_employees(employee_3)
department_2.add_dep_employees(employee_1)
department_2.add_dep_employees(employee_4)
department_3.add_dep_employees(employee_5)
department_3.add_dep_employees(employee_6)

# add employees to a project
project_1 = Project("MUTCU Project Alpha", "An app for MUTCU")
project_1.add_employees_to_project(employee_1)
project_1.add_employees_to_project(employee_4)
project_1.add_employees_to_project(employee_2)
project_1.add_employees_to_project(employee_3)


# remove an employee from a project
print(project_1.no_of_project_assignees())