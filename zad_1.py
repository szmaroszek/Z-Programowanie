class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks)/len(self.marks) > 50


student1 = Student("Szymon", [50, 50, 59])

print(student1.is_passed())
