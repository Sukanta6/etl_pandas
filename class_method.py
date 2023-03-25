class Employee:
    #pass

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {} {}'.format(self.first, self.last, self.email)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

#emp_1 = Employee()
#print(emp_1.first, emp_1.last, emp_1.email)

print(emp_1.fullname())