input = open('input.txt', 'r')
output = open('output-1.txt', 'w')

result = 0

for num in input:
	result += int(num)

output.write(str(result))

input.close()
output.close()

