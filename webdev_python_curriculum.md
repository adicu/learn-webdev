<a id="top"></a>
# An Introduction to Python Programming

*Preparing you to build your first web application*

Written and developed by [Matt Piccolella](mailto:matthew@adicu.com) and [ADI](http://adicu.com).

Credit to [Learn X in Y Minutes: X = Python](#xy) and [Learn Python the Hardway](#hardway).

------

<a id="getting-started"></a>
## Getting Started

Before we start building our first web application, we must become familiar with the Python programming language.

### What is Python?
[Python](#python) is a dynamic programming language that is similar to Perl, Ruby, and Java. It is known for its clear, readable syntax, its dynamic data types, and its usage in many different types of application development.

### How will we use Python?
We will use Python to develop a web application. We will do this using the Python web microframework called [Flask](#flask), which allows developers to rapidly create fast and powerful webapps.

### What will this tutorial teach me?
This introduction is meant to teach only the basics of Python. It is not meant to replace ENGI1006 or any other formal introduction to the language. It is meant only to teach the features of the language most vital to developing webapps.

-------------
## Using this Document

This document contains a series of six sections, each of which explains a concept of Python that will be valuable to us in building our web application. Each section will end with a short exercise that will ask you to write a little bit of code that ties together what was learned in the previous section. You are not required to type out and run the sample code that we provide, but it will definitely help you to learn Python much more quickly if you do.

### Running the Sample Code

All of the code in this document can be either of two ways. It can be typed in the Python shell, which can be opened by simply typing 'python' into your command line interface once you have installed the language:

```
$ python
```

Or, the code can be typed into a file with the ending '.py' and run from the command line like so:

```
$ python my_file.py
```

This is also the way you should write the code for the exercises. Perhaps individual files for each exercise will help you to separate your code based on the concepts it covers.

------------------
<a id="table-of-contents"></a>
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
	- [6.3 pip/requirements.txt](#pip)


------------------------------
<a id="comments"></a>
# Preface: Comments
Comments are like notes a programmer takes while writing code. Comments do not affect the code, and should be used liberally to ensure code can be easily understood later both by yourself and other developers.

```python
# If you only need one line for your comment, use a hash.

""" 
If you want a comment that spans multiple lines, 
you can use triple quotes at the beginning and end.
"""
```

We will use these throughout this tutorial to make it easier to follow our code. You should do the same when writing your own code!
<a id="datatypes"></a>
# 1.0 Data Types and Operators
Every programming language needs to store data and a way to work with this data. Python, like other languages, breaks these data into types and provides different ways to interact with them.

<a id="math"></a>
## 1.1 Math and Numbers
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
## 1.2 Booleans
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
## 1.3 Comparisons
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
## 1.4 Strings
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
## 1.5 Printing
We'll probably want to be able to print things to the screen. Python gives us two easy ways to do this.

```python
print("Here is one way to print.")
print "Here is a second way."
```

<a id="exercise1"></a>
## 1.6 Exercise 1

-------
<a id="variablescolls"></a>
#2.0 Variables and Collections
What happens if we want to use a value more than once? Or what happens if we want to store the result of, say, a comparison or an operation? Or, even better, what if we have the results of several operations that we want to store together? For these things, we use variables and collections.

<a id="variables"></a>
## 2.1 Variables
Unlike in Java and other languages, we do not specify a type! Also, Python uses a different naming convention than Java, going for underscores instead of capital letters.

```python
my_var = 5 + 4
print my_var # 9
```
<a id="lists"></a>
## 2.2 Lists
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
my_other_list.pop() # [1,5,9,6,7,8]

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
## 2.3 Tuples
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
## 2.4 Dictionaries
Think of a dictionary as a key and value pair. Each value has a key, which, instead of a numeric index, is a string that helps to identify a value. We can start with an empty list or a full list, and add elements at any time using a key.

```python
my_dict = {}
my_other_dict = {"first" : 10, "second", 7}
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

We can again use the `in` keyword to check to see if a key exists in a dictionary:

```python
"first" in my_other_dict # True
```

<a id="sets"></a>
## 2.5 Sets
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

Or we can check if an element is in a set:

```python
1 in my_set # True
```

<a id="exercise2"></a>
## 2.6 Exercise 2
--------

<a id="controlflow"></a>
# 3.0 Control Flow
What good is a program if we can't make decisions? Luckily, we have several tools are our disposal that allow us to make these decisions, which direct the way our program executes in such a way to make it meaningful.

<a id="ifelse"></a>
## 3.1 If/Else
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
## 3.2 For Loops
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
## 3.3 While Loops
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
## 3.4 Try/Except
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
## 3.5 Exercise 3
---------------
<a id="functions"></a>
# 4.0 Functions
We've seen things like `len(my_list)` and `my_list.append(4)` that perform some action on a piece of data. In Python, we call these things functions.
<a id="definecall"></a>
## 4.1 Defining and Calling Functions
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
## 4.2 Variable Arguments
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

## 4.3 First Class and Anonymous Functions

Interestingly, Python functions can themselves return functions. This is something JavaScript developers may be familiar with. These functions are called first-class functions.

```python
def get_multiplier_function():
	def multipler(a,b):
		return a * b
	return multiplier

multiplier = get_multiplier_function()
product = multiplier(8,7) # = 56
```

Also, what if you had a function that you only wanted to use once, and thus you didn't want to give it a name? These functions are called anonymous functions, and Python provides us with the word `lambda` to declare these:

```python
g = lambda x: return x * x
square = g(8) # = 64
```

<a id="exercise4"></a>
## 4.4 Exercise 4
---------
<a id="classes"></a>
# 5.0 Classes

You may have heard the term 'Object-Oriented Programming.' If you are unfamiliar, this basically means that things should be represented as 'objects,' each of which stores data, called fields, and associated operations, called methods. In Python and other object-oriented programming languages, we instantiate objects by defining classes.

<a id="defineclass"></a>

## 5.1 Defining a Class

To define a class in Python, we use the reserved word `class`:

```python
class Animal(object):
```

In the parentheses, we put the class from which we are subclassing. In most cases, this will be the object class.

<a id="attributes"></a>
## 5.2 Class Attributes

Each object is going to have attributes, pieces of data that are stored along with it. Some will be shared by all objects of the class. For example, all Animals belong to the same kingdom, Animalia. We call these attributes class attributes.

```python
class Animal(object):
	kingdom = "Animalia"
```
<a id="initializer"></a>

## 5.3 Initializer

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
## 5.4 Instance Methods
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
##5.5 Class Methods
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
    def get_kingdom(cls):
    	return cls.kingdom

# Instantiate an Animal object
animal = Animal("Polly", "Parrot")
# Call our class method
animal.get_kingdom() # = "Animalia"

```
<a id="static"></a>
## 5.6 Static Methods
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
    def get_kingdom(cls):
        return cls.kingdom
        
    # Static Method
    def boo():
    	return "BOO!"

# Call our static method
Animal.boo() # = "BOO!"

```

<a id="exercise5"></a>
## 5.7 Exercise 5
_______________
<a id="goodies"></a>
# 6.0 More Goodies


[python]: http://www.python.org
[flask]: http://flask.pocoo.org/
[learn]: http://adicu.com/learn
[xy]: http://learnxinyminutes.com/docs/python/
[hardway]: http://learnpythonthehardway.org

