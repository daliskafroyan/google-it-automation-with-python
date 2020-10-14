crash-course-python-w1-hello-python

# Crash Course on Python
## WEEK 1 - Hello Python!

### **Course Introduction**
* * *
#### *Specialization Introduction*
So why take this program to learn how to code in Python? Well, first it's geared towards people who are already in or aspiring to be in the field of IT.

#### *Course Introduction*
Computer programming skills open up an incredible amount of opportunity. Being able to write scripts and programs that tell your computer to perform a task equips you with an invaluable tool. Not only does it make your work easier and more efficient,

<br/>

### **Introduction to Programming**
* * *
#### *What is Programming?*
At a basic level, a computer program is a recipe of instructions that tells your computer what to do. When you write a program, you create a step by step recipe of what needs to be done to complete a task and when your computer executes the program it reads what you wrote and follows your instructions to the letter.

In a programming language like Python, the syntax is the rules for how each instruction is written and the semantics is the effects the instructions have.

A script is a program that is short, simple, and can be written very quickly. 

#### *What is Automation?*
Automation is the process of replacing a manual step with one that happens automatically. Take a traffic light for example, which continuously regulates the flow of vehicles at an intersection. A traffic light requires a human intervention only when it needs repairs or maintenance. 

The automatic regulation of traffic means that humans don't have to stand at the intersection manually signaling when cars should stop or go. Instead, people can concentrate on more complex, creative, or difficult tasks like focusing on where you're driving. What's more, traffic lights don't get tired, bored, or accidentally display a green light when they meant red. This highlights another benefit of automation consistency.

Automation is a powerful tool when used in the right place at the right moment. It can save time, reduce errors, increase consistency, and provide a way to centralized solutions and mistakes making them easier to fix. 

<br/>

### **Introduction to Python**
* * *
#### *What is Python?*
So why pick Python? Well, we chose Python for a few reasons. First off, programming in Python usually feels similar to using a human language. This is because Python makes it easy to express what we want to do with syntax that's easy to read and write.

<br/>

### **Hello World**
* * *
#### *Hello, world!*
```python
print('hello, world!')
```
any text that isn't inside quotation mark is considered part of the code

#### *Python Can Be Your Calculator*
```python
print((((1+2)*3)/4)**5)
```
<br/>

### **Module 1 Graded Assessment**
* * *


6. Write a Python script that outputs "Automating with Python is fun!" to the screen.
```python
print("Automating with Python is fun!" )
```
7. Fill in the blanks so that the code prints "Yellow is the color of sunshine".
```python
color = "Yellow"
thing = "sunshine"
print(color + " is the color of " + thing)
```
8. Keeping in mind there are 86400 seconds per day, write a program that calculates how many seconds there are in a week, if a week is 7 days. Print the result on the screen.
```python
print(86400*7)
```
9. Use Python to calculate how many different passwords can be formed with 6 lower case English letters. For a 1 letter password, there would be 26 possibilities. For a 2 letter password, each letter is independent of the other, so there would be 26 times 26 possibilities. Using this information, print the amount of possible passwords that can be formed with 6 letters.
```python
print(26*6)
```
10. Most hard drives are divided into sectors of 512 bytes each. Our disk has a size of 16 GB. Fill in the blank to calculate how many sectors the disk has.
```python
disk_size = 16*1024*1024*1024
sector_size = 512
sector_amount = disk_size / sector_size

print(sector_amount)
```
