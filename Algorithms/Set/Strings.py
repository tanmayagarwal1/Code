def Unique(sti):
	if len(sti) == 0:
		return - 1
	s, q = set(), []
	for char in sti:
		if char not in s:
			s.add(char)
		else:
			q.append(char)
	for char in sti:
		if char not in q:
			print(char)

def RemoveDups(sti):
	if len(sti) == 0 : return -1 
	s, q = set(), []
	for char in sti:
		if char not in s:
			s.add(char)
			q.append(char)
		else:
			continue 
	return ''.join(q)

def StartingWith(arr, pattern):
	if len(arr) == 0 :
		return -1 
	q = []
	for word in arr:
		count = 0 
		for i in range(len(pattern)):
			if word[i] == pattern[i]:
				count += 1
			else:
				break 
			if count == len(pattern):
				q.append(word)
	return q 

def License(sti):
	if not sti : return - 1
	sti = ''.join(sti.split('-')).upper()
	i, j, res = 0, len(sti), []
	while j > i :
		if sti[j - k:j] : res.append(sti[j - k : j])
		else: res.append(sti[j - k :j])
		j -= k
	return ''.join(res[::-1])

def IsValid(sti):
	if len(sti) == 0 : return - 1
	sti = ''.join(sti.split(' ')).lower()
	q = []
	for char in sti:
		if char.isalnum():
			q.append(char)
	return q==q[::-1]

def OneSwap(sti):
	if len(sti) == 0 :
		return - 1
	i, j = 0, len(sti) - 1
	while j > i:
		if sti[i] == sti[j]:
			i += 1
			j -= 1
		else:
			one, two = sti[i : j], sti[i + 1, j + 1]
			return one == one[::-1] or two == two[::-1]
	return True 

def MinSwap(sti):
	if len(sti) == 0 :
		return - 1
	if not IsValid(sti):
		return -1 
	i, j = 0, len(sti) - 1
	sti, swaps = [i for i in sti], 0
	while j > i :
		if sti[i] == sti[j]:
			i += 1
			j -= 1
		else:
			temp = j 
			while j >= i and sti[temp] != sti[i]:
				temp -= 1
			if i == temp:
				sti[temp], sti[temp + 1] = sti[temp + 1], sti[temp]
				swaps += 1
				continue 
			for x in range(temp, j):
				sti[x], sti[x + 1] = sti[x + 1], sti[x]
				swaps += 1
			i += 1
			j -= 1
	return swaps 

def IsValid(sti):
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	return len([i for i, j in d.items() if j & 1]) <= 1

def UNiqueLengthMax(arr):
	if len(arr) == 0 :
		return - 1
	sol, res = [''], 0
	for word in arr:
		for string in sol:
			temp = word + string
			if len(temp) == len(set(temp)):
				sol.append(temp)
				res = max(res, len(temp))
	return res 

def FrequencySort(sti):
	if len(sti) == 0 :
		return -1 
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	q = [i for i in d.values()]
	q, sol = sorted(q, reverse = True), ''
	for freq in q:
		for char, freqq in d.items():
			if freq == freqq:
				sol += char*freq
		del d[char]
	return sol 

def anagrapgroups(arr):
	if len(arr) == 0 :
		return - 1
	d = dict()
	for word in arr:
		tmp = ''.join(sorted(word))
		if tmp in d.keys():
			d[tmp].append(word)
		else:
			d[tmp] = [word]
	return [i for i in d.values()]

def Blocks(arr, pattern):
	if len(arr) == 0 :
		return - 1
	q = []
	for block in arr:
		count = 0 
		for place, IsPresent in block.items():
			for z in range(len(pattern)):
				if place[z] == pattern[z] and IsPresent == True:
					count +=1
		q.append(count)
	res = q[0]
	for i in range(len(q)):
		res = max(res, q[i])
	return res 

def HtmlParser(sti):
	if len(sti) == 0 :
		return - 1
	d = {}
	Keywrords, Outputs, Mode = [], [], False 
	for char in sti:
		if char == '&':
			Keywrords.append(char)
			Mode = True 
		elif Mode:
			Keywrords.append(char)
			if char == ';':
				Keywrord = ''.join(Keywrords)
				Outputs.append(d.get(Keywrord, Keywrord))
				Mode = False 
				Keywrords = []
		else:
			Outputs.append(char)
	if Mode:
		Outputs.append(Keywrords)
	return ''.join(Outputs)

def HtmlTagValidator(sti):
	if len(sti)  == 0 : return - 1
	Open, Close, br = [], [], ['<', '>', '/']
	for i in range(len(sti)):
		if sti[i] == br[0] and sti[i + 1] != br[2]:
			while sti[i] != br[1]:
				Open.append(sti[i])
				i += 1
		elif sti[i] == br[0] and sti[i + 1] == br[2]:
			while sti[i] != br[1]:
				if sti[i] == br[2]:
					i += 1
				Close.append(sti[i])
				i += 1
		else:
			i += 1
	return sorted(Open) == sorted(Close)

def MaxDeletion(sti):
	if len(sti) == 0 :
		return - 1
	d = dict()
	for char in sti:
		d[char] = d.get(char, 0) + 1
	s, swaps = set(), 0
	for i in d.values():
		while i >= 0 and i in s:
			i -= 1
			swaps += 1
		s.add(i)
	return swaps 

def KeyBasedSort(arr):
	if len(arr) == 0 : return -1 
	arr.sort(key = lambda x : (x.split(' ')[1], x.split(' ')[0]))
	return arr 

def JunctionBoxes(arr):
	if len(arr) == 0 :
		return - 1
	new, old = [], []
	for sti in arr:
		Mode = sti.split(' ')[1]
		if Mode.isalpha():
			old.append(sti)
		else:
			new.append(sti)
	old.sort(key = lambda x : (x.split(' ')[1:], x.split(' ')[0]))
	old.extend(new)
	return old 

