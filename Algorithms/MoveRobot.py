def MoveRobot(dirs):
	if not dirs : raise ValueError 
	x, y, dx, dy = 0, 0, 0, 1 
	for dir in dirs:
		if dir == 'G' : x, y = x + dy, y + dy 
		if dir == 'L' : dx, dy = -dy, dx 
		if dir == 'R' : dx, dy = dy, -dx
	return (x, y) == (0, 0) or (dx, dy) != (0, 1)

dirs = 'GGLLGG'
print(MoveRobot(dirs))

# If the robot ends up at the origin its true 
# If robot ends up in ay other direction it will be true ( As after a few iterations of the same string, it will form a circle )
# For left and right just swap dx, dy in any fashion as the dot proct of both of them is a zero 
# here dx = 0 and dy = 1 initially as a G means only movement on the y axis and hence we can do x = x + dx and y = y + dy 