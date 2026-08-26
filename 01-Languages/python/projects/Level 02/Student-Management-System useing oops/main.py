class Student: # Student("Abhishek", 20, "Diploma CSE")

    def __init__(self, name, age, course): # name = Abhishek , age = 20, course = Diploma CSE
        self.name = name
        self.__age = age
        self.course = course

    def show_details(self):
        print("\nStudent Details")
        print(f"Name   : {self.name}")
        print(f"Age    : {self.__age}")
        print(f"Course : {self.course}")

    def get_age(self):
        return self.__age

    def set_age(self, age):

        if 0 <= age <= 120:
            self.__age = age
        else:
            print("Invalid Age")


student_1 = Student(
    "Abhishek",
    20,
    "Diploma CSE"
)

student_2 = Student(
    "Aman",
    21,
    "BCA"
)

student_1.show_details()
student_2.show_details()

student_1.set_age(22)

print("\nUpdated Age:")
print(student_1.get_age())

