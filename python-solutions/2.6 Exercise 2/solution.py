a = 11
b = "Awesome"
c = [2, 3, 5, 7, 4]
d = ("Ready", "Set", "Python!")
e = {"star": 7, "fish": "chips", "house": True}
f = {1, 3, 5, 7}

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