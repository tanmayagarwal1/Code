from potential import potential
from robot import robot
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


gX = int(input("Enter X coordinate of the goal:"))
gY = int(input("Enter Y coordinate of the goal:"))

X = int(input("Enter X coordinate of the initial position: "))
Y = int(input("Enter Y coordinate of the initial position: "))
 
rO = int(input(20))
rG = 0.2

sO = 10

a = 0.001
b = 0.03

xPlot = []
yPlot = []

xPlot.append(X)
yPlot.append(Y)

max_iter = 10000
iter_ = 0

f = 0
   
def Drone():
	if f <= 90:
		oX.append(int(Y + int("left_obst_dist")))
		oY.append(int(X))
	if f <= 90:
		oX.append(int(Y - int("left_obst_dist")))
		oY.append(int(X))
	if f <= 90:
		oX.append(int(Y))
		oY.append(int(X + int("front_obst_dist")))
	if f <= 90:
		oX.append(int(Y))
		oY.append(int(X - int("front_obst_dist")))        
	pot_env = potential(gX, gY, oX, oY)
	rob = robot(X, Y)
	curX, curY = rob.getCurrentLocation()
	distG, theG = pot_env.getParamsFromGoal(curX, curY)
	
	return oX, oY, pot_env, rob, curX, distG, theG
 

		 
		
while True:
	oX, oY, pot_env, rob, curX, distG, theG = Drone()
	while distG > rG and iter_ <= max_iter:
		iter_ += 1
		delX = a*(distG - rG)*(math.cos(theG))
		delY = a*(distG - rG)*(math.sin(theG))
		distO, theO = pot_env.getParamsFromObstacles(curX, curY)
		if (distO[0] != -1):
			for i, j in zip(distO, theO):
				# print "Distance from obstacle: " + str(i)
				if (i < rO):
					delX = delX - 2.5 * (math.cos(j))
					delY = delY - 2.5 * (math.sin(j))
				elif (i < sO + rO):
					delX = delX - b * (sO + rO - i) * (math.cos(j))
					delY = delY - b * (sO + rO - i) * (math.sin(j))

		# print delX, delY
		# print "Distance from Goal: " + str(distG)
		# print "Curr coordinates: " + str(rob.getCurrentLocation())
		rob.updateLocation(delX, delY)
		
		curX, curY = rob.getCurrentLocation()
		xPlot.append(curX)
		yPlot.append(curY)

		distG, theG = pot_env.getParamsFromGoal(curX, curY)

	ax = plt.axes()
	for i in range(n):
		ax.add_patch(patches.Circle((oX[i], oY[i]), rO, hatch = '/', fill = False))

	plt.plot(xPlot, yPlot)
	plt.show()
   

		
		
		
 



























	   

