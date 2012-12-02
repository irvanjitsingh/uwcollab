import string
 
def compareItems((w1,c1), (w2,c2)):
	if c1 > c2:
		return - 1
	elif c1 == c2:
		return cmp(w1, w2)
	else:
		return 1
 
def analyze(text, num):
	# get the sequence of words from input
	for ch in """!"#$%&()*+,-./:;<=>?@[\\]?_'`{|}?""":
		text = string.replace(text, ch,' ') 
		words = string.split(text)

# construct a dictionary of word counts
	counts = {}
	for w in words:
		try:
			counts[w] = counts[w] + 1
		except KeyError:
			counts[w] = 1

	# output analysis of n most frequent words.
	items = counts.items()
	items.sort(compareItems)
	result = []
	for i in range(num):
		result.append(" '  %-10s' appears %5d time(s)" % items[i])
	return result
 