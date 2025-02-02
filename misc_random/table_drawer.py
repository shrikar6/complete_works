def zigzag():
	table = open("table.txt", 'w')
	table_list = []
	counter1 = 0
	counter2 = -1
	tiles = 0
	skip = False

	for i in range(6, 10):
		for j in range(9):
			space = ' '*(2*(9-i))
			str1 = space + '+---'*i + '+\n'
			table_list.append(str1)

			str2_list = [space]
			str2_list.extend(['|   ']*i)
			str2_list.append('|\n')

			if not skip:
				tiles += 2
				if counter1 >= 0:
					str2_list[1 + counter1] = '||||'
					str2_list[-1 + counter2] = '||||'

					if 1 + counter1 == i - 1 + counter2:
						tiles -= 1
					elif 2 + counter1 == i - 1 + counter2:
						counter1 += 1
						counter2 -= 1

					counter1 += 1
					counter2 -= 1

					if counter1 == i:
						counter1 = -2
						counter2 = 1

				else:
					str2_list[-1 + counter1] = '||||'
					str2_list[1 + counter2] = '||||'

					if 1 + counter2 == i - 1 + counter1:
						tiles -= 1
					elif 2 + counter2 == i - 1 + counter1:
						counter1 -= 1
						counter2 += 1

					counter1 -= 1
					counter2 += 1

					if counter1 == -i-1:
						counter1 = 1
						counter2 = -2

			table_list.append("".join(str2_list))
			skip = not skip


	table.write('+---'*9 + '+\n')

	for i in table_list[::-1]:
		table.write(i)

	table.close()

	print(tiles)

def nth_col(n):
	if n < 1:
		return
	table = open("table.txt", 'w')
	table_list = []
	skip = False

	for i in range(6, 10):
		for j in range(9):
			space = ' '*(2*(9-i))
			str1 = space + '+---'*i + '+\n'
			table_list.append(str1)

			str2_list = [space]
			str2_list.extend(['|   ']*i)
			str2_list.append('|\n')

			if not skip:
				for k in range(n, i+1, n):
					str2_list[k] = '||||'

			table_list.append("".join(str2_list))
			skip = not skip


	table.write('+---'*9 + '+\n')

	for i in table_list[::-1]:
		table.write(i)

	table.close()

def nth_tile(n):
	if n < 1:
		return
	table = open("table.txt", 'w')
	table_list = []
	# skip = False
	tile = 0

	for i in range(6, 10):
		for j in range(9):
			space = ' '*(2*(9-i))
			str1 = space + '+---'*i + '+\n'
			table_list.append(str1)

			str2_list = [space]
			str2_list.extend(['|   ']*i)
			str2_list.append('|\n')

			# if not skip:
			while tile < i:
				str2_list[1+tile] = '||||'
				tile += n
			tile %= i

			table_list.append("".join(str2_list))
			# skip = not skip


	table.write('+---'*9 + '+\n')

	for i in table_list[::-1]:
		table.write(i)

	table.close()

if __name__ == '__main__':
	nth_tile(10)