class Employee():

    raise_rate = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emp += 1
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_rate)
        # access to class variable should either through class itself or instance of class


emp_1 = Employee('Test', 'Case', 5000)

# print(emp_1.email)
# print(emp_1.fullname())
# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# parentheses means execute the function 
# print(emp_1.pay)

print(emp_1.__dict__)

print(emp_1.__dict__)


# Decoration 
def decoration_function(ori_func):
    def wrapper_function():
        return ori_func
    return wrapper_function

def display_f