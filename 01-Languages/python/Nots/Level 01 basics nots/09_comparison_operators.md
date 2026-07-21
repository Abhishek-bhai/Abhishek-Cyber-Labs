# Comparison Operators in Python

---

# What are Comparison Operators?

Comparison Operators do values ko compare karte hain.

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

# List of Comparison Operators

| Operator | Meaning |
|-----------|----------|
| == | Equal To |
| != | Not Equal To |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than Equal To |
| <= | Less Than Equal To |

---

# Equal To (==)

Check karta hai ki dono values equal hain ya nahi.

Example:

```python
print(10 == 10)
```

Output:

```text
True
```

---

Example:

```python
print(10 == 20)
```

Output:

```text
False
```

---

# Not Equal To (!=)

Check karta hai ki values different hain ya nahi.

Example:

```python
print(10 != 20)
```

Output:

```text
True
```

---

Example:

```python
print(10 != 10)
```

Output:

```text
False
```

---

# Greater Than (>)

Example:

```python
print(20 > 10)
```

Output:

```text
True
```

---

Example:

```python
print(5 > 10)
```

Output:

```text
False
```

---

# Less Than (<)

Example:

```python
print(5 < 10)
```

Output:

```text
True
```

---

Example:

```python
print(20 < 10)
```

Output:

```text
False
```

---

# Greater Than Equal To (>=)

Example:

```python
print(20 >= 20)
```

Output:

```text
True
```

---

Example:

```python
print(30 >= 20)
```

Output:

```text
True
```

---

Example:

```python
print(10 >= 20)
```

Output:

```text
False
```

---

# Less Than Equal To (<=)

Example:

```python
print(10 <= 20)
```

Output:

```text
True
```

---

Example:

```python
print(20 <= 20)
```

Output:

```text
True
```

---

Example:

```python
print(50 <= 20)
```

Output:

```text
False
```

---

# Comparison with Variables

Example:

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

---

Example:

```python
marks = 30

print(marks >= 33)
```

Output:

```text
False
```

---

# Comparison with Input

```python
age = int(input("Enter Age: "))

print(age >= 18)
```

Input:

```text
20
```

Output:

```text
True
```

---

# String Comparison

Example:

```python
print("Python" == "Python")
```

Output:

```text
True
```

---

Example:

```python
print("Python" == "python")
```

Output:

```text
False
```

Python case-sensitive hai.

---

# Boolean Comparison

Example:

```python
print(True == True)
```

Output:

```text
True
```

---

Example:

```python
print(True == False)
```

Output:

```text
False
```

---

# Real World Example

Voting Eligibility

```python
age = 18

print(age >= 18)
```

Output:

```text
True
```

---

# Pass / Fail Example

```python
marks = 45

print(marks >= 33)
```

Output:

```text
True
```

---

# Salary Check

```python
salary = 50000

print(salary > 30000)
```

Output:

```text
True
```

---

# Common Mistakes

Wrong:

```python
print(10 = 10)
```

Error

Reason:

```python
=
```

Assignment Operator hai.

---

Correct:

```python
print(10 == 10)
```

---

Wrong:

```python
name = "Python"

print(name = "Python")
```

Error

---

Correct:

```python
print(name == "Python")
```

---

# Difference Between = and ==

Assignment:

```python
age = 18
```

Means:

```text
Value Store Karna
```

---

Comparison:

```python
age == 18
```

Means:

```text
Compare Karna
```

---

# Summary

You Learned:

- ==
- !=
- >
- <
- >=
- <=
- Boolean Results
- Variable Comparison
- Input Comparison
- String Comparison
- = vs ==