in_file = open('input.txt', 'r')
out_file = open('output-2.txt', 'w')

result = 0
result_set = set([0]);
found = False
freq = 0

while (not found):
	for num in in_file:
		result += int(num)
		if result in result_set:
			freq = result
			found = True
			break
		else:
			result_set.add(result)

	in_file.seek(0)

out_file.write(str(freq))

in_file.close()
out_file.close()

