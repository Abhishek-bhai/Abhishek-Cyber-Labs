# Class and Object

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
