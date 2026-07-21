# Variables in Python

---

# What is a Variable?

Variable ek container hota hai jo data ko store karta hai.

Simple words me:

Variable = Data Store Karne Ka Naam

Example:

```python
name = "Abhishek"
```

Yaha:

- name → Variable
- Abhishek → Value

---

# Why Variables?

Without Variable:

```python
print("Abhishek")
print("Abhishek")
print("Abhishek")
```

---

With Variable:

```python
name = "Abhishek"

print(name)
print(name)
print(name)
```

Code clean aur reusable ho jata hai.

---

# Creating Variables

Syntax:

```python
variable_name = value
```

Example:

```python
name = "Abhishek"
age = 18
```

---

# Different Types of Variables

String:

```python
name = "Abhishek"
```

Integer:

```python
age = 18
```

Float:

```python
height = 5.8
```

Boolean:

```python
is_student = True
```

---

# Printing Variables

```python
name = "Abhishek"

print(name)
```

Output:

```text
Abhishek
```

---

Multiple Variables:

```python
name = "Abhishek"
age = 18

print(name)
print(age)
```

Output:

```text
Abhishek
18
```

---

# Changing Variable Value

```python
name = "Abhishek"

print(name)

name = "Rahul"

print(name)
```

Output:

```text
Abhishek
Rahul
```

Latest value store hoti hai.

---

# Multiple Variable Assignment

```python
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)
```

Output:

```text
10
20
30
```

---

# Same Value Assignment

```python
x = y = z = 100

print(x)
print(y)
print(z)
```

Output:

```text
100
100
100
```

---

# Variable Naming Rules

## Rule 1

Variable number se start nahi ho sakta.

Wrong:

```python
1name = "Abhishek"
```

Correct:

```python
name1 = "Abhishek"
```

---

## Rule 2

Special characters allowed nahi hain.

Wrong:

```python
user@name = "Abhishek"
```

Wrong:

```python
user-name = "Abhishek"
```

Correct:

```python
user_name = "Abhishek"
```

---

## Rule 3

Space allowed nahi hai.

Wrong:

```python
user name = "Abhishek"
```

Correct:

```python
user_name = "Abhishek"
```

---

## Rule 4

Keywords use nahi kar sakte.

Wrong:

```python
if = 10
```

Wrong:

```python
class = "Python"
```

---

# Valid Variable Names

```python
name
user_name
student_age
course1
price
total_marks
```

---

# Invalid Variable Names

```python
1name
user-name
user name
class
if
```

---

# Case Sensitive

Python case-sensitive language hai.

```python
name = "Abhishek"
Name = "Rahul"

print(name)
print(Name)
```

Output:

```text
Abhishek
Rahul
```

Dono different variables hain.

---

# Naming Convention

Recommended:

Snake Case

```python
student_name = "Abhishek"
total_marks = 450
user_email = "abc@gmail.com"
```

---

# Real World Example

```python
product_name = "Laptop"
price = 50000
stock = 20

print(product_name)
print(price)
print(stock)
```

---

# Swapping Variables

Traditional Method:

```python
a = 10
b = 20

temp = a
a = b
b = temp

print(a)
print(b)
```

---

Python Method:

```python
a = 10
b = 20

a, b = b, a

print(a)
print(b)
```

Output:

```text
20
10
```

---

# Checking Variable Type

```python
name = "Abhishek"

print(type(name))
```

Output:

```python
<class 'str'>
```

---

# Memory Concept

```python
x = 10
```

Python:

```text
Variable --> Value

x ------> 10
```

Variable value ko reference karta hai.

---

# Common Mistakes

Wrong:

```python
user name = "Abhishek"
```

---

Wrong:

```python
1age = 18
```

---

Wrong:

```python
class = "Python"
```

---

# Summary

You Learned:

- Variables
- Variable Creation
- Variable Reassignment
- Multiple Assignment
- Naming Rules
- Naming Convention
- Case Sensitivity
- Swapping Variables
- type()