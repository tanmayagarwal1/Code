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
sti="[{}]"
print(checker(sti))



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
dups(a) # Print statement already in the fucntion 

#KADENS 
a=[123,2324,3212,32,-132,-12312,234,-213,23,232,-23,12,3123,12,-23,13,-32134324]
print(kadens(a))

#TARGET SUM 
a=[123,4,3212,334,123,123,43,3,123,234]
t=46
print(target(a,t))

#UNIQUE 
unique('tanmay') #Print statement in function 

#WINDOW MAX 
print(subarraysum([1,2,3,4,5,6,7,8,9,10,11],3))

#SUBARRAY SUM(WINDOW)
print(maxelement([1,2,3,4,5,6,7,8,9,10,11],3))

#STRING STARTING WITH 
print(StartingWith(['tanmay','shivika','tanuuuu'],'tan'))


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

root = node(20)
root.left = node(8)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)
root.right = node(22)
root.right.right = node(25)



#GRAPHS for BFS and DFS 
g=graph()
g.append(0,1)
g.append(1,2)
g.append(1,3)
g.append(3,4)
g.append(1,5)
g.bfs(0)
print()
g.dfs(0)

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

# ---------------------------------------------------------------------------------------------------------------------------------------

#REGULAR EXPRESSION 
print(regularexpression("c","a*c"))

#LCS 

print(Lcs('tanmay','shivika'))
#EGGS_MAX 
print(eggs_max(100,2))

#WATER_COLLECTOR
print(water_collector([0,1,0,2,1,0,1,3,2,1,2,1]))

# Unique Paths
print(UniquePaths(3,3))

# Unique Paths 2 

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(UniquePaths2(obstacleGrid))

# Train Tickets
days = [1,4,6,7,8,20]
costs = [2,7,15]
print(TrainTix(days, costs)) 

# Coin Change 
print(CoinChange([1,2,3,4],5))

# Minimum Cost Path 
cost= [[1, 2, 3],
       [4, 8, 2],
       [1, 5, 3]]

print(MinimumCost(cost))

# Knapsack
val = [350, 400, 450, 20, 70, 8, 5, 5]
wt  = [25, 35, 45, 5, 25 ,3, 2, 2]
w   = 104
print(Knapsack(wt, val, w))

# Knapsack - Subset sum 
arr = [2, 3, 7, 8, 10]
target = 11
print(SubsetSum(arr, target))

# Knapsack - Count Subset Sum 
arr = [1, 2, 3, 3]
target = 6 
print(totSubsets(arr, target))

# Knapsack - Equal Sum Partition
print(CanPartition([1, 2, 3, 5]))

# Unbounded Knapsack 
arr = [1, 5, 8, 9, 10, 17, 17, 20]
length = [1, 2, 3, 4, 5, 6, 7, 8]
n = 8 
print(UnboundKnapsack(length, arr, n))

# Word Break
s = "applepenapple"
wordDict = ["apple","pen"]
print(WordBreak(s, wordDict))

# ---------------------------------------------------------------------------------------------------------------------------------------
# STRINGS 

print(Unique('tanmay'))
print(Startingwith(['tanmay','shivika','tanuuuu'],'tan'))
print(License("3R-34213-3213D", 5))
print(IsPalindorme("A man, a plan, a canal: Panama"))
print(OneSwap('abc'))
print(MinSwaps('ntiin'))
arr = ["cha","r","act","ers"]
print(UniqueMax(arr))
print(FrequencySort("Aabb"))
print(minFrequency("hogdheejnglfmaidocafjngkf"))

# ---------------------------------------------------------------------------------------------------------------------------------------

# Pacific Atlantic 
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(PacificAtlantic(heights))

# Num Islands 
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(NumIslands(grid))

# Count Islands 

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(CountIslands(grid))


# Word Search 
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
print(WordSearch(board,"ABCCED"))

# Surrounding
grid = [ ["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
Surrounding(grid)

# Walls and Gates
grid = [[float('inf'), -1, 0, float('inf')], [float('inf'), float('inf'), float('inf'), -1], \
    [float('inf'), -1, float('inf'), -1], [0, -1, float('inf'), float('inf')]]
print(WallsAndGates(grid))

# Rotten Oranges
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(RottenOranges(grid))

# Mine Sweeper 

grid = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
print(MineSweeper(grid, click))


# Flood Fill 
grid = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(FloodFill(grid, sr, sc, newColor))

# Binary Matrix First One 
grid = [[0,0,0],[1,1,1],[1,1,1]]
print(MaxOnes(grid))

# Binary Matrix max one row 
grid = [[0,0,0],[1,1,1],[1,1,1]]
print(MaxOnes(grid))

# Grid Convolutions
grid = [[100,200,100],[200,50,200],[100,200,100]]
print(ImageSmoother(grid))

# Lamps Illumination
n = 5 
lamps = [[0, 0], [0, 4]]
queries = [[0,4],[0,1],[1,4]]
print(Lights(n, lamps, queries))

# Sub Islands - Grid Matching 
grid = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
gridd = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(SubIslands(grid, gridd))

# Diagonal Traversal
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(DiagonalTraversal(grid))

# Spiral Matrix

matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8],
          [9,10,11,12]]
          
print(Spiral(matrix))

# Anti Spiral Matric 
matrix = [[1, 2, 3, 4], 
          [5, 6, 7, 8],
          [9,10,11,12]]
          
print(AntiSpiral(matrix))

# -------------------------------------------------------------------------------------------------------------------------------------------

# Permutations
print(Permutations([1,2,3]))

# Combinations
print(Combination([2,3,4], 7))

# Subsets 
print(Subsets2([1,2,3]))

