crash-course-python-w2-basic-python-syntax

# Crash Course on Python
## WEEK 2 - Basic Python Syntax

### **Expression and Variables**
* * *
#### *Data Types*
Most programs need to manipulate some kind of data, and that data can come in a lot of different forums, or like we call them data types. 

If you tell your computer to mix these two different data types, your computer isn't going to know what to do and will raise an error. 

`type(<data>)` to print out the data type

#### *Variables*
Variables are names that we give to certain values in our programs. Those values can be of any data type; numbers, strings or even the results of operations. 

The process of storing a value inside a variable is called assignment. 

An expression is a combination of numbers, symbols or other variables that produce a result when evaluated. 

#### *Expressions, Numbers, and Type Conversions*
*Implicit conversion*. The interpreter automatically converts one data type into another. Such as adding integer and float.

So what if you really want to combine a string and a number, is it possible? It sure is but only with an *explicit conversion*.

<br/>

### **Functions**
* * *
#### *Defining Functions*
We're going to see how to define our own functions to tell the computer to do things that the language is built-in functions don't. 

![](https://cdn.askpython.com/wp-content/uploads/2019/06/python-functions.png)
*pictures taken from askpython.com*

#### *Returning Values*
He work that functions do can produce new results. Sure, we can print the results on the screen, but what if we wanted to use those results later in our script or didn't want to print them at all? We can do this by returning values from the functions we defined ourselves.

In python we could return multiple value and assign each of them to multiple variable

```python
def test2():
    return 'abc', 100, [0, 1, 2]

a, b, c = test2()
res = test()

print(type(res))
# <class 'tuple'>

print(a)
# abc

print(b)
# 100

print(c)
# [0, 1, 2]
```

In Python, comma-separated values are considered tuples without parentheses, 

<br/>

### **Conditionals**
* * *
#### *Comparing Things*
Python can also compare values. This lets us check whether something is smaller than, equal to, or bigger than something else. This allows us to take the result of our expressions and use them to make decisions

![](https://miro.medium.com/max/727/0*-h4Y88JjmLCvPnil.png)

*pictures taken from medium.com*

#### *Branching with if Statements*
The ability of a program to alter its execution sequence is called branching, and it's a key component in making your scripts useful. It make your program do something only when certain conditions are met.

![](https://www.simplilearn.com/ice9/free_resources_article_thumb/c-evenodd.JPG)

*pictures taken from simplilearn.com*
