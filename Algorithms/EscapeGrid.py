def Escape(ghosts, target):
	if not target : raise ValueError 
	if not ghosts : return True 
	x, y = target 
	d = abs(x) + abs(y)
	return True if all(d < abs(x - a) + abs(y - b) for a, b in ghosts) else False 

ghosts = [[1,0],[0,3]]
target = [0,1]
print(Escape(ghosts, target))