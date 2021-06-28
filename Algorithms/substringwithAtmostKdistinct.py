def LongestSubstringwithAtmostKDistinct(sti, k ):
	if len(sti) == 0 : raise ValueError 
	def Helper(sti,  k ):
		l, r, count, res = 0, 0, 0, 0
		d = dict()
		while r < len(sti):
			d[sti[r]] = d.get(sti[r], 0) + 1
			if d[sti[r]] == 1 : count += 1
			r += 1
			while l < r and count >  k :
				d[sti[l]] -= 1
				if d[sti[l]] == 0 : count -= 1
			res = max(res, r - l) # If we want total count then res += r - l else if we want the longest/ shortest => max/min(res, l - 1)
		return res 
	
	return Helper(sti, k)

sti = "abcabcbb"
print(LongestSubstringwithAtmostKDistinct(sti, 2))