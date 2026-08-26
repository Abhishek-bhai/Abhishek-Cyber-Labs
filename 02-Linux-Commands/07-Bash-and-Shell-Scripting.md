# Linux Commands Notes
## Part 7 - Bash and Shell Scripting (301-350)

---

# Section 1 - Shell Environment & Bash Commands (301-320)

---

# 301. echo
## Description
Print text or variables to the terminal.

```bash
echo "Hello, World!"
```

---

# 302. printf
## Description
Print formatted output.

```bash
printf "Name: %s\n" "Abhishek"
```

---

# 303. alias
## Description
Create a shortcut for a command.

```bash
alias ll="ls -lah"
```

---

# 304. unalias
## Description
Remove an alias.

```bash
unalias ll
```

---

# 305. alias
## Description
Display all aliases.

```bash
alias
```

---

# 306. env
## Description
Display all environment variables.

```bash
env
```

---

# 307. printenv
## Description
Display environment variables.

```bash
printenv
```

---

# 308. export
## Description
Create an environment variable.

```bash
export NAME="Abhishek"
```

---

# 309. unset
## Description
Remove a shell variable.

```bash
unset NAME
```

---

# 310. source
## Description
Execute commands from a file in the current shell.

```bash
source ~/.bashrc
```

---

# 311. .
## Description
Another way to execute a script in the current shell.

```bash
. ~/.bashrc
```

---

# 312. history
## Description
Display command history.

```bash
history
```

---

# 313. history -c
## Description
Clear command history.

```bash
history -c
```

---

# 314. !!
## Description
Run the previous command again.

```bash
!!
```

---

# 315. !n
## Description
Run command number n from history.

```bash
!50
```

---

# 316. type
## Description
Display how a command is interpreted.

```bash
type ls
```

---

# 317. command -v
## Description
Show the path of a command.

```bash
command -v python3
```

---

# 318. builtin
## Description
Run a Bash built-in command.

```bash
builtin pwd
```

---

# 319. exec
## Description
Replace the current shell with another program.

```bash
exec bash
```

---

# 320. exit
## Description
Exit the current shell.

```bash
exit
```

---

# Section 2 - Pipes and Redirection (321-335)

---

# 321. >
## Description
Redirect output to a file.

```bash
echo "Hello" > file.txt
```

---

# 322. >>
## Description
Append output to a file.

```bash
echo "World" >> file.txt
```

---

# 323. <
## Description
Redirect input from a file.

```bash
sort < file.txt
```

---

# 324. 2>
## Description
Redirect standard error.

```bash
ls invalid 2> error.log
```

---

# 325. &>
## Description
Redirect standard output and error.

```bash
command &> output.log
```

---

# 326. |
## Description
Pipe output from one command to another.

```bash
ls -l | less
```

---

# 327. tee
## Description
Display output and save it to a file.

```bash
ls | tee files.txt
```

---

# 328. xargs
## Description
Build and execute commands from standard input.

```bash
find . -name "*.txt" | xargs rm
```

---

# 329. yes
## Description
Repeatedly output a string.

```bash
yes
```

---

# 330. paste
## Description
Merge lines from multiple files.

```bash
paste file1 file2
```

---

# 331. split
## Description
Split a file into smaller parts.

```bash
split -b 10M file.iso part_
```

---

# 332. join
## Description
Join lines from two sorted files.

```bash
join file1 file2
```

---

# 333. comm
## Description
Compare two sorted files.

```bash
comm file1 file2
```

---

# 334. sponge
## Description
Safely overwrite a file with piped output.

```bash
cat file.txt | sponge file.txt
```

---

# 335. script
## Description
Record a terminal session.

```bash
script session.log
```

---

# Section 3 - Bash Scripting Syntax (336-350)

---

# 336. Variable

## Description
Create a shell variable.

```bash
name="Abhishek"
echo "$name"
```

---

# 337. Command Substitution

## Description
Store command output in a variable.

```bash
today=$(date)
echo "$today"
```

---

# 338. if Statement

## Description
Execute code if a condition is true.

```bash
if [ "$a" -eq "$b" ]; then
    echo "Equal"
fi
```

---

# 339. if...else Statement

## Description
Execute different code based on a condition.

```bash
if [ "$a" -gt "$b" ]; then
    echo "Greater"
else
    echo "Smaller"
fi
```

---

# 340. for Loop

## Description
Repeat commands over a list.

```bash
for i in 1 2 3
do
    echo "$i"
done
```

---

# 341. while Loop

## Description
Repeat while a condition is true.

```bash
count=1

while [ "$count" -le 5 ]
do
    echo "$count"
    ((count++))
done
```

---

# 342. until Loop

## Description
Repeat until a condition becomes true.

```bash
count=1

until [ "$count" -gt 5 ]
do
    echo "$count"
    ((count++))
done
```

---

# 343. case Statement

## Description
Execute code based on pattern matching.

```bash
case "$choice" in
1) echo "One" ;;
2) echo "Two" ;;
*) echo "Invalid" ;;
esac
```

---

# 344. Function

## Description
Create a reusable block of code.

```bash
greet() {
    echo "Hello"
}

greet
```

---

# 345. read

## Description
Take input from the user.

```bash
read -p "Enter your name: " name
```

---

# 346. test

## Description
Evaluate conditions.

```bash
test -f file.txt
```

---

# 347. [

## Description
Alternative syntax for test.

```bash
[ -d Documents ]
```

---

# 348. [[ ]]

## Description
Advanced conditional expression.

```bash
[[ "$name" == "Abhishek" ]]
```

---

# 349. (( ))

## Description
Perform arithmetic operations.

```bash
((a=10+20))
echo "$a"
```

---

# 350. select

## Description
Create a simple menu in Bash.

```bash
select option in Start Exit
do
    echo "$option"
    break
done
```

---
