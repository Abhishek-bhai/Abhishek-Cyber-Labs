# Abstraction

## Definition

Abstraction is one of the four pillars of Object-Oriented Programming (OOP).

Abstraction means hiding implementation details and showing only essential features to the user.

In simple words:

> Hide complexity and show only necessary functionality.

The user uses the feature without knowing the internal working process.

---

# Why Abstraction is Used

Large applications contain complex logic.

Users do not need to know every internal detail.

Abstraction helps:

- Reduce complexity
- Improve security
- Improve maintainability
- Create a standard structure
- Build scalable applications

---

# Real World Example

## Car Example

When driving a car, you use:

- Steering
- Brake
- Accelerator

You do not need to know:

- Engine combustion process
- Fuel injection system
- Internal gearbox mechanisms

The internal implementation is hidden.

This is Abstraction.

---

## Mobile Phone Example

You use:

- Calling
- Messaging
- Internet

You do not know:

- Network routing
- Signal processing
- Server communication

The complexity is hidden.

---

# Abstraction in Python

Python provides abstraction using:

```python
from abc import ABC, abstractmethod
```

Where:

```python
ABC
```

stands for:

```text
Abstract Base Class
```

---

# Abstract Class

An Abstract Class is a class that contains one or more abstract methods.

It acts as a blueprint for child classes.

---

## Syntax

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

---

# Abstract Method

An Abstract Method is a method that has no implementation in the parent class.

Child classes must implement it.

Example:

```python
@abstractmethod
def sound(self):
    pass
```

---

# Example 1

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog_1 = Dog()

dog_1.sound()
```

### Output

```text
Dog Barks
```

---

# Example 2

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


car_1 = Car()

car_1.start()
```

### Output

```text
Car Started
```

---

# Example 3

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("UPI Payment Successful")


upi_1 = UPI()

upi_1.pay()
```

### Output

```text
UPI Payment Successful
```

---

# Rules of Abstract Classes

If a class contains:

```python
@abstractmethod
```

then child classes must implement that method.

---

## Wrong Example

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    pass


dog_1 = Dog()
```

### Output

```text
TypeError
```

Because:

```python
sound()
```

was not implemented.

---

# How Abstraction Works

Parent Class:

```python
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
```

Child Class:

```python
class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

The parent forces every child class to provide its own implementation.

---

# Abstraction vs Encapsulation

| Abstraction | Encapsulation |
|------------|------------|
| Hides complexity | Protects data |
| Focuses on implementation | Focuses on security |
| Uses abstract classes | Uses private variables |
| Shows only essential features | Restricts direct access |

---

# Real World Uses

Abstraction is used in:

- Django Framework
- APIs
- Payment Gateways
- Authentication Systems
- Banking Applications
- Cybersecurity Tools

Examples:

```python
login()

logout()

pay()

authenticate()
```

The user sees only functionality, not internal logic.

---

# Benefits of Abstraction

- Cleaner Design
- Better Security
- Easier Maintenance
- Scalable Applications
- Standardized Structure

---

# Important Points

- Abstraction hides complexity.
- Uses Abstract Classes.
- Uses Abstract Methods.
- Child classes must implement abstract methods.
- Helps build large applications.

---

# Summary

- Abstraction hides implementation details.
- Shows only essential functionality.
- Implemented using ABC and @abstractmethod.
- Child classes are required to implement abstract methods.
- One of the four pillars of OOP.

---

# OOP Pillars Summary

## 1. Encapsulation

Protect data using private variables.

Example:

```python
self.__balance
```

---

## 2. Inheritance

Reuse code from a parent class.

Example:

```python
class Dog(Animal)
```

---

## 3. Polymorphism

One method, multiple forms.

Example:

```python
sound()
```

Different behavior for different objects.

---

## 4. Abstraction

Hide complexity and expose only necessary functionality.

Example:

```python
@abstractmethod
```

Used to define a standard structure.