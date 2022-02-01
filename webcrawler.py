class Employee():

    def __init__(self, firstName, lastName, email, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.salary = salary

    def employeeFullName(self):
        return "{} {}".format(self.firstName, self.lastName)

    def employeeEmail(self):
        return self.email

    def employeeSalary(self):
        return self.salary

    def employeeSalaryRaise(self):
        return self.salary + 5000



employee1 = Employee("Joshua", "Ayegba", "ayegbajoshua@yahoo.com", 5000)
employee2 = Employee("Jennifer", "Ayegba", "ayegbajenny@yahoo.com", 5000)


print(employee1.employeeFullName())
print(employee1.employeeEmail())
print(employee1.employeeSalary())
print(employee1.employeeSalaryRaise())


print(employee2.employeeFullName())
print(employee2.employeeEmail())
print(employee2.employeeSalary())
print(employee2.employeeSalaryRaise())