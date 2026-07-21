# Logical Operators in Python

---

# What are Logical Operators?

Logical Operators ka use multiple conditions ko combine karne ke liye hota hai.

Result hamesha:

```python
True
```

ya

```python
False
```

hota hai.

---

# Types of Logical Operators

| Operator | Meaning |
|-----------|----------|
| and | Both conditions True honi chahiye |
| or | Ek bhi condition True ho to True |
| not | Result ko reverse karta hai |

---

# AND Operator

Syntax:

```python
condition1 and condition2
```

Rule:

```text
True and True   -> True
True and False  -> False
False and True  -> False
False and False -> False
```

---

# Example 1

```python
print(10 > 5 and 20 > 10)
```

Output:

```text
True
```

---

# Example 2

```python
print(10 > 5 and 5 > 10)
```

Output:

```text
False
```

---

# Example 3

```python
age = 20

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

---

# OR Operator

Syntax:

```python
condition1 or condition2
```

Rule:

```text
True or True   -> True
True or False  -> True
False or True  -> True
False or False -> False
```

---

# Example 1

```python
print(10 > 5 or 5 > 10)
```

Output:

```text
True
```

---

# Example 2

```python
print(5 > 10 or 2 > 20)
```

Output:

```text
False
```

---

# Example 3

```python
marks = 35

print(marks >= 33 or marks == 30)
```

Output:

```text
True
```

---

# NOT Operator

Syntax:

```python
not condition
```

Rule:

```text
not True  -> False
not False -> True
```

---

# Example 1

```python
print(not True)
```

Output:

```text
False
```

---

# Example 2

```python
print(not False)
```

Output:

```text
True
```

---

# Example 3

```python
print(not (10 > 5))
```

Output:

```text
False
```

---

# Combining Operators

Example:

```python
age = 25

print(age >= 18 and age <= 60)
```

Output:

```text
True
```

---

Example:

```python
print((10 > 5 and 20 > 10) or (5 > 10))
```

Output:

```text
True
```

---

# Real World Example

## Login System

```python
username = "admin"
password = "1234"

print(
    username == "admin"
    and password == "1234"
)
```

Output:

```text
True
```

---

## Voting Eligibility

```python
age = 20
citizen = True

print(age >= 18 and citizen)
```

Output:

```text
True
```

---

## Student Pass Check

```python
marks = 80
attendance = 90

print(
    marks >= 33
    and attendance >= 75
)
```

Output:

```text
True
```

---

## Weekend Check

```python
day = "Sunday"

print(
    day == "Saturday"
    or day == "Sunday"
)
```

Output:

```text
True
```

---

# Operator Precedence

Order:

```text
1. ()
2. not
3. and
4. or
```

---

Example:

```python
print(not True and False)
```

Step:

```python
False and False
```

Output:

```text
False
```

---

# Truthy Values

These behave like True:

```python
1
100
"Python"
[1, 2]
(True)
```

Example:

```python
print(bool("Python"))
```

Output:

```text
True
```

---

# Falsy Values

These behave like False:

```python
0
0.0
""
[]
()
{}
None
False
```

Example:

```python
print(bool(""))
```

Output:

```text
False
```

---

# Common Mistakes

Wrong:

```python
print(10 > 5 AND 20 > 10)
```

Python Keywords lowercase me hote hain.

Correct:

```python
print(10 > 5 and 20 > 10)
```

---

Wrong:

```python
not 10 > 5 and 20 > 10
```

Complex expressions me brackets use karo.

Correct:

```python
not (10 > 5 and 20 > 10)
```

---

# Summary

You Learned:

- and
- or
- not
- Truth Tables
- Combining Conditions
- Operator Precedence
- Real World Examples