class queue:
	def __init__(self):
		self.s1, self.s2 = [], []
	def enqueue(self, x):
		self.s1.append(x)
	def dequeue(self):
		if len(self.s1) == 0 and len(self.s2) == 0:
			return -1 
		if len(self.s2) == 0 and len(self.s1) != 0:
			while len(self.s1) != 0:
				self.s2.append(self.s1[-1])
				self.s1.pop()
			return self.s2.pop()
		else:
			return self.s2.pop()

q = queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.dequeue())
print(q.dequeue())
