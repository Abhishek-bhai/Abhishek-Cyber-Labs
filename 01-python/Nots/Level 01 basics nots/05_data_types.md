# Data Types in Python

---

# What is a Data Type?

Data Type batata hai ki variable ke andar kis type ka data store hai.

Example:

```python
name = "Abhishek"
```

Yaha:

```python
str
```

type ka data store hai.

---

# Why Data Types?

Python ko pata hona chahiye:

- Number hai ya Text
- True/False hai
- List hai ya Dictionary

Isi liye Data Types use hote hain.

---

# Check Data Type

Syntax:

```python
type(variable)
```

Example:

```python
name = "Abhishek"

print(type(name))
```

Output:

```python
<class 'str'>
```

---

# Main Data Types

Python me commonly use hone wale data types:

```text
int
float
str
bool
list
tuple
set
dict
complex
```

---

# Integer (int)

Whole Numbers

Examples:

```python
10
20
100
5000
-50
```

Program:

```python
age = 18

print(type(age))
```

Output:

```python
<class 'int'>
```

---

# Float

Decimal Numbers

Examples:

```python
5.5
99.99
10.25
```

Program:

```python
price = 99.99

print(type(price))
```

Output:

```python
<class 'float'>
```

---

# String (str)

Text Data

Examples:

```python
"Python"
"Abhishek"
"Hello"
```

Program:

```python
name = "Abhishek"

print(type(name))
```

Output:

```python
<class 'str'>
```

---

# String Quotes

Double Quotes:

```python
name = "Python"
```

Single Quotes:

```python
name = 'Python'
```

Both are valid.

---

# Boolean (bool)

Only Two Values:

```python
True
False
```

Program:

```python
is_student = True

print(type(is_student))
```

Output:

```python
<class 'bool'>
```

---

# Boolean Example

```python
age = 18

print(age >= 18)
```

Output:

```python
True
```

---

# Complex Number

Format:

```python
a + bj
```

Example:

```python
x = 2 + 3j

print(type(x))
```

Output:

```python
<class 'complex'>
```

Mostly:

- Scientific Computing
- Mathematics

---

# List

Multiple Values Store Karne Ke Liye

Syntax:

```python
[]
```

Example:

```python
fruits = ["Apple", "Mango", "Banana"]
```

Check Type:

```python
print(type(fruits))
```

Output:

```python
<class 'list'>
```

---

# Tuple

List jaisa hota hai.

Difference:

Tuple immutable hota hai.

Syntax:

```python
()
```

Example:

```python
colors = ("Red", "Blue", "Green")
```

Output:

```python
<class 'tuple'>
```

---

# Set

Unique Values Store Karta Hai.

Syntax:

```python
{}
```

Example:

```python
numbers = {1, 2, 3, 4}
```

Output:

```python
<class 'set'>
```

Duplicate Remove Example:

```python
data = {1, 1, 2, 2, 3}

print(data)
```

Output:

```python
{1, 2, 3}
```

---

# Dictionary

Key-Value Pair

Syntax:

```python
{}
```

Example:

```python
student = {
    "name": "Abhishek",
    "age": 18
}
```

Output:

```python
<class 'dict'>
```

---

# Data Type Comparison

| Data Type | Example |
|------------|----------|
| int | 10 |
| float | 10.5 |
| str | "Python" |
| bool | True |
| list | [1,2,3] |
| tuple | (1,2,3) |
| set | {1,2,3} |
| dict | {"name":"Abhi"} |
| complex | 2+3j |

---

# Multiple Data Types

```python
name = "Abhishek"
age = 18
height = 5.8
is_student = True
```

---

# Dynamic Typing

Python me variable ka type change ho sakta hai.

Example:

```python
x = 10

print(type(x))
```

Output:

```python
<class 'int'>
```

---

Now:

```python
x = "Python"

print(type(x))
```

Output:

```python
<class 'str'>
```

---

# Common Mistakes

Wrong:

```python
age = "18"
```

Agar number ki tarah use karna hai to:

```python
age = 18
```

---

Wrong:

```python
is_student = true
```

Correct:

```python
is_student = True
```

Python me:

```python
True
False
```

Capital letter se likhte hain.

---

# Summary

You Learned:

- Data Types
- int
- float
- str
- bool
- complex
- list
- tuple
- set
- dict
- type()
- Dynamic Typing