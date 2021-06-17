
class sol:
	def BeautifulArrangements(self, n):
		if not n : return - 1
		arr = [i for i in range(1, n + 1)]
		self.res = 0 
		def dfs(arr, i):
			if i == n + 1:
				self.res += 1
				return 
			for j, num in enumerate(arr):
				if num % i == 0 or i % num == 0:
					dfs(arr[:j] + arr[j + 1:], i + 1)
		dfs(arr, 1)
		return self.res 

n = 3
sl = sol()
print(sl.BeautifulArrangements(3))

