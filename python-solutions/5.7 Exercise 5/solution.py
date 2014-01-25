# Write the "Human" class here

class Human(object):

	def __init__(self, height, weight):
		self.height = height
		self.weight = weight

	def get_bmi(self):
		return float(self.weight) / (self.height * self.height) * 703

# Don't edit anything below this comment
# --------------------------------------

my_human = Human(120, 67)
print "my_human's height and weight is %s and %s respectively, and it's BMI is %s." % (my_human.height, my_human.weight, my_human.get_bmi())

# Should print "my_human's height and weight is 120 and 67 respectively, and it's BMI is 3.27090277778."
