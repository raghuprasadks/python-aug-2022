"""
Exception with inheritance
Exception is parent class
InvalidMarks is child class
"""
class InvalidMarks(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr('Invalid marks ' + str(self.data))


marks = int(input('Enter your marks '))
if (marks < 0 or marks > 100):
    print('Marks is invalid ')
    raise InvalidMarks(marks)
else:
    print('Marks is valid')
