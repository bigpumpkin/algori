def longest_common_subsequence(word_a,word_b):
	cell= [[0 for i in range(len(word_a))] for j in range(len(word_b))]
	for i in range(len(word_a)):
		for j in range(len(word_b)):
			if word_a[i] == word_b[j]:
				# The letters match.
				if i > 0 and j > 0:
					cell[i][j] = cell[i-1][j-1] + 1
				else:
					cell[i][j] = 1
			else:
				# The letters don't match.
				if i == 0 and j > 0:
					cell[i][j] = cell[i][j-1]
				elif i > 0 and j == 0:
					cell[i][j] = cell[i-1][j]
				elif i == 0 and j == 0:
					cell[i][j] = 0
				else:
					cell[i][j] = max(cell[i-1][j], cell[i][j-1])

	for i in range(len(word_a)):
			print cell[i]
	print "The result is "+ str(cell[len(word_a)-1][len(word_b)-1])



a = "fish"
b = "fosh"
longest_common_subsequence(a,b)

c = "ice-cream"
d = "eee-craam"
longest_common_subsequence(c,d)
