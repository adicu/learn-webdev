a = [3,4,5,2]

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