# Input Function in Python

---

# What is Input Function?

Input Function ka use user se data lene ke liye kiya jata hai.

Syntax:

```python
input()
```

Example:

```python
name = input("Enter Your Name: ")

print(name)
```

Output:

```text
Enter Your Name: Abhishek
Abhishek
```

---

# How Input Works?

Program:

```python
name = input("Enter Name: ")

print(name)
```

Step 1:

```text
Enter Name:
```

Screen par show hoga.

Step 2:

User value enter karega.

Example:

```text
Abhishek
```

Step 3:

Value variable me store ho jayegi.

---

# Important Rule

Input hamesha String return karta hai.

Example:

```python
age = input("Enter Age: ")

print(type(age))
```

Input:

```text
18
```

Output:

```python
<class 'str'>
```

---

# Input with Integer

Wrong:

```python
age = input("Enter Age: ")

print(age + 10)
```

Error aayega.

---

Correct:

```python
age = int(input("Enter Age: "))

print(age + 10)
```

Input:

```text
18
```

Output:

```text
28
```

---

# Input with Float

```python
price = float(input("Enter Price: "))

print(price)
```

Input:

```text
99.99
```

Output:

```text
99.99
```

---

# Taking Name Input

```python
name = input("Enter Name: ")

print("Hello", name)
```

Output:

```text
Hello Abhishek
```

---

# Taking Multiple Inputs

Method 1

```python
name = input("Enter Name: ")
age = int(input("Enter Age: "))
```

---

Method 2

```python
a, b = input("Enter Two Numbers: ").split()
```

Input:

```text
10 20
```

Output:

```python
a = "10"
b = "20"
```

---

# Multiple Integer Input

```python
a, b = map(int, input().split())

print(a)
print(b)
```

Input:

```text
10 20
```

Output:

```text
10
20
```

---

# map() Function

Used for conversion.

Example:

```python
numbers = map(int, ["1", "2", "3"])
```

Converts:

```python
"1" -> 1
"2" -> 2
"3" -> 3
```

---

# Taking Three Numbers

```python
a, b, c = map(int, input().split())
```

Input:

```text
10 20 30
```

Output:

```text
10
20
30
```

---

# Input + Calculation

Example:

```python
a = int(input("Enter Number: "))
b = int(input("Enter Number: "))

print(a + b)
```

---

Input:

```text
10
20
```

Output:

```text
30
```

---

# Input + Area of Rectangle

```python
length = float(input("Enter Length: "))
width = float(input("Enter Width: "))

area = length * width

print(area)
```

---

# Input + Circle Area

```python
radius = float(input("Enter Radius: "))

area = 3.14 * radius * radius

print(area)
```

---

# Input + Student Data

```python
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

print(name)
print(age)
print(city)
```

---

# Common Mistakes

Wrong:

```python
age = input()

print(age + 10)
```

Reason:

Input returns string.

---

Correct:

```python
age = int(input())

print(age + 10)
```

---

Wrong:

```python
a, b = input()
```

Input:

```text
10 20
```

Error.

---

Correct:

```python
a, b = input().split()
```

---

# Real World Example

Login System

```python
username = input("Username: ")
password = input("Password: ")

print("Login Successful")
```

---

# Summary

You Learned:

- input()
- String Input
- Integer Input
- Float Input
- Multiple Inputs
- split()
- map()
- User Data Input
- Calculations Using Input