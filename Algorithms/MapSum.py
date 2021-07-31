class mapsum:
	def __init__(self):
		self.d = {}

	def insert(self, key, val):
		self.d[key] = val 

	def sum(self, prefix):
		return sum(self.d[i] for i in self.d if i.startswith(prefix))


obj = mapsum()
obj.insert("apple", 3)
print(obj.sum('app'))