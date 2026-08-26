# Methods

## Definition

A method is a function defined inside a class.

Methods are used to perform actions using object data.

Methods help objects perform specific tasks.

---

## Why Methods are Used

Methods allow objects to:

- Display information
- Perform calculations
- Update data
- Execute actions

Without methods, objects would only store data.

---

## Syntax

```python
class ClassName:

    def method_name(self):
        print("Hello")
```

---

## Example 1

```python
class Student:

    def show_name(self):
        print("Abhishek")


student_1 = Student()

student_1.show_name()
```

### Output

```text
Abhishek
```

---

## Example 2

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(self.brand)


car_1 = Car("BMW")

car_1.show_brand()
```

### Output

```text
BMW
```

---

## Example 3

```python
class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Price: {self.price}")


mobile_1 = Mobile("Samsung", 25000)

mobile_1.show_info()
```

### Output

```text
Brand: Samsung
Price: 25000
```

---

# Understanding Methods

A method is simply a function that belongs to a class.

Example:

```python
class Student:

    def show_name(self):
        print("Abhishek")
```

Here:

```python
show_name()
```

is a method.

---

# Calling a Method

Methods are called using an object.

```python
student_1.show_name()
```

---

# Why self is Used in Methods

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)
```

When:

```python
student_1.show_name()
```

runs,

Python internally does something similar to:

```python
Student.show_name(student_1)
```

Therefore:

```python
self = student_1
```

---

# Methods Using Object Data

Example:

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name)
        print(self.salary)
```

Object:

```python
employee_1 = Employee("Abhishek", 50000)
```

Method:

```python
employee_1.show_details()
```

Output:

```text
Abhishek
50000
```

---

# Important Points

- Methods are functions inside classes.
- Methods are called using objects.
- Methods can access object data using self.
- Methods make objects perform actions.
- Methods improve code organization.

---

# Real World Uses

Methods are used in:

- Banking Systems
- Authentication Systems
- E-Commerce Applications
- Django Models
- APIs
- Cybersecurity Tools

Examples:

```python
user.login()
user.logout()

account.deposit()
account.withdraw()

car.start()
car.stop()
```

---

# Summary

- Method = Function inside a class.
- Methods perform actions.
- Methods can use object data.
- self gives access to current object data.
- Methods are called using objects.