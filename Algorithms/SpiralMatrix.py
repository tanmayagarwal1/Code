def Spiral(matrix):
	m=len(matrix)
	n=len(matrix[0])
	if m==0 or n==0:
		return -1 
	Top, Right, Left, Bottom = 0, n-1, 0, m-1
	arr=[]
	max_size = m*n 
	while len(arr)<max_size:
		for i in range(Left,Right+1):  
			if len(arr)<max_size:
				arr.append(matrix[Top][i])
		Top += 1 

		for i in range(Top,Bottom+1):
			if len(arr)<max_size:
				arr.append(matrix[i][Right])
		Right-=1

		for i in range(Right,Left-1,-1):
			if len(arr)<max_size:
				arr.append(matrix[Bottom][i])
		Bottom-=1

		for i in range(Bottom,Top-1,-1):
			if len(arr)<max_size:
				arr.append(matrix[i][Left])
		Left +=1
	return arr 



matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8],
          [9,10,11,12]]
          
print(Spiral(matrix))



