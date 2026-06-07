# Encapsulation

## Definition

Encapsulation is one of the four pillars of Object-Oriented Programming (OOP).

Encapsulation means hiding and protecting data from direct access and allowing controlled access through methods.

In simple words:

> Encapsulation protects object data from unauthorized modification.

---

# Why Encapsulation is Used

Without Encapsulation, anyone can directly modify important data.

Example:

```python
class BankAccount:

    def __init__(self):
        self.balance = 5000


account = BankAccount()

account.balance = -100000

print(account.balance)
```

### Output

```text
-100000
```

This creates invalid data.

Encapsulation helps prevent such problems.

---

# Public Variables

By default, variables in Python are public.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Abhishek"
```

Access:

```python
student_1 = Student()

print(student_1.name)
```

### Output

```text
Abhishek
```

Public variables can be accessed directly from outside the class.

---

# Private Variables

Private variables are created using double underscores:

```python
__variable_name
```

Example:

```python
class BankAccount:

    def __init__(self):
        self.__balance = 5000
```

Here:

```python
__balance
```

is a private variable.

---

# Example 1

```python
class BankAccount:

    def __init__(self):
        self.__balance = 5000


account = BankAccount()

print(account.__balance)
```

### Output

```text
AttributeError
```

Python does not allow direct access to private variables.

---

# Example 2

```python
class Student:

    def __init__(self):
        self.__marks = 85
```

Attempting:

```python
student_1 = Student()

print(student_1.__marks)
```

### Output

```text
AttributeError
```

---

# Accessing Private Variables

Private variables should be accessed through methods.

Example:

```python
class BankAccount:

    def __init__(self):
        self.__balance = 5000

    def show_balance(self):
        print(self.__balance)


account = BankAccount()

account.show_balance()
```

### Output

```text
5000
```

---

# Example 3

```python
class User:

    def __init__(self):
        self.__password = "admin123"

    def show_password(self):
        print(self.__password)


user_1 = User()

user_1.show_password()
```

### Output

```text
admin123
```

---

# Real World Example

Think about an ATM.

You can:

- Check Balance
- Deposit Money
- Withdraw Money

But you cannot directly enter the bank database and change your balance.

The bank protects data using controlled access.

This is the idea behind Encapsulation.

---

# Encapsulation Workflow

```text
User
 │
 ▼
Method
 │
 ▼
Private Data
```

The user interacts with methods.

Methods interact with private variables.

---

# Benefits of Encapsulation

- Data Protection
- Better Security
- Controlled Access
- Easier Maintenance
- Cleaner Code

---

# Encapsulation in Real Applications

Used in:

- Banking Systems
- Authentication Systems
- User Management
- E-Commerce Applications
- Django Projects
- APIs

Examples:

```python
account.withdraw()

account.deposit()

user.change_password()
```

---

# Important Points

- Encapsulation protects data.
- Private variables use double underscores (__).
- Private variables should not be accessed directly.
- Methods provide controlled access.
- Encapsulation improves security.

---

# Public vs Private Variables

| Public Variable | Private Variable |
|----------|----------|
| Accessible from outside | Not directly accessible |
| No special symbol | Uses __ |
| Less secure | More secure |
| Open access | Controlled access |

---

# Summary

- Encapsulation is used to protect data.
- Private variables use double underscores (__).
- Data should be accessed through methods.
- Encapsulation provides security and control.
- It is one of the four pillars of OOP.