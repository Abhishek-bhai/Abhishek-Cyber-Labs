# Arithmetic Operators in Python

---

# What are Arithmetic Operators?

Arithmetic Operators ka use mathematical calculations karne ke liye hota hai.

Examples:

- Addition
- Subtraction
- Multiplication
- Division

---

# List of Arithmetic Operators

| Operator | Meaning |
|-----------|----------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus |
| // | Floor Division |
| ** | Exponent |

---

# Addition Operator (+)

Do values ko add karta hai.

Example:

```python
a = 10
b = 20

print(a + b)
```

Output:

```text
30
```

---

# Addition with Input

```python
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print(a + b)
```

---

# Subtraction Operator (-)

Example:

```python
a = 20
b = 5

print(a - b)
```

Output:

```text
15
```

---

# Multiplication Operator (*)

Example:

```python
a = 10
b = 5

print(a * b)
```

Output:

```text
50
```

---

# Division Operator (/)

Always float return karta hai.

Example:

```python
a = 10
b = 2

print(a / b)
```

Output:

```text
5.0
```

---

Example:

```python
print(5 / 2)
```

Output:

```text
2.5
```

---

# Modulus Operator (%)

Remainder return karta hai.

Example:

```python
print(10 % 3)
```

Output:

```text
1
```

Calculation:

```text
10 ÷ 3

Quotient = 3
Remainder = 1
```

---

# Modulus Uses

Even Number Check:

```python
num = 10

print(num % 2)
```

Output:

```text
0
```

Means:

```text
Even Number
```

---

Odd Number:

```python
num = 11

print(num % 2)
```

Output:

```text
1
```

Means:

```text
Odd Number
```

---

# Floor Division (//)

Decimal hata kar integer quotient return karta hai.

Example:

```python
print(10 // 3)
```

Output:

```text
3
```

---

Example:

```python
print(20 // 6)
```

Output:

```text
3
```

---

# Exponent Operator (**)

Power calculate karta hai.

Example:

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2
```

---

Example:

```python
print(5 ** 2)
```

Output:

```text
25
```

---

# Arithmetic Expressions

Example:

```python
print(10 + 5 * 2)
```

Output:

```text
20
```

Because:

```text
5 * 2 = 10

10 + 10 = 20
```

---

# Operator Precedence

Order:

```text
()
**
* / // %
+ -
```

---

Example:

```python
print(10 + 2 * 5)
```

Output:

```text
20
```

---

Example:

```python
print((10 + 2) * 5)
```

Output:

```text
60
```

---

# Real World Example

Rectangle Area

```python
length = 10
width = 5

area = length * width

print(area)
```

Output:

```text
50
```

---

# Circle Area

```python
radius = 7

area = 3.14 * radius * radius

print(area)
```

---

# Average of 3 Numbers

```python
a = 10
b = 20
c = 30

avg = (a + b + c) / 3

print(avg)
```

Output:

```text
20.0
```

---

# Common Mistakes

Wrong:

```python
10 ^ 2
```

Python me power operator nahi hai.

---

Correct:

```python
10 ** 2
```

---

Wrong:

```python
10 / 0
```

Output:

```text
ZeroDivisionError
```

---

# Summary

You Learned:

- +
- -
- *
- /
- %
- //
- **
- Arithmetic Expressions
- Operator Precedence
- Real World Calculations