<a id="top"></a>
# An Introduction to Python Programming

*Preparing you to build your first web application*

Written and developed by [Matt Piccolella](mailto:matthew@adicu.com) and [ADI](adi).

Credit to [Learn X in Y Minutes: X = Python][xy] and [Learn Python the Hardway][hardway].

<a href="#top" class="top" id="getting-started">Top</a>
## Getting Started

Before we start building our first web application, we must become familiar with the Python programming language.

### What is Python?
[Python][python] is a dynamic programming language that is similar to Perl, Ruby, and Java. It is known for its clear, readable syntax, its dynamic data types, and its usage in many different types of application development.

### How will we use Python?
We will use Python to develop a web application. We will do this using the Python web microframework called [Flask][flask], which allows developers to rapidly create fast and powerful webapps.

### What will this tutorial teach me?
This introduction is meant to teach only the basics of Python. It is not meant to replace ENGI1006 or any other formal introduction to the language. It is meant only to teach the features of the language most vital to developing webapps.

## Using this Document

This document contains a series of six sections, each of which explains a concept of Python that will be valuable to us in building our web application. Each section will end with a short exercise that will ask you to write a little bit of code that ties together what was learned in the previous section. You are not required to type out and run the sample code that we provide, but it will definitely help you to learn Python much more quickly if you do.

### Running the Sample Code

All of the code in this document can be either of two ways. It can be typed in the Python shell, which can be opened by simply typing 'python' into your command line interface once you have installed the language:

``` bash
$ python
```

Or, the code can be typed into a file with the ending '.py' and run from the command line like so:

``` bash
$ python my_file.py
```

This is also the way you should write the code for the exercises. Perhaps individual files for each exercise will help you to separate your code based on the concepts it covers.

### Exercises

There are Exercises at the end of each section, that attempt to summarize the important parts of the section in a programming challenge.  Solutions are available on [Github][github].

<a href="#top" class="top" id="table-of-contents">Top</a>
## Table of Contents

