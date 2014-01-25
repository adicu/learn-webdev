# Write the "square" function here
def square(x):
	return x * x

# Write the "squarify" function here
def squarify(l):
	for index in range(len(l)):
		l[index] = square(l[index])
	return l

# Don't edit anything below this comment
# --------------------------------------

print square(4) == 16
print square(square(3)) == 81
print squarify([3,4,9]) == [9, 16, 81]