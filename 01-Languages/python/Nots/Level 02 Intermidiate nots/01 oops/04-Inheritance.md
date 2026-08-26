# Inheritance 
This is first pillar of oops

## Definition

Inheritance is a feature of Object-Oriented Programming (OOP) that allows a child class to inherit properties and methods from a parent class.

Inheritance helps in code reusability and reduces duplication.

---

## Why Inheritance is Used

Without inheritance, we may need to write the same code multiple times.

Inheritance allows child classes to reuse existing code from parent classes.

Benefits:

- Code Reusability
- Better Code Organization
- Easier Maintenance
- Reduced Duplication

---

## Syntax

```python
class Parent:
    pass


class Child(Parent):
    pass
```

---

## Example 1

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    pass


dog_1 = Dog()

dog_1.eat()
```

### Output

```text
Animal is eating
```

---

## Example 2

```python
class Person:

    def show_name(self):
        print("My name is Abhishek")


class Student(Person):
    pass


student_1 = Student()

student_1.show_name()
```

### Output

```text
My name is Abhishek
```

---

## Example 3

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def show_brand(self):
        print("BMW")


car_1 = Car()

car_1.start()
car_1.show_brand()
```

### Output

```text
Vehicle Started
BMW
```

---

# Understanding Parent and Child Classes

## Parent Class

The class whose properties and methods are inherited.

Example:

```python
class Animal:
```

Animal is the parent class.

---

## Child Class

The class that inherits from another class.

Example:

```python
class Dog(Animal):
```

Dog is the child class.

---

# How Inheritance Works

Example:

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass
```

Dog does not have an `eat()` method.

However, because Dog inherits from Animal:

```python
dog_1.eat()
```

works successfully.

---

# Real World Example

```text
Vehicle
│
├── Car
├── Bike
└── Bus
```

All vehicles can:

- Start
- Stop

Each child class can also have its own unique methods.

---

# Multiple Child Classes Example

```python
class Animal:

    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog_1 = Dog()
cat_1 = Cat()

dog_1.eat()
cat_1.eat()
```

### Output

```text
Eating
Eating
```

---

# Important Points

- Inheritance allows code reuse.
- Parent class provides methods and attributes.
- Child class can access parent methods.
- Child class can also define its own methods.
- Inheritance creates a relationship between classes.

---

# Built-in Functions

## issubclass()

Checks whether a class is derived from another class.

Example:

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


print(issubclass(Car, Vehicle))
```

### Output

```text
True
```

---

## isinstance()

Checks whether an object belongs to a class.

Example:

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


car_1 = Car()

print(isinstance(car_1, Car))
```

### Output

```text
True
```

---

# Real World Uses

Inheritance is commonly used in:

- Django Models
- Authentication Systems
- User Management Systems
- Payment Systems
- APIs
- Cybersecurity Tools

Examples:

```text
User
│
├── Admin
├── Moderator
└── Customer
```

---

# Summary

- Inheritance allows one class to inherit from another class.
- Parent class provides common functionality.
- Child class reuses parent code.
- Improves code reusability.
- Reduces duplication.
- Creates hierarchical relationships between classes.