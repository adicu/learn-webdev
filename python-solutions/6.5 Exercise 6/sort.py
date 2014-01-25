input_string = raw_input("Enter the string of numbers: ")
num_list = []
for character in input_string:
	num_list.append(int(character))
output_string = ""
num_list.sort()
for num in num_list:
	output_string += str(num)
print output_string
