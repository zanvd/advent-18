input = open('input.txt', 'r')
output = open('output-1.txt', 'w')

twice = 0
thrice = 0

for box_id in input:
	twice_found = thrice_found = False

	# Get unique letters in a box id.
	letters = list(set(box_id))

	for letter in letters:
		# Count occurances of a letter in a box id.
		occurance_num = box_id.count(letter)

		# If a letter appears twice or thrice in a box id, count it,
		# but only once per box id.
		if not twice_found and occurance_num == 2:
			twice += 1
			twice_found = True
		elif not thrice_found and occurance_num == 3:
			thrice += 1
			thrice_found = True

		# Just break from the loop if both are found since any other occurances won't count.
		if twice_found and thrice_found:
			break

output.write(str(twice * thrice))

input.close()
output.close()

