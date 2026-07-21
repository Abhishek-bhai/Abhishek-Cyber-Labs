# Method Overriding

## Definition

Method Overriding is a feature of Object-Oriented Programming (OOP) where a child class provides its own implementation of a method that already exists in the parent class.

The child class method replaces the parent class method when called using a child object.

---

## Why Method Overriding is Used

Method Overriding allows child classes to customize or modify inherited behavior.

Benefits:

- Customize parent functionality
- Achieve Polymorphism
- Improve flexibility
- Write reusable code

---

## Syntax

```python
class Parent:

    def method_name(self):
        print("Parent Method")


class Child(Parent):

    def method_name(self):
        print("Child Method")
```

---

## Example 1

```python
class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog_1 = Dog()

dog_1.sound()
```

### Output

```text
Dog barks
```

---

## Example 2

```python
class Vehicle:

    def start(self):
        print("Vehicle is started")


class Bike(Vehicle):

    def start(self):
        print("Bike is started")


bike_1 = Bike()

bike_1.start()
```

### Output

```text
Bike is started
```

---

## Example 3

```python
class Person:

    def work(self):
        print("Person is working")


class Teacher(Person):

    def work(self):
        print("Teacher is teaching")


teacher_1 = Teacher()

teacher_1.work()
```

### Output

```text
Teacher is teaching
```

---

# How Method Overriding Works

Parent Class:

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")
```

Child Class:

```python
class Car(Vehicle):

    def start(self):
        print("Car Started")
```

Object:

```python
car_1 = Car()

car_1.start()
```

Output:

```text
Car Started
```

Python first looks inside the child class.

If the method exists there, Python uses the child class version.

---

# Parent Method vs Child Method

Parent:

```python
def start(self):
    print("Vehicle Started")
```

Child:

```python
def start(self):
    print("Car Started")
```

Because both methods have the same name:

```python
start()
```

The child method overrides the parent method.

---

# Overriding with Inheritance

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Cat(Animal):

    def sound(self):
        print("Meow")


cat_1 = Cat()

cat_1.sound()
```

### Output

```text
Meow
```

The child class changes the behavior inherited from the parent class.

---

# Important Rules

For overriding:

- Method name must be the same.
- Parameters should usually be the same.
- Child class must inherit from parent class.

Example:

```python
class Parent:

    def show(self):
        pass


class Child(Parent):

    def show(self):
        pass
```

---

# Real World Example

```text
Vehicle
│
├── Car
├── Bike
└── Bus
```

All vehicles can start.

But each vehicle may start differently.

```python
car.start()
bike.start()
bus.start()
```

Each class can override the same method.

---

# Method Overriding vs Inheritance

## Inheritance

Reuse parent methods.

Example:

```python
dog_1.eat()
```

Uses parent method.

---

## Method Overriding

Modify parent methods.

Example:

```python
dog_1.sound()
```

Uses child method instead of parent method.

---

# Real World Uses

Method Overriding is commonly used in:

- Django Models
- APIs
- Authentication Systems
- Payment Systems
- GUI Applications
- Cybersecurity Tools

Examples:

```text
Payment
│
├── UPI Payment
├── Card Payment
└── Net Banking
```

Each can override:

```python
process_payment()
```

---

# Important Points

- Child class can modify parent methods.
- Same method name is required.
- Supports Polymorphism.
- Increases flexibility.
- Makes code reusable and maintainable.

---

# Summary

- Method Overriding allows a child class to replace a parent class method.
- The child version is executed instead of the parent version.
- Used with inheritance.
- Supports code customization.
- Forms the foundation of Polymorphism.