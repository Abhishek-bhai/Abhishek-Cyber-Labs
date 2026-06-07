# Type Casting in Python

---

# What is Type Casting?

Ek Data Type ko dusre Data Type me convert karna
Type Casting kehlata hai.

Example:

```python
age = "18"
```

Ye string hai.

Agar hume ise integer banana ho:

```python
age = int(age)
```

---

# Why Type Casting?

Input function hamesha string return karta hai.

Example:

```python
age = input("Enter Age: ")
```

User:

```text
18
```

Python:

```python
"18"
```

Store karega.

Number ki tarah use karne ke liye:

```python
age = int(age)
```

---

# Types of Casting

1. Implicit Type Casting
2. Explicit Type Casting

---

# Implicit Type Casting

Python automatically conversion karta hai.

Example:

```python
a = 10
b = 2.5

result = a + b

print(result)
print(type(result))
```

Output:

```text
12.5
<class 'float'>
```

Python ne int ko float me convert kar diya.

---

# Explicit Type Casting

Programmer khud conversion karta hai.

Example:

```python
age = "18"

age = int(age)
```

---

# int()

String ya Float ko Integer me convert karta hai.

Example:

```python
x = "100"

print(int(x))
```

Output:

```text
100
```

---

Float to Integer:

```python
price = 99.99

print(int(price))
```

Output:

```text
99
```

Decimal part remove ho jata hai.

---

# float()

Integer ya String ko Float me convert karta hai.

Example:

```python
x = 10

print(float(x))
```

Output:

```text
10.0
```

---

String to Float:

```python
price = "99.99"

print(float(price))
```

Output:

```text
99.99
```

---

# str()

Kisi bhi value ko String me convert karta hai.

Example:

```python
age = 18

print(str(age))
```

Output:

```text
18
```

Type:

```python
print(type(str(age)))
```

Output:

```python
<class 'str'>
```

---

# bool()

Value ko Boolean me convert karta hai.

---

False Values:

```python
False
0
0.0
""
[]
()
{}
set()
None
```

Sab False return karte hain.

Example:

```python
print(bool(0))
```

Output:

```text
False
```

---

Example:

```python
print(bool(""))
```

Output:

```text
False
```

---

# True Values

Example:

```python
print(bool(1))
```

Output:

```text
True
```

---

Example:

```python
print(bool("Python"))
```

Output:

```text
True
```

---

Example:

```python
print(bool(100))
```

Output:

```text
True
```

---

# list()

String ko List me convert karta hai.

Example:

```python
name = "Python"

print(list(name))
```

Output:

```python
['P', 'y', 't', 'h', 'o', 'n']
```

---

# tuple()

Example:

```python
data = [1, 2, 3]

print(tuple(data))
```

Output:

```python
(1, 2, 3)
```

---

# set()

Example:

```python
data = [1, 1, 2, 2, 3]

print(set(data))
```

Output:

```python
{1, 2, 3}
```

---

# Dictionary Conversion

Example:

```python
data = [
    ("name", "Abhishek"),
    ("age", 18)
]

print(dict(data))
```

Output:

```python
{
'name': 'Abhishek',
'age': 18
}
```

---

# Common Errors

Example:

```python
int("hello")
```

Output:

```text
ValueError
```

Reason:

"hello" number nahi hai.

---

Correct:

```python
int("100")
```

---

Example:

```python
float("abc")
```

Output:

```text
ValueError
```

---

# Real World Example

Without Casting:

```python
a = input("Enter First Number: ")
b = input("Enter Second Number: ")

print(a + b)
```

Input:

```text
10
20
```

Output:

```text
1020
```

---

With Casting:

```python
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print(a + b)
```

Output:

```text
30
```

---

# Important Conversion Table

| From  | To   | Function |
|-------|-------|---------|
| str   | int   | int()   |
| str   | float | float() |
| int   | str   | str()   |
| int   | float | float() |
| float | int   | int()   |
| any   | bool  | bool()  |
| list  | tuple | tuple() |
| list  | set   | set()   |

---

# Summary

You Learned:

- Type Casting
- Implicit Casting
- Explicit Casting
- int()
- float()
- str()
- bool()
- list()
- tuple()
- set()
- dict()
- Conversion Errors