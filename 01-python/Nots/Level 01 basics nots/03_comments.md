# Comments in Python

---

# What are Comments?

Comments aise statements hote hain jo Python execute nahi karta.

Comments ka use code ko explain karne ke liye kiya jata hai.

Benefits:

- Code ko samajhna easy hota hai
- Team work me help milti hai
- Future me code maintain karna easy hota hai
- Notes likhne ke liye useful

---

# Single Line Comment

Single line comment ke liye `#` ka use hota hai.

Syntax:

```python
# Comment
```

Example:

```python
# This is a comment

print("Hello")
```

Output:

```text
Hello
```

Comment execute nahi hoga.

---

# Multiple Single Line Comments

```python
# Name Program
# Created By Abhishek
# Version 1.0

print("Hello World")
```

---

# Inline Comment

Code ke baad bhi comment likh sakte hain.

Example:

```python
age = 18  # User age
```

```python
print(age)  # Print age
```

Output:

```text
18
```

---

# Multi Line Comment

Python me officially multi-line comment nahi hota.

Lekin documentation ya notes ke liye triple quotes ka use kiya jata hai.

Example:

```python
"""
This is
multi line
text
"""
```

---

# Triple Double Quotes

```python
"""
Python Notes
Created By Abhishek
"""
```

---

# Triple Single Quotes

```python
'''
Python Notes
Created By Abhishek
'''
```

---

# Docstring

Function, Class aur Module explain karne ke liye Docstring use hoti hai.

Example:

```python
def greet():
    """
    This function prints greeting.
    """
    print("Hello")
```

---

# Why Comments are Important?

Without Comment:

```python
r = 5
a = 3.14 * r * r

print(a)
```

Samajhna mushkil ho sakta hai.

---

With Comment:

```python
# Radius

r = 5

# Area of Circle

a = 3.14 * r * r

print(a)
```

Code jyada readable lagta hai.

---

# Good Comment Example

```python
# Calculate total marks

maths = 80
science = 90

total = maths + science

print(total)
```

---

# Bad Comment Example

```python
# Variable x

x = 10

# Print x

print(x)
```

Aise comments unnecessary hote hain.

---

# Commenting Shortcut in VS Code

Windows:

```text
Ctrl + /
```

Mac:

```text
Cmd + /
```

---

# Common Mistakes

Wrong:

```python
This is comment
```

Error aayega.

Correct:

```python
# This is comment
```

---

# Summary

You Learned:

- Single Line Comment
- Inline Comment
- Multi Line Comment
- Triple Quotes
- Docstring
- Good vs Bad Comments
- VS Code Shortcut