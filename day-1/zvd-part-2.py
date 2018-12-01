input = open('i-z.txt', 'r')
output = open('o-z-2.txt', 'w')

result = 0
result_set = set([0]);
found = False
freq = 0

while (not found):
	for num in input:
		result += int(num)
		if result in result_set:
			freq = result
			found = True
			break
		else:
			result_set.add(result)

	input.seek(0)

output.write(str(freq))

input.close()
output.close()