-	[Preface: Comments](#comments)
-	[1.0 Data Types and Operators](#datatypes)
	-	[1.1 Math and Numbers](#math)
	-	[1.2 Booleans and Equality](#boolean)
	-	[1.3 Comparisons](#comparisons)
	-   [1.4 Strings](#strings)
	-   [1.5 Printing](#print)
	-   [1.6 Exercise 1](#exercise1)
-	[2.0 Variables and Collections](#variablescolls)
	-	[2.1 Variables](#variables)
	-   [2.2 Lists](#lists)
	-   [2.3 Tuples](#tuples)
	-   [2.4 Dictionaries](#dictionaries)
	-   [2.5 Sets](#sets)
	-   [2.6 Exercise 2](#exercise2)
-	[3.0 Control Flow](#controlflow)
	-	[3.1 If/Else](#ifelse)
	-	[3.2 For Loops](#forloop)
	-	[3.3 While Loops](#whileloop)
	-	[3.4 Try/Except](#tryexcept)
	-	[3.5 Exercise 3](#exercise3)
-	[4.0 Functions](#functions)
	-	[4.1 Defining/Calling a Function](#definecall)
	-	[4.2 Variable Arguments](#arguments)
	-	[4.3 First Class/Anonymous Functions](#firstclass)
	-	[4.4 Exercise 4](#exercise4)
-	[5.0 Classes](#classes)
	-	[5.1 Defining a Class](#defineclass)
	-	[5.2 Class Attributes](#attributes)
	-	[5.3 Initializer](#initializer)
	-	[5.4 Instance Methods](#instance)
	-	[5.5 Class Methods](#class)
	-	[5.6 Static Methods](#static)
	-	[5.7 Exercise 5](#exercise5)
-	[6.0 More Goodies](#goodies)
	- [6.1 Modules](#modules)
	- [6.2 User Input](#input)
	- [6.3 Decorator Functions](#decorator)
	- [6.4 pip/requirements.txt](#pip)
	- [6.5 Exercise 6](#exercise6)
-   [Additional Resources](#additionalresources)


------------------------------
<a href="#top" class="top" id="comments">Top</a>
## Preface: Comments
Comments are like notes a programmer takes while writing code. Comments do not affect the code, and should be used liberally to ensure code can be easily understood later both by yourself and other developers.

```python
# If you only need one line for your comment, use a hash.

""" 
If you want a comment that spans multiple lines, 
you can use triple quotes at the beginning and end.
"""
```

We will use these throughout this tutorial to make it easier to follow our code. You should do the same when writing your own code!

<a href="#top" class="top" id="datatypes">Top</a>
## 1.0 Data Types and Operators
Every programming language needs to store data and a way to work with this data. Python, like other languages, breaks these data into types and provides different ways to interact with them.

<a id="math"></a>
### 1.1 Math and Numbers
Numbers in Python are, well, numbers. They act like normal numbers. They can be added, subtracted, multiplied, and divided.

```python
3 + 5 # = 8
9 - 2 #  = 7
4 * 5 # = 20
12 / 3 # = 4
```

However, what happens if division isn't even? As in other programming languages, the result gets rounded down to the nearest whole number.

```python
11 / 4 # = 2
```

We can fix this with floating point numbers, or those with decimal points. (Ex. 12.4)

```python
11.0 / 4.0 # = 2.75
```

If you need to, order your operations using parentheses!

```python
((3 + 5) / 4) * 3 # = 6
```
<a id="boolean"></a>
### 1.2 Booleans
Booleans are used to store whether something is true or false. We represent these using two values:

```python
# Notice the capital letters!
True
False
```

We can negate these values using the word `not`:

```python
not True # False
not False # true
```

In addition, we have one more datatype, called `None`. It is similar to `null` in Java, and can be used to check whether an object contains anything. It is seen as being equal to `False`.

<a id="comparisons"></a>
### 1.3 Comparisons
Channel your pre-algebra skills; remember all the mathematical comparisons available to us. These comparisons evaluate to boolean values, and can be used the same ways booleans can be.

```python
# Greater/Less Than
2 < 3 # True
4 > 7 # False
3 >= 3 # True

# Equality uses ==
5 == 4 # False

#  Inequality uses !=
6 != 4 # True

# Don't forget about chaining!
1 < 5 < 10 # True
```

One more comparison can check the type of an object. This is with the keyword `is`. Use `is` when checking if an object is `None`.

```python
"ADI" is None # False
```

<a id="strings"></a>
### 1.4 Strings
We use strings to store text. Use either `'` or `"`, whichever you prefer.

```python
'This is my string. I like it very much.'
"This is my other string. It is even nicer than the first."

# Concatenate (add) strings
'Hello ' + ' ADI!' # 'Hello ADI!'

# Pull out individual characters by their index
'Hello'[0] # 'H'

# Format them too!
"I like to eat %s and %s" % ("peas", "carrots") # "I like to eat peas and carrots"
```
<a id="print"></a>
### 1.5 Printing
We'll probably want to be able to print things to the screen. Python gives us two easy ways to do this.

```python
print("Here is one way to print.")
print "Here is a second way."
```

<a id="exercise1"></a>
### 1.6 Exercise 1

Start with the following template code. Modify the print statements so that they print appropriately.  Use only the following: 

-   Numbers `3` and `5`
-   Math symbols `+`, `-`, `*`, `/`
-   The comparison symbol `<`
-   No string longer than 10 characters

```python
# 7
print 

# 122
print

# ADI is Awesome
print 

# True
print 
```

<a href="#top" class="top" id="variablescolls">Top</a>
## 2.0 Variables and Collections
What happens if we want to use a value more than once? Or what happens if we want to store the result of, say, a comparison or an operation? Or, even better, what if we have the results of several operations that we want to store together? For these things, we use variables and collections.

<a id="variables"></a>
### 2.1 Variables
Unlike in Java and other languages, we do not specify a type! Also, Python uses a different naming convention than Java, going for underscores instead of capital letters.

```python
my_var = 5 + 4
print my_var # 9
```
<a id="lists"></a>
### 2.2 Lists
Lists store collections of data indexed by a number, starting at 0. We can start with an empty list, or add some elements to start with:

```python
my_list = []
my_other_list = [1,5,9,6,7,8]
```

We can add and remove from the end of the list:

```python
# Add an element to the end
my_other_list.append(6) # [1,5,9,6,7,8,6]

# Remove an element from the end
my_other_list.pop() # 6
```

Access and remove elements at certain positions, or even ranges:

```python
# Access element at position 0
my_num = my_other_list[0] # 1

# Delete element at position 1
del my_other_list[1] # [1,9,6,7,8]

# Get elements between elements 1 and 3
range_1 = my_other_list[1:3] # [9,6]

# Get elements from beginning to element 3
range_2 = my_other_list[:3] # [1,9,6]

# Don't go too high though!
my_other_list[9] # IndexError - there is no element at position 9
```

Add lists together:

```python
["first", "second"] + ["third"] # ["first", "second", "third"]
```

Check if an element is within a list:

```python
4 in [1,2,5] # False
```

And get how many items are in a list:

```python
len([8,6,4,3]) # 4
```

<a id="tuples"></a>
### 2.3 Tuples
Tuples are just like lists, except they use parentheses instead of brackets. Also, they are immutable, which means you cannot change the elements in them.

```python
my_tuple = (1,2,3) # Use parentheses instead!
my_tuple[0] # 1
my_tuple[0] = 3 # Illegal! You get a TypeError
```

You can use all the same operations we saw for lists. In addition, you can unpack tubles into variables!

```python
var_1, var_2, var_3, var_4 = (1, 2, 3, 4)
print var_1 + " " + var_2 # "1 2"
```

<a id="dictionaries"></a>
### 2.4 Dictionaries
Think of a dictionary as a key and value pair. Each value has a key, which, instead of a numeric index, is a string that helps to identify a value. We can start with an empty list or a full list, and add elements at any time using a key.

```python
my_dict = {}
my_other_dict = {"first" : 10, "second": 7}
my_dict["my_key"] = "my_value" # {"my_key" : "my_value"}
```

If we want to access an element, we simply use its key:

```python
var_1 = my_other_dict["first"] # = 10
```

But using this method, if we don't find the key we pass, we will get an error! We have a solution though, the `get()` method:

```python
my_other_dict["third"] # KeyError
my_other_dict.get("third") # = None, no error!
```

If we want all the keys or all the values in a dictionary, we can get these as lists:

```python
my_other_dict.keys() # ["first", "second"]
my_other_dict.values() # [10, 7]
```

We can find the length of a dictionary (the number of keys) using the `len()` function.

```python
len(my_other_dict) # 2
```

We can again use the `in` keyword to check to see if a key exists in a dictionary:

```python
"first" in my_other_dict # True
```

<a id="sets"></a>
### 2.5 Sets
For you mathy folks, we can also represent sets, which remove duplicate elements from lists. We can declare these two ways:

```python
my_set = set([1,2,2,4,4,4,5]) # set([1,2,4,5])
# OR
my_set = {1,2,2,4,4,4,5} # {1,2,4,5}
```

Adding to a set is simple:

```python
my_set.add(6) # {1,2,4,5,6}
```

We can find the intersection and the union of two sets:

```python
my_intersection = {1,2,5} & {4,2,6} # {2}
my_union = {1,2,5} | {4,2,6} # {1,2,4,6}
```

We can find difference:

```python
my_difference = {1,2,3} - {2,4} # {1,3}
```

And find the length of a set

```python
len(my_difference) # 2
```

Or we can check if an element is in a set:

```python
1 in my_set # True
```

<a id="exercise2"></a>
### 2.6 Exercise 2

Modify the variables above the line so that all of the print statements print out `True`.

```python
a =
b =
c =
d =
e = 
f =

# Don't edit anything below this comment
# --------------------------------------

# Prints "True" if a is an int
print type(a) is int
print a < 15

# Prints "True" if b is a string
print type(b) is str
print b[5] == 'm' and b[0] == "A"

# Prints "True" if c is a list
print type(c) is list 
print len(c) == 5
print 5 in c

# Prints "True" if d is a tuple
print type(d) is tuple
print d[2] == "Python!"

# Prints "True" if e is a dictionary
print type(e) is dict
print "star" in e
print 7 in e.values()
print e.get("fish") == "chips"
print len(e) == 3
e["house"] = "cards"
print len(e) == 3

# Prints "True" if f is a set
print type(f) is set
print len(f) == 4
print len(f & {2,5,7}) == 2
```

<a href="#top" class="top" id="controlflow">Top</a>
## 3.0 Control Flow
What good is a program if we can't make decisions? Luckily, we have several tools at our disposal that allow us to make these decisions, which direct the way our program executes in such a way to make it meaningful.

<a id="ifelse"></a>
### 3.1 If/Else
We probably want the ability to do something if another condition is met. For this, we have `if`. It is here our boolean values become important:

```python
# Important: Use your tabs for whitespace! It matters!
if 4 > 3: # True
	print "Yay!" # Prints!
```

But what happens if our condition isn't true! You guessed it! `else`!

```python
if 4 != 4:
	print "This is true."
else:
	print "This is false." # Prints!
```

We can even add other conditions if our first one isn't met with `elif`. Notice this is different from the Java `else if`.

```python
if 4 == 3:
	print "First condition is true."
elif 109 > 105:
	print "Second condition is true." # Prints!
else:
	print "Third condition is true."
```

Say we have more than one condition we want to check at the same time. We have two other words, `and` and `or`. Notice that these are different than the traditional `&&` and `||`.

```python
if 4 == 4 or 8 < 4:
	print "This is true." # Prints!
if 4 == 4 and 8 < 4:
	print "This is true." # Does not print!
```

<a id="forloop"></a>
### 3.2 For Loops
If we want to iterate through all the elements in a list, a set, or a tuple, we can easily do this using a `for` loop.

```python
# Prints each element in the list
for i in ["Mom", "Dad", "Brother", "Sister"]:
	print i
```

We can also use the `range()` function combined with `for` to do some interesting things:

```python
# Range from 0 to 6
for i in range(6):
	print i # Prints 0, then 1, then 2, …, then 5
# Range from 1 to 7
for i in range(1,7):
	print i # Prints 1, then 2, then 3,…,then 6
# Range from 1 to 100, counting by three
for i in range(1,100,3):
	print i # Prints 1, then 4, then 7, …, then 97
	
```
Note: The syntax `for (x = 0; x < 10; x = x + 1)` from Java is not valid in Python.

<a id="whileloop"></a>
### 3.3 While Loops
While loops are similar to for loops, but instead execute until a condition is no longer true. We can do this with any boolean condition, but while loops are often used with mathematical comparisons.

```python
x = 0
while x < 4:
	print(x) # Prints 0, then 1, then 2, then 3
	x += 1

# Infinite Loop, must make sure inner loop changes condition
while True:
	print("This is an infinite loop.")
```

<a id="tryexcept"></a>
### 3.4 Try/Except
Sometimes you will run into errors in your code. We saw this when we tried to access an index in a list that didn't exist. For this, we can use a `try/except` clause, similar to a `try/catch` statement in Java. Let's see here:

```python
my_list = [1,2,4]
try:
	print my_list[3] # Causes IndexError
except IndexError:
	print "This is an index error!" # Executes, prevents the stopping of the program
```

This is just an example of one error that can be caught. Other common errors include `IOError`, `ValueError`, and `TypeError`. We can catch one or more using `except` statements, or catch any remaining exceptions as a default.

```python
try:
	# Some code
except IndexError:
	print "Index error!"
except IOError:
	print "IO error!"
except ValueError:
	print "Value error!"
except:
	print "Some other kind of error!"
```
This can be vital to creating robust programs that DO NOT BREAK. They should be used whenever you are doing 'risky' manipulations, such as dealing with files or user input.

<a id="exercise3"></a>
### 3.5 Exercise 3

Find a value for `a` such that all the print statements are `True`.

```python
a =

# Will your "a" variable pass my evil tests?

# Let's start off simple.  Is it the right type?
# Muhahahahaha!
if type(a) is list:
	print True
else:
	print False

# Didn't see this coming, did you?
for x in a:
	if not type(x) is int:
		print False
	else:
		print True

# And now, my evil for loop of evil testingness!
for y in range(a[3]):
	if y in a:
		print False

# Don't fall for my "Python Infinite Pit"!!!
try:
	a[5] = "Trap!"
	while True:
		print False
except IndexError:
	print True

# Rats!  Foiled again!
```

<a href="#top" class="top" id="functions">Top</a>
## 4.0 Functions
We've seen things like `len(my_list)` and `my_list.append(4)` that perform some action on a piece of data. In Python, we call these things functions.

<a id="definecall"></a>
### 4.1 Defining and Calling Functions
To define a function, we simply use the reserved word `def`.

```python
def multiply(a,b):
	return a * b
```

Notice some syntactical measures. After the name of the function, we include a colon. Also, we can specify parameters, which are pieces of data that the function takes that it can work on. In addition, we can return something from this function, in this case the product of the two parameters.

To call a function, one simply passes the parameters.

```python
var product = multiply(4,7) # = 28
```

<a id="arguments"></a>
### 4.2 Variable Arguments
Imagine that we didn't know how many parameters we want to pass. Python allows us to handle this situation using asterisks. We can pass an arbitrary number of positional arguments (list elements) using a single asterisk, or an arbitrary number of keyword arguments (dictionary elements) using a double asterisk.

```python
# Returns a list from a variable number of parameters
def positional_args(*args):
	return args

# Returns a dictionary from a variable number of parameters
def keyword_args(**kwargs):
	return kwargs
	
var my_list = positional_args(1,2,3,4) # = [1,2,3,4]
var my_dict = keyword_args(name="joe", age="17") # = {'name':'joe', 'age':'17}
```

We could also do the opposite of `*args` and `**kwargs` by attaching asterisks to our parameters to unpack them. For example:

```python
positional_args(*my_list) # = positional_args(1,2,3,4)
keyword_args(**my_dict) # = keyword_args(name="joe", age="17")
```

<a id="firstclass"></a>
### 4.3 First Class and Anonymous Functions

Interestingly, Python functions can themselves return functions. This is something JavaScript developers may be familiar with. These functions are called first-class functions.

```python
def get_multiplier_function():
	def multiplier(a,b):
		return a * b
	return multiplier

multiplier = get_multiplier_function()
product = multiplier(8,7) # = 56
```

Also, what if you had a function that you only wanted to use once, and thus you didn't want to give it a name? These functions are called anonymous functions, and Python provides us with the word `lambda` to declare these:

```python
g = lambda x: x * x
square = g(8) # = 64
```

<a id="exercise4"></a>
### 4.4 Exercise 4

Write the `square` function, which takes in a number and returns its square, and the `squarify` function which uses the `square` function to square all the numbers in a list.  All `print` statements

```python
# Write the "square" function here


# Write the "squarify" function here


# Don't edit anything below this comment
# --------------------------------------

print square(4) == 16
print square(square(3)) == 81
print squarify([3,4,9]) == [9, 16, 81]
```

<a href="#top" class="top" id="classes">Top</a>
## 5.0 Classes

You may have heard the term 'Object-Oriented Programming.' If you are unfamiliar, this basically means that things should be represented as 'objects,' each of which stores data, called fields, and associated operations, called methods. In Python and other object-oriented programming languages, we instantiate objects by defining classes.

<a id="defineclass"></a>
### 5.1 Defining a Class

To define a class in Python, we use the reserved word `class`:

```python
class Animal(object):
```

In the parentheses, we put the class from which we are subclassing. In most cases, this will be the object class.

<a id="attributes"></a>
### 5.2 Class Attributes

Each object is going to have attributes, pieces of data that are stored along with it. Some will be shared by all objects of the class. For example, all Animals belong to the same kingdom, Animalia. We call these attributes class attributes.

```python
class Animal(object):
	kingdom = "Animalia"
```
<a id="initializer"></a>
### 5.3 Initializer

However, classes will also have data that is specific to each instance of that class. For example, each Animal will have its own species or its own name. These attributes are called instance attributes, or sometimes instance variables. We handle these in what is called an initializer, which provides a way for us to create new objects.

We write an initializer like this:

```python
class Animal(object):
	kingdom = "Animalia"
	
	def __init__(self, name, species):
		self.name = name
		self.species = species
```

Notice the double underscore character before and after the word `init`. This signifies an initializer, which is known in Java as a constructor. Also notice the word `self`. The initializer always takes this as its first parameter, as it refers to the object being created.

In addition to `self`, we can pass any number of parameters, in this case the name and species.  Both `self.name` and `self.species` refer to instance attributes, which each instance of the class has.

To create a new Animal object, simply use the initializer as follows, passing each parameter in order:


```python
# Sequentially uses positioning of parameters
animal_1 = Animal("Bobo", "Monkey")

# Access attributes
animal_1.name # = "Bobo"
animal_1.species # = "Monkey"

# Change attributes
animal_1.name = "Sugar"
animal_1.name # = "Sugar"
```

<a id="instance"></a>
### 5.4 Instance Methods
Instance methods are functions defined within a class that deal specifically with the instance. They often modify or return instance attributes. They, like initializers, must take `self` as their first parameter.

```python
class Animal(object):
	# Class Attribute
	kingdom = "Animalia"
	
	# Initializer
	def __init__(self, name, species):
		self.name = name
		self.species = species
	
	# Instance Method
	def speak(self, msg):
		return "%s says %s" % (self.name, msg)

# Instantiate an Animal object
animal = Animal("Butch", "Dog")
# Call our instance method
animal.speak("woof") # = "Butch says woof"
		
```

<a id="class"></a>
###5.5 Class Methods
Class methods, like class attributes, are shared for all instances of the class. Thus, they cannot access any instance attributes or methods. They always take the `cls`, the calling class, as their first argument.

```python
class Animal(object):
    # Class Attribute
    kingdom = "Animalia"

    # Initializer
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Instance Method
    def speak(self, msg):
        return "%s says %s" % (self.name, msg)
        
    # Class Method
    @classmethod
    def get_kingdom(cls):   # "cls" refers to the class that calls get_kingdom
    	return cls.kingdom

# Instantiate an Animal object
animal = Animal("Polly", "Parrot")
# Call our class method w/ the class
Animal.get_kingdom() # = "Animalia"
```
<a id="static"></a>
### 5.6 Static Methods
Static methods, unlike class methods or instance methods, need neither a class or an instance. They are called using the class name.

```python
class Animal(object):
    # Class Attribute
    kingdom = "Animalia"

    # Initializer
    def __init__(self, name, species):
        self.name = name
        self.species = species

    # Instance Method
    def speak(self, msg):
        return "%s says %s" % (self.name, msg)

    # Class Method
    @classmethod
    def get_kingdom(cls):
        return cls.kingdom
        
    # Static Method
    @staticmethod
    def boo():
    	return "BOO!"

# Call our static method
Animal.boo() # = "BOO!"
```

<a id="exercise5"></a>
### 5.7 Exercise 5

Write a class called `Human`.  It should have a constructor that takes in a height and weight (in inches and pounds respectively), and they should be stored in instance variables.

Write an instance method called `get_bmi` that returns the BMI of the human.  Note that BMI is `weight/(height^2) * 703`.

> Having a problem with division?  If you divide two integers in Python, the result will be rounded down to the nearest integer.  Try making the numerator a decimal using the float() function before dividing.

```python
# Write the "Human" class here


# Don't edit anything below this comment
# --------------------------------------

my_human = Human(120, 67)
print "my_human's height and weight is %s and %s respectively, and it's BMI is %s." % (my_human.height, my_human.weight, my_human.get_bmi())

# Should print "my_human's height and weight is 120 and 67 respectively, and it's BMI is 3.27090277778."
```

<a href="#top" class="top" id="goodies">Top</a>
## 6.0 More Goodies
While the previous five sections provide a very thorough introduction to the basics of Python, this section will provide you with some extra information about the language. You will find many of these features to be very helpful to you when you start developing your web application and as your Python programs become more complex.

<a id="modules"></a>
### 6.1 Modules
As you start to write longer and more complex programs, you can imagine there will be lots of functions you want to be able to use. Along with that, your files will begin to get very long, to the point where you may lose control of your program. For this, we have modules.

Modules are regular Python files that contain definitions of functions that can later be imported for use in another file. Many very important functions are given to us in the Python language, all we need to do is important them! For example, Python comes with a default module called `math`, which provides many important function for mathematical operations. If we wanted to use these functions, all we have to do is import it:

```python
# your_math.py
import math

answer_1 = math.factorial(4) # 24
answer_2 = math.sqrt(4) # 2
```

If you don't want to have to say `math` everytime you use a function, you could import the specific functions you want to use:

```python
from math import pow, fabs 

answer_1 = pow(4,2) # 16
answer_2 = fabs(-5) # 5
```

You can even import all the functions from a module using an asterisk:

```python
from my_math import *
```
Though, remember that this is generally a bad idea, as you could run in to collisions with function names.

Also, we can store constants in modules! We simply access them with the dot syntax.

```python
import math

pi = math.pi #3.1415...
```

<a id="input"></a>
### 6.2 User Input
Nearly every useful program takes some kind of input from the user. Python gives us several ways to do this, the first of which is text from the command line.

We do this using the function `raw_input()`, which takes a line of text typed in by a user on the command line interface and stores it into a variable. For example:

```python
name = raw_input("What is your name? ")
```

In name will be stored whatever the user types in. Within the parentheses, you can put a prompt, which is meant to prompt the user to instruct them on what to input.

We can also take command line arguments, which are arguments input on the command line when the file is run. These arguments are stored as a [tuple](#tuples), which can then be packed or unpacked in the same way that we discussed before. For example, say we have the following Python file:

```python
# Import needed for command line arguments
from sys import argv

my_script, my_name, my_age = argv

print("Hello %s, you are %s years old." % (my_name, my_age))
print("This file is called %s." % my_script)
```

`argv` always takes at least one argument, which is the name of the script. Others can be input and handled within the program, as shown here. This program could be run by typing this in the command line:

```python
$ python my_script.py Matt 19

"""
"Hello Matt, you are 19 years old."
"This file is called my_script.py."
"""
```

We can also read from a file to get input from the user:

```python
# Get the file name from the user
file_name = raw_input("Enter a file name: ")
# Open the file for reading
file = open(file_name)
# Print the contents of the file
print file.read()
# Remember to close the file
file.close()
```

If we wanted to, we could even write to the file:

```python
file_name = raw_input("Enter a file name: ")
file = open(file_name)
file.write("Hello File!")
```

However, there is another way to read files that prevents having to close the file after you finish. It is generally preferred to use this method:

```python
# 'r' stands for 'read'
with open('my_file', 'r') as f:
	data = f.read()
```

<a id="decorator"></a>
### 6.3 Decorator Functions
As we covered previously, in Python, functions are known as first-class objects, which basically means they can be referred to be name and passed as parameters to a function. A [decorator function](http://www.brianholdefehr.com/decorators-and-functional-python), then, is a function that takes another function as a parameter and makes some kind of change to it. These changes can be small or large, but normally they can be very helpful. For example:

```python
def mod_decorator(function):
	def inner_wrapper();
		inner_wrapper.mod_count += 1
		print("I have modified this function " + inner_wrapper.mod_count + " times.")
		function()
	inner_wrapper.mod_count = 0
	return inner_wrapper
```

As we can see, we take a function, then wrap that function with the added functionality to print how many times the modified function has been called, then simply call the function we have been passed. We can then call this modified function here.

```python
def my_function():
	print "This is MY function."

decorated_function = mod_decorator(my_function)

decorated_function() 
# "I have modified this function 1 times."
# "This is MY function."

decorated_function()
# "I have modified this function 2 times."
# "This is MY function."
```

While writing it like this is perfectly legal, Python provides us some additional syntax to make this easier:

```python
@mod_decorator
def my_function():
	"My decorator has been applied automatically!"
```

While this provides a basic introduction to decorator functions, they are a hard concept to understand from a very low level. Please refer to the [following link][stackflow].
<a id="pip"></a>
### 6.4 pip/requirements.txt
When your developing a web application, there are certain packages that need to be installed to make up an environment. These packages that are needed for your project are called dependencies. We can install these dependencies easily using a built-in Python function called [`pip`][pip]. First, we would need to make a file of all our requirements called `requirements.txt`:

```python
pkg1
pkg2
pkg3
```

This file contains the names of all the packages needed for your application. For example, if we were writing a Flask application, we might need MySQL, a database program, followed by the required version number:

```bash
MySQL-python==1.2.3
```

Then, to install all of the packages in our `requirements.txt` folder, we would simply type in this command:

```bash
$ pip install -r requirements.txt
```

Then all of your required packages are installed.

But what do you put in your `requirements.txt`? A useful command to help you build these files is `pip freeze`, which can be used to print a list of installed packages in the correct format for your `requirements.txt` file. This output can then be copied and pasted into your file:

```bash
$ pip freeze
Jinja2==2.6
Pygments==1.5
Sphinx==1.1.3
docutils==0.9.1
```

A useful command in unix that can be used to copy these to your `requirements.txt` file is called a redirect. A redirect, in Unix, redirects the output of a command to another location, usually a text file. This is done using the '>' character. To redirect our requirements to our `requirements.txt` file, we simply run this command:

```bash
$ pip freeze > requirements.txt
```

Once these requirements have been copied, we can then run our `pip install` command.

<a id="exercise6"></a>
### 6.5 Exercise 6

Write a program called `sort.py` that takes in a string of numbers (like `36427478554`), and then prints the string out in the same format, but sorted.

You can sort a list by calling `.sort()` on it: 

```python
my_array = [3,1,2]
my_array.sort() # [1,2,3]``
```

Also, the `int()` and `str()` functions convert to and from strings and ints:

```python
x = 7
x_as_string = str(x)
x == int(x_as_string) # True
```

Example terminal usage:

```bash
$ python sort.py 
Enter the string of numbers: 555987654321
123455556789
```

___________

<a href="#top" class="top" id="additionalresources">Top</a>
## Additional Resources

Along with this tutorial, there is a wealth of information available on Python all across the web. Below are some good places to start:

[Learn X in Y Minutes: X=Python][xy]

[Learn Python the Hard Way][hardway]

[Official Python Documentation][pydoc]

[ADI Resources][learn]

[Codecademy][codecademy]



[github]: https://github.com/adicu/devfest-webdev
[python]: http://www.python.org
[flask]: http://flask.pocoo.org/
[pydoc]: http://docs.python.org/3/
[learn]: http://adicu.com/learn
[xy]: http://learnxinyminutes.com/docs/python/
[hardway]: http://learnpythonthehardway.org
[decorators]: http://www.brianholdefehr.com/decorators-and-functional-python
[codecademy]: http://www.codecademy.com/tracks/python
[adi]: http://adicu.com
[stackflow]: http://stackoverflow.com/questions/739654/how-can-i-make-a-chain-of-function-decorators-in-python/1594484#1594484
[pip]: http://www.pip-installer.org
