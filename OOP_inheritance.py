class Student:

    def __init__(self ,name, age, DOB):
        self.name = name
        self.age = age
        self.DOB = DOB


    def get_stud_data(self, name, age, DOB):
        self.name = name
        self.age = age
        self.DOB = DOB

    def display_stud_data(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Date of Birth {}".format(self.DOB))


class ScienceStudent(Student):

    def disp_sci(self):
        print("Science Students Batch")


class ComputerStudent(Student):
    def disp_com(self):
        print("Computer Students Batch")


sci = ScienceStudent("", "", "")
sci.disp_sci()
name = input("Enter the name :")
age = input("Enter the age :")
dob = input("Enter the date of birth :")

sci.get_stud_data(name, age, dob)
sci.display_stud_data()
