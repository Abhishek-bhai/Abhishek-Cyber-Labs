# Class Methods vs Static Methods vs Instance Methods

## Definition

Python OOP provides three types of methods:

1. Instance Methods
2. Class Methods
3. Static Methods

Each method type serves a different purpose.

Understanding the difference is important for writing clean and professional code.

---

# 1. Instance Methods

## Definition

Instance Methods work with object data.

They can access instance variables and class variables.

Instance Methods use:

```python
self
```

---

## Syntax

```python
class Student:

    def show_name(self):
        print("Student")
```

---

## Example 1

```python
class Student:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


student_1 = Student("Abhishek")

student_1.show_name()
```

### Output

```text
Abhishek
```

---

## Example 2

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(self.name)
        print(self.salary)


employee_1 = Employee("Abhishek", 50000)

employee_1.show_details()
```

---

# Why Instance Methods?

Instance Methods are used when we need object-specific data.

Example:

```python
self.name
self.salary
self.age
```

---

# 2. Class Methods

## Definition

Class Methods work with class data.

They use:

```python
cls
```

and require:

```python
@classmethod
```

decorator.

---

## Syntax

```python
class Student:

    @classmethod
    def method_name(cls):
        pass
```

---

## Example 1

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()
```

### Output

```text
ABC School
```

---

## Example 2

```python
class Employee:

    company = "Google"

    @classmethod
    def show_company(cls):
        print(cls.company)


Employee.show_company()
```

### Output

```text
Google
```

---

# Why Class Methods?

Class Methods are used when we need class-level data.

Examples:

```python
cls.company
cls.school
cls.tax_rate
```

---

# What is cls?

Just like:

```python
self
```

represents the current object,

```python
cls
```

represents the current class.

---

# 3. Static Methods

## Definition

Static Methods do not use:

```python
self
```

or

```python
cls
```

They behave like normal functions placed inside a class.

Static Methods require:

```python
@staticmethod
```

decorator.

---

## Syntax

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
```

---

## Example 1

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

### Output

```text
30
```

---

## Example 2

```python
class MathUtils:

    @staticmethod
    def square(number):
        return number * number


print(MathUtils.square(5))
```

### Output

```text
25
```

---

# Full Example

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

    @classmethod
    def show_school(cls):
        print(cls.school)

    @staticmethod
    def greet():
        print("Welcome Student")
```

Usage:

```python
student_1 = Student("Abhishek")

student_1.show_name()

Student.show_school()

Student.greet()
```

### Output

```text
Abhishek
ABC School
Welcome Student
```

---

# Key Differences

| Feature | Instance Method | Class Method | Static Method |
|----------|----------|----------|----------|
| First Parameter | self | cls | None |
| Works With | Object | Class | Neither |
| Access Instance Variables | Yes | No | No |
| Access Class Variables | Yes | Yes | No |
| Decorator Required | No | @classmethod | @staticmethod |

---

# Real World Example

## Instance Method

```python
user.login()
```

Uses user-specific data.

---

## Class Method

```python
Employee.show_company()
```

Uses class-level data.

---

## Static Method

```python
Calculator.add()
```

Utility function.

---

# Real World Uses

Instance Methods:

- Login Systems
- User Profiles
- Products
- Bank Accounts

Class Methods:

- Company Settings
- School Information
- Shared Configuration

Static Methods:

- Calculations
- Utility Functions
- Validation Functions

---

# Important Points

- Instance Methods use self.
- Class Methods use cls.
- Static Methods use neither self nor cls.
- Class Methods require @classmethod.
- Static Methods require @staticmethod.
- Each method type has a specific purpose.

---

# Summary

## Instance Method

- Uses self
- Works with object data

## Class Method

- Uses cls
- Works with class data

## Static Method

- Uses neither self nor cls
- Utility function inside class

Choosing the correct method type makes code cleaner, reusable, and easier to maintain.