# Class Variables vs Instance Variables

## Definition

In Python OOP, variables can be divided into two types:

1. Class Variables
2. Instance Variables

Class Variables belong to the class itself and are shared by all objects.

Instance Variables belong to individual objects and each object can have different values.

---

# Class Variables

## Definition

A Class Variable is a variable that belongs to the class.

It is shared among all objects created from that class.

---

## Syntax

```python
class Student:

    school = "ABC School"
```

Here:

```python
school
```

is a Class Variable.

---

## Example 1

```python
class Student:

    school = "ABC School"


student_1 = Student()
student_2 = Student()

print(student_1.school)
print(student_2.school)
```

### Output

```text
ABC School
ABC School
```

---

## Example 2

```python
class Employee:

    company = "Google"


employee_1 = Employee()
employee_2 = Employee()

print(employee_1.company)
print(employee_2.company)
```

### Output

```text
Google
Google
```

---

# Instance Variables

## Definition

Instance Variables belong to individual objects.

Each object has its own copy of instance variables.

Instance Variables are usually created inside the constructor using:

```python
self.variable_name
```

---

## Syntax

```python
class Student:

    def __init__(self, name):
        self.name = name
```

Here:

```python
self.name
```

is an Instance Variable.

---

## Example 1

```python
class Student:

    def __init__(self, name):
        self.name = name


student_1 = Student("Abhishek")
student_2 = Student("Anuj")

print(student_1.name)
print(student_2.name)
```

### Output

```text
Abhishek
Anuj
```

---

## Example 2

```python
class Mobile:

    def __init__(self, model):
        self.model = model


mobile_1 = Mobile("Samsung")
mobile_2 = Mobile("iPhone")

print(mobile_1.model)
print(mobile_2.model)
```

### Output

```text
Samsung
iPhone
```

---

# Class Variable and Instance Variable Together

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name


student_1 = Student("Abhishek")
student_2 = Student("Anuj")

print(student_1.school)
print(student_1.name)

print(student_2.school)
print(student_2.name)
```

### Output

```text
ABC School
Abhishek
ABC School
Anuj
```

---

# Memory Visualization

## Class Variable

```text
Student Class
│
└── school = ABC School

student_1
student_2
```

One copy shared by all objects.

---

## Instance Variables

```text
student_1
│
└── name = Abhishek

student_2
│
└── name = Anuj
```

Separate copy for each object.

---

# Key Differences

| Class Variable | Instance Variable |
|----------|----------|
| Belongs to class | Belongs to object |
| Shared by all objects | Separate for each object |
| Defined inside class body | Defined using self |
| One copy | Multiple copies |

---

# Real World Example

## Class Variable

```python
company = "Google"
```

All employees belong to the same company.

---

## Instance Variables

```python
self.name
self.salary
```

Each employee has different details.

---

# Example

```python
class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee_1 = Employee("Abhishek", 50000)
employee_2 = Employee("Aman", 60000)

print(employee_1.company)
print(employee_1.name)
print(employee_1.salary)

print(employee_2.company)
print(employee_2.name)
print(employee_2.salary)
```

---

# Real World Uses

Class Variables:

- Company Name
- School Name
- Country Name
- Tax Rate

Instance Variables:

- User Name
- Password
- Age
- Salary
- Product Price

---

# Important Points

- Class Variables are shared.
- Instance Variables are unique.
- Instance Variables use self.
- Class Variables are defined directly inside the class.
- Every object gets its own instance variable values.

---

# Summary

## Class Variable

- Belongs to class
- Shared by all objects
- Single copy

## Instance Variable

- Belongs to object
- Separate for every object
- Created using self

Class Variables store common data.

Instance Variables store object-specific data.