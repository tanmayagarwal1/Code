"""

A FILE FOR TEST CASES 		

"""

#MAZESOLVER 
maze = [  [1, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 0, 1, 0],
          [1, 1, 1, 1] ]
mazesolver(maze)

#GOLDMAX
gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]]
        
print(goldmax(gold))

#MERGESORT 
a=[3,5,6,8,4,1,2]
mergesort(a)

#HEAPSORT 
a=[2,4,3,6,5,8,7]
heapsort(a)
print(a)

#PARANTHESIS
str="[{}]"
print(isvalid(str))

#EGGS_MAX 
print(superEggDrop(2,100))

#WATER_COLLECTOR
print(water_collector([0,1,0,2,1,0,1,3,2,1,2,1]))

#ENCODING 
ogmap='abcdefghijklmnopqrstuvwxyz'
#-----
mymap='qwertyuiopasdfghjklzxcvbnm'
print(encoding(mymap,'tanmay'))

#HOUSES 
print(Houses([20,90,40,90],100))

#BLOCKS 
arr=[{'gym':False,'school':True,'store':False},  \
	 {'gym':True,'school':False,'store':False},  \
     {'gym':True,'school':True,'store':False},   \
     {'gym':False,'school':True,'store':False},  \
     {'gym':False,'school':True,'store':True},]

interests=['gym','store']
print(Blocks(arr,interests))

#TRIPS
a=[1,2,3,4,5,6,7,8,9]
print(trips(a))

#DUPS 
a=[1,1,2,34,34,231,21]
print(dups(1))

#KADENS 
a=[123,2324,3212,32,-132,-12312,234,-213,23,232,-23,12,3123,12,-23,13,-32134324]

#TARGET SUM 
a=[123,4,3212,334,123,123,43,3,123,234]
t=46
print(target(a,t))

#UNIQUE 
print(unique('tanmay'))	

#WINDOW MAX 
'''add functions name'''([1,2,3,4,5,6,7,8,9,10,11],3)

#SUBARRAY SUM(WINDOW)
'''add functions name'''([1,2,3,4,5,6,7,8,9,10,11],3)

#STRING STARTING WITH 
print(Startingwith(['tanmay','shivika','tanuuuu'],'tan'))


#LISTS 
li.append(1)
li.append(2)
li.append(3)
li.append(4)
li.append(5)
li.append(6)
'''---------------'''
#for list palindrome

li.append(1)
li.append(0)
li.append(0)
li.append(1)

#TREES 
root=node(5)
push(root,10)
push(root,15)
push(root,6)
push(root,8)
push(root,1)


#GRAPHS for BFS and DFS 
g=graph()
g.append(0,1)
g.append(1,2)
g.append(1,3)
g.append(3,4)
g.append(1,5)
g.bfs()
print()
g.dfs()

#Graph for dijkstra 
g = graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
          [4, 0, 8, 0, 0, 0, 0, 11, 0],
          [0, 8, 0, 7, 0, 4, 0, 0, 2],
          [0, 0, 7, 0, 9, 14, 0, 0, 0],
          [0, 0, 0, 9, 0, 10, 0, 0, 0],
          [0, 0, 4, 14, 10, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 1, 6],
          [8, 11, 0, 0, 0, 0, 1, 0, 7],
          [0, 0, 2, 0, 0, 0, 6, 7, 0]
          ]







