input = open('input.txt', 'r')
output = open('output-2.txt', 'w')

# Read whole file since we are going to iterate over it in nested loops.
box_ids = input.read().splitlines()

# Iterate over box ids and get the index of the current box id.
# Inner loop should go on from the next box id.
for index_1, box_id_1 in enumerate(box_ids):
	for box_id_2 in box_ids[index_1 + 1:]:

		common = ''
		diff_num = 0

		# Iterate over characters in both ids at the same time.
		for id_1, id_2 in zip(box_id_1, box_id_2):
			# If they differ, add it to the difference counter.
			if id_1 != id_2:
				diff_num += 1

				# Check if there are already too many differences.
				if diff_num > 1:
					break
			else:
				# Store common characters.
				common += id_1

		# Check if we have found our solution and break from the inner loop.
		if (diff_num == 1):
			break
	else:
		# The else part occurs if the loop ended on its own (no breaks).
		# This is so we can break out of the outer loop when a solution is found.
		# If no break occurs, the coninue gets executed and the outer loop goes on,
		# otherwise the break gets executed and the whole process ends.
		continue

	break

output.write(common)

input.close()
output.close()

