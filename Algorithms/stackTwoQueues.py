class stack:
	def __init__(self):
		self.q = []
		self.pq = []
	def Push(self, data):
		self.q.insert(0, data)
	def pop(self):
		if not self.q and not self.pq :
			return -1 
		for i in range(len(self.q) - 1, 0, - 1):
			self.pq.insert(0, self.q[i])
			self.q.pop(i)
		x = self.q.pop()
		self.q, self.pq = self.pq, self.q 
		return x 

s = stack()
s.Push(1)
s.Push(2)
s.Push(3)
s.Push(4)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