# Subsets with bitmask 
print(Subsets([1,2, 3]))

# Partitions 
print(Partitions(5, 3))

# Max Product Subarray 
arr = [2,3,-2,4]
print(MaxProductSubarray(arr))


# Beautiful Arrangement 
print(BeautifulArrangements(6)) # 36 

# Beautiful arrangeent 2 
print(Arrangement2(3, 2)) # [1, 3, 2]

# Two sum 
target = 14
arr = [2, 3, 4, 5, 6, 7, 8] # (4, 6)
print(TargetSum(arr, target))

# Subarray Sum equal to k 
arr = [1, 2, 3]
k = 3
print(SubarrayEqualK(arr, k)) # 2

# subarray sum divisble by k 
arr = [4,5,0,-2,-3,1]
k = 5 
print(SubarrayDivisibleK(arr, k)) # 7 

# Product Array 
arr = [1, 2, 3, 4, 5]
print(ProductArray(arr)) # [120, 60, 40, 30, 24]


# Rotate 
arr = [1,2,3,4,5,6,7]
k = 3
print(Rotate(arr, k)) # [5,6,7,1,2,3,4]

# Cook Chef 
arr = [1, 2, 3, 4]
p = 10
print(CookChef(arr, p)) # 12 

# Boats 
arr = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(Boats(arr, D)) # 15

# Painters 
arr = [15, 17, 20]
k = 2 
print(PaintersPartition(arr, k)) # 32

# Next Permutation 
arr = [1,1,5]
print(NextPermutation(arr)) # [1, 5, 1]

# Peak Element 
arr = [2, 23, 90, 67]
print(PeakElement(arr)) # 90

# Subarray Sorts the array
arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
print(SortSubarray(arr)) # (30, 35) => Nums ; (3, 8) => Indices

# Piles 
print(PilesHeight([5, 2, 1]))

# Min operations to make array strictly increasing 
arr = [1, 1, 1]
print(MinOperationsArrayIncrease(arr))  # 3

# Product Search 
arr = [2, 3, 4, 5, 6]
target = 20
print(ProductSearch(arr, target)) # (2, 3)

# Alternating Negative and Positive 
arr = [1, 2, 3, -4, -1, 4]
print(AlternatingPostiveAndNegative(arr)) # [-1, 2, -4, 4, 1, 3]

#Dutch Flag 
arr = [0, 1, 2, 1, 1, 0, 0, 2, 1, 1, 0, 1, 2, 1]
print(DutchFlag(arr))

# Floyds
arr = [1, 3, 2, 5, 4, 1, 6]
print(Floyd(arr)) # 1 

#KADENS 
a=[123,2324,3212,32,-132,-12312,234,-213,23,232,-23,12,3123,12,-23,13,-32134324]
print(kadens(a)) # (5691, 0, 3)


# -------------------------------------------------------------------------------------------------------------------------------------------

# Anagram Groups 
print(AnagramGroups(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# String Starting With 
print(StartingWith(['tanmay','shivika','tanuuuu'],'tan')) # ['tanmay', 'tanuuuu']

# License Plate 
print(License("3R-34213-3213D", 5)) # 3R-34213-3213D

# One swap palindrome 
print(OneSwap('abc')) # False 

# Min Swap Palindrome 
print(MinSwap('ntiin')) # 1 

# Unique Length Max 
arr = ["cha","r","act","ers"]  
print(UniqueLengthMax(arr)) # 6 

# Frequency Sort 
print(FrequencySort("Aabb")) # bbAa

# Max deletions
print(MaxDeletions("hogdheejnglfmaidocafjngkf")) # 39

#BLOCKS 
arr=[{'gym':False,'school':True,'store':False},  \
   {'gym':True,'school':False,'store':False},  \
     {'gym':True,'school':True,'store':False},   \
     {'gym':False,'school':True,'store':False},  \
     {'gym':False,'school':True,'store':True},]
interests=['gym','store']
print(Blocks(arr,interests)) # 2

#REGULAR EXPRESSION 
print(regularexpression("c","a*c")) # True

# LCS
print(Lcs('tanmay','shivika')) # 1 

# Lonest Palindromic Subsequence 
print(LongestPalindromicSub('agbcba')) # 5 

# Unique Substrings
print(SubStrings('abcd')) # {'a', 'c', 'b', 'abcd', 'bc', 'cd', 'bcd', 'd', 'abc', 'ab'}

# Html Parser
text = "&amp; is an HTML entity but &ambassador; is not."
text_2 = "x &gt; y &amp;&amp; x &lt; y is always false"
print(HtmlParser(text))   # & is an HTML entity but &ambassador; is not.
print(HtmlParser(text_2)) # x > y && x < y is always false

# Word Break 
s = "applepenapple"
wordDict = ["apple","pen"]
print(WordBreak(s, wordDict)) # True 

# Html Validator 
print(HtmlValidator("<head><head> This is a Html headline </head></head>")) # True

# Special Reverse
print(Specialrev('abc&^def')) # fed&^cba

# Is Rotation 
sti = 'ABCD'
other = 'CDAB'
print(IsRotatation(sti, other)) # True 

# Valid Shuffle 
First = "XY"
second = '12'
arr = ["1XY2", "Y1X2", "Y21XX"]
print(ValidShuffle(arr, First, second)) # ['1XY2', 'Y1X2']

# Longest Palindromic Substring 
sti = "babad"
print(LongestPalindromicSubstring(sti)) # bab 

# LevenshteinDistance 
word1 = "horse"
word2 = 'ros'
print(LevenshteinDistance(word1, word2)) # 3

# Minimum Adds to make balanced paranthesis 
sti = '()))(('
print(MinAddsToMakeBalanceParanthesis(sti)) # 4 

