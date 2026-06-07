<!---------------------------------
LEVEL 2 — Intermediate PYTHON 
---------------------------------->

<!-------------------------------------
  --- Topic- 01 Class and Object ----
------------------------------------->

## Definition

Class is a blueprint used to create objects.

Object is an instance of a class.

### Real World Example

* Class = Car Design
* Object = Actual Car

A class defines the structure, while objects are the real entities created from that structure.

---

## Syntax

```python
class ClassName:
    pass

object_name = ClassName()
```

---

## Example 1

```python
class Car:

    brand = "BMW"
    speed = 250


car_1 = Car()

print(car_1.brand)
print(car_1.speed)
```

### Output

```text
BMW
250
```

---

## Example 2

```python
class Student:

    name = "Abhishek"
    age = 20


student_1 = Student()

print(student_1.name)
print(student_1.age)
```

### Output

```text
Abhishek
20
```

---

## Example 3

```python
class Laptop:

    ram = "16GB"
    processor = "Intel i7"


laptop_1 = Laptop()

print(laptop_1.ram)
print(laptop_1.processor)
```

### Output

```text
16GB
Intel i7
```

---

## Explanation

### Class

A class is used to define attributes and methods.

```python
class Car:
```

---

### Object

An object is created using the class.

```python
car_1 = Car()
```

---

### Accessing Data

Object data can be accessed using dot notation.

```python
car_1.brand
car_1.speed
```

---

## Important Points

* Class is a blueprint.
* Object is an instance of a class.
* Multiple objects can be created from one class.
* Dot notation is used to access attributes.
* Classes help organize code.

---

## Real World Uses

* User Systems
* Bank Accounts
* Cars
* Students
* Products
* APIs
* Django Models

---

## Summary

* Class = Blueprint
* Object = Real Instance
* Objects are created from classes.
* Objects can access class attributes using dot notation.

```
```




<!-----------------------------------------
  --- Topic- 02 Constructor and Self ----
------------------------------------------>

# Constructor and Self

## Definition

A constructor is a special method that automatically runs when an object is created.

In Python, the constructor is written using:

```python
__init__()
```

The `self` keyword represents the current object.

---

## Why Constructor is Used

Constructor is used to initialize object data.

Without a constructor, every object would have the same fixed values.

With a constructor, each object can have different values.

---

## Syntax

```python
class ClassName:

    def __init__(self, value):
        self.value = value
```

---

## Example 1

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student_1 = Student("Abhishek", 20)

print(student_1.name)
print(student_1.age)
```

### Output

```text
Abhishek
20
```

---

## Example 2

```python
class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


mobile_1 = Mobile("Samsung", 25000)
mobile_2 = Mobile("iPhone", 60000)

print(mobile_1.brand, mobile_1.price)
print(mobile_2.brand, mobile_2.price)
```

### Output

```text
Samsung 25000
iPhone 60000
```

---

## Example 3

```python
class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed


car_1 = Car("BMW", 250)
car_2 = Car("Ferrari", 320)

print(car_1.brand, car_1.speed)
print(car_2.brand, car_2.speed)
```

### Output

```text
BMW 250
Ferrari 320
```

---

# Understanding self

## What is self?

`self` represents the current object.

When an object calls a method, Python automatically passes that object to `self`.

---

## Example

```python
class Student:

    def __init__(self, name):
        self.name = name


student_1 = Student("Abhishek")
```

Python internally does something similar to:

```python
Student.__init__(student_1, "Abhishek")
```

So:

```python
self = student_1
```

---

## Why self is Needed

Without self:

```python
class Student:

    def __init__(self, name):
        name = name
```

Python would not know where to store the data.

Correct way:

```python
self.name = name
```

Meaning:

Store the value inside the current object.

---

## Memory Visualization

```text
student_1
│
└── name = Abhishek
```

Here:

```python
self.name
```

points to:

```python
student_1.name
```

---

## Important Points

- `__init__()` is called automatically when an object is created.
- Constructor initializes object data.
- `self` represents the current object.
- Every object has its own data.
- `self.variable` creates instance variables.

---

## Real World Uses

- User Accounts
- Products
- Students
- Bank Accounts
- Django Models
- API Objects

---

## Summary

- Constructor = `__init__()`
- Runs automatically during object creation.
- Used to initialize object data.
- `self` refers to the current object.
- `self.variable` stores data inside the object.



<!-------------------------------------
  --- Topic- 01 Class and Object ----
------------------------------------->

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

