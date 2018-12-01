input = open('i-z.txt', 'r')
output = open('o-z-1.txt', 'w')

result = 0

for num in input:
	result += int(num)

output.write(str(result))

input.close()
output.close()

