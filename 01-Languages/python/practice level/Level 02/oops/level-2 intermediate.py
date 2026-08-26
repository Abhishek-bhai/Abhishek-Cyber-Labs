# ==================== #
# == Level-02 Start == #
# ==================== #

# ======================================= #
# ============== Topic 01 =============== #
# == OOP (Object Oriented Programming) == #
# ======================================= #

# ================ #
# == Example 01 == #
# ================ #

# class Car:
#     brand = "BMW"
#     speed = 250

# C1 = Car()

# print(C1.brand, C1.speed)


# ================ #
# == Example 02 == #
# ================ #

# class Phone:
#      model = "Oppo A18"
#      price = 10000

# P1 = Phone()

# print (P1.model, P1.price)


# ================ #
# == Example 03 == #
# ================ #

# class laptop:
#     ram = "16GB"
#     processor = "i7"

# L1 = laptop()

# print(L1.ram, L1.processor)


# ============================================== #
# ================= Topic 02 =================== # 
# =============== Constructor ================== #
# ============================================== #

# ================== #
# == Example 01 == #
# ================== #

# class Car:

#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed


# C1 = Car("BMW", 250)
# C2 = Car("Audi", 300)

# print(C1.brand, C1.speed)
# print(C2.brand, C2.speed)


# ================= #
# == Example 02 == #
# ================= #

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# student_1 = Student("Aman", 21)
# student_2 = Student("Anuj", 20)

# print(f"Name: {student_1.name}, Age: {student_1.age}")
# print(f"Name: {student_2.name}, Age: {student_2.age}")


# class Mobile:

#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price


# mobile_1 = Mobile("iPhone", 40000)
# mobile_2 = Mobile("Samsung", 35000)

# print(f"Brand: {mobile_1.brand}, Price: {mobile_1.price}")
# print(f"Brand: {mobile_2.brand}, Price: {mobile_2.price}")



# ==================================== #
#  =========== Topic 03 ============== #
# == Constructor Method (Functions) == #
# ==================================== #

# ================== #
# == Example 01 == #
# ================== #

# class Car:

#     def __init__(self, name):
#         self.name = name

#     def show_name(self):
#         print(f"Student Name: {self.name}")


# s1 = Student("Abhishek")

# s1.show_name()


# ================== #
# == Example 02 == #
# ================== #

# class Car:

#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def show_details(self):
#         print(f"Car Brand: {self.brand}")
#         print(f"Car Speed: {self.speed}")


# car_1 = Car("BMW", 250)
# car_2 = Car("Ferrari", 300)

# car_1.show_details()
# car_2.show_details()

