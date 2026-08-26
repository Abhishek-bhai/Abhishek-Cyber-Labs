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