# print() Function in Python

---

# Introduction

Python me output screen par dikhane ke liye
`print()` function ka use kiya jata hai.

Syntax:

```python
print(value)
```

Example:

```python
print("Hello World")
```

Output:

```text
Hello World
```

---

# Printing Text

```python
print("Python")
print("Django")
print("React")
```

Output:

```text
Python
Django
React
```

---

# Printing Numbers

```python
print(10)
print(20)
print(100)
```

Output:

```text
10
20
100
```

---

# Printing Multiple Values

```python
print("Name:", "Abhishek")
```

Output:

```text
Name: Abhishek
```

Example:

```python
print("Age:", 18)
```

Output:

```text
Age: 18
```

---

# Separator (sep)

Default separator:

```python
print("Python", "Django", "React")
```

Output:

```text
Python Django React
```

Custom separator:

```python
print("Python", "Django", "React", sep="-")
```

Output:

```text
Python-Django-React
```

Example:

```python
print(1, 2, 3, 4, sep=" | ")
```

Output:

```text
1 | 2 | 3 | 4
```

---

# End Parameter

Default:

```python
print("Hello")
print("World")
```

Output:

```text
Hello
World
```

Custom end:

```python
print("Hello", end=" ")
print("World")
```

Output:

```text
Hello World
```

Example:

```python
print("Python", end=" -> ")
print("Django")
```

Output:

```text
Python -> Django
```

---

# Escape Characters

## New Line

```python
print("Hello\nWorld")
```

Output:

```text
Hello
World
```

---

## Tab Space

```python
print("Python\tDjango")
```

Output:

```text
Python    Django
```

---

## Double Quotes

```python
print("\"Hello\"")
```

Output:

```text
"Hello"
```

---

## Backslash

```python
print("\\")
```

Output:

```text
\
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

Example:

```python
name = "Abhishek"
age = 18

print(name, age)
```

Output:

```text
Abhishek 18
```

---

# Mixing Text and Variables

```python
name = "Abhishek"

print("My name is", name)
```

Output:

```text
My name is Abhishek
```

---

# Common Mistakes

Wrong:

```python
Print("Hello")
```

Reason:

Python is case-sensitive.

Correct:

```python
print("Hello")
```

---

Wrong:

```python
print(Hello)
```

Reason:

Text ko quotes me likhna hota hai.

Correct:

```python
print("Hello")
```

---

# Summary

You Learned:

- print()
- Multiple Values
- sep
- end
- Escape Characters
- Printing Variables
- Text + Variables