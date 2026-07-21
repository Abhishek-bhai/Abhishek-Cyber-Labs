# Getters and Setters

## Definition

Getters and Setters are methods used to access and modify private variables in a controlled way.

They are commonly used with Encapsulation.

- Getter → Read data
- Setter → Update data

Instead of directly accessing private variables, we use methods.

---

# Why Getters and Setters are Used

Private variables cannot be accessed directly.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 90


student_1 = Student()

print(student_1.__marks)
```

### Output

```text
AttributeError
```

Python prevents direct access to private variables.

To safely access data, we use Getters and Setters.

---

# Getter Method

## Definition

A Getter is a method used to retrieve the value of a private variable.

---

## Syntax

```python
def get_variable(self):
    return self.__variable
```

---

## Example 1

```python
class Student:

    def __init__(self):
        self.__marks = 90

    def get_marks(self):
        return self.__marks


student_1 = Student()

print(student_1.get_marks())
```

### Output

```text
90
```

---

## Example 2

```python
class User:

    def __init__(self):
        self.__username = "Abhishek"

    def get_username(self):
        return self.__username


user_1 = User()

print(user_1.get_username())
```

### Output

```text
Abhishek
```

---

# Setter Method

## Definition

A Setter is a method used to modify the value of a private variable.

---

## Syntax

```python
def set_variable(self, value):
    self.__variable = value
```

---

## Example 1

```python
class Student:

    def __init__(self):
        self.__marks = 90

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks


student_1 = Student()

student_1.set_marks(95)

print(student_1.get_marks())
```

### Output

```text
95
```

---

## Example 2

```python
class User:

    def __init__(self):
        self.__username = "Abhishek"

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username


user_1 = User()

user_1.set_username("Aman")

print(user_1.get_username())
```

### Output

```text
Aman
```

---

# Validation Using Setter

One of the biggest advantages of Setters is validation.

Without validation:

```python
marks = -500
```

Invalid values can be stored.

---

## Example

```python
class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):

        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid Marks")

    def get_marks(self):
        return self.__marks


student_1 = Student()

student_1.set_marks(120)

print(student_1.get_marks())
```

### Output

```text
Invalid Marks
0
```

---

# Real World Example

## Bank Account

Without validation:

```python
balance = -100000
```

Invalid balance.

Using Setter:

```python
set_balance()
```

we can check:

```python
if balance >= 0
```

before updating.

---

# Complete Example

```python
class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):

        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid Balance")


account = BankAccount()

account.set_balance(10000)

print(account.get_balance())
```

### Output

```text
10000
```

---

# Benefits of Getters and Setters

- Controlled Access
- Data Validation
- Better Security
- Better Encapsulation
- Cleaner Code

---

# Getters vs Setters

| Getter | Setter |
|----------|----------|
| Reads data | Updates data |
| Returns value | Changes value |
| No modification | Allows modification |
| Used for access | Used for validation |

---

# Real World Uses

Getters and Setters are used in:

- Banking Systems
- User Authentication
- E-Commerce Applications
- Django Models
- APIs
- Employee Management Systems

Examples:

```python
get_balance()

set_balance()

get_salary()

set_salary()
```

---

# Important Points

- Getters read private variables.
- Setters modify private variables.
- Setters can validate data.
- Used with Encapsulation.
- Improve security and maintainability.

---

# Summary

- Getter retrieves private data.
- Setter updates private data.
- Setters allow validation.
- Used to implement Encapsulation properly.
- Commonly used in real-world applications.