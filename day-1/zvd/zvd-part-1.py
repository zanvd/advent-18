in_file = open('input.txt', 'r')
out_file = open('output-1.txt', 'w')

result = 0

for num in in_file:
	result += int(num)

out_file.write(str(result))

in_file.close()
out_file.close()

