# Polymorphism

## Definition

Polymorphism is one of the four pillars of Object-Oriented Programming (OOP).

The word Polymorphism comes from:

- Poly = Many
- Morph = Forms

Polymorphism means:

> One interface, many forms.

It allows the same method name to perform different actions depending on the object.

---

# Why Polymorphism is Used

Polymorphism allows us to write flexible and reusable code.

Instead of creating different method names:

```python
dog_sound()
cat_sound()
cow_sound()
```

We can use:

```python
sound()
```

and let each class provide its own implementation.

---

# Example 1

```python
class Dog:

    def sound(self):
        print("Dog Barks")


class Cat:

    def sound(self):
        print("Cat Meows")


dog_1 = Dog()
cat_1 = Cat()

dog_1.sound()
cat_1.sound()
```

### Output

```text
Dog Barks
Cat Meows
```

---

# Example 2

```python
class Car:

    def start(self):
        print("Car Started")


class Bike:

    def start(self):
        print("Bike Started")


car_1 = Car()
bike_1 = Bike()

car_1.start()
bike_1.start()
```

### Output

```text
Car Started
Bike Started
```

---

# Polymorphism with Inheritance

Polymorphism is commonly achieved using:

- Inheritance
- Method Overriding

---

## Example

```python
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


class Cat(Animal):

    def sound(self):
        print("Cat Meows")
```

Objects:

```python
dog_1 = Dog()
cat_1 = Cat()

dog_1.sound()
cat_1.sound()
```

### Output

```text
Dog Barks
Cat Meows
```

---

# Example Using Loop

```python
class Dog:

    def sound(self):
        print("Dog Barks")


class Cat:

    def sound(self):
        print("Cat Meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

### Output

```text
Dog Barks
Cat Meows
```

---

# How It Works

Python sees:

```python
animal.sound()
```

and automatically calls the correct method depending on the object type.

For Dog object:

```python
Dog.sound()
```

For Cat object:

```python
Cat.sound()
```

---

# Real World Example

Imagine a payment system:

```text
Payment
│
├── UPI
├── Card
└── NetBanking
```

Each class may have:

```python
pay()
```

method.

Example:

```python
upi.pay()
card.pay()
netbanking.pay()
```

Same method name.

Different behavior.

This is Polymorphism.

---

# Polymorphism Through Method Overriding

```python
class Vehicle:

    def start(self):
        print("Vehicle Started")


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")
```

Output depends on the object used.

---

# Benefits of Polymorphism

- Cleaner Code
- Better Flexibility
- Easy Maintenance
- Code Reusability
- Supports Large Applications

---

# Real World Uses

Polymorphism is heavily used in:

- Django Framework
- REST APIs
- Payment Gateways
- Authentication Systems
- GUI Applications
- Cybersecurity Tools

Examples:

```python
login()

logout()

pay()

start()
```

Different classes can implement them differently.

---

# Polymorphism vs Method Overriding

## Method Overriding

A child class replaces a parent class method.

Example:

```python
class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

---

## Polymorphism

Using the same method name across different objects.

Example:

```python
animal.sound()
```

Output changes based on object type.

---

# Important Points

- Same method name.
- Different implementations.
- Achieved using inheritance and overriding.
- Makes code flexible.
- Supports reusable design.

---

# Summary

- Polymorphism means one method, many forms.
- Same method can behave differently for different objects.
- Commonly implemented using inheritance and method overriding.
- Improves flexibility and maintainability.
- One of the four pillars of OOP.