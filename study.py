#1. class-level variables (aka shared variables)

#example:
class Student:
    school_name = "General High School"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

#using it:
s1 = Student("Elijah")
s2 = Student("Alex")

print(s1.school_name)
print(s2.school_name)