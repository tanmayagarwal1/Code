# In this problem we can perfrom three operations : Insert, delete and update 
# First off we define a hash map to make sure we are not doing repeated cals 
# Next we define base cases 
# Base Case 1 : If Both strings are empty : return 0 
# Base Case 2 : If only 1 of them is reamaing return the length of the remaining string 
# Case 1 : If both the words on the current index already match just move forward by doing a [1:] on both strings 
# Now we need to stimulate the three operations : 
# 1. Insertion is stimulated by doing a [1:] on the second word : Think of it as adding to the first word - 
#    And then deleting from the second, That adding to the first is taken into count by the + 1 in the Begineeing 
# 2. Deletion is stimulate by doing a [1:] in the first word. In deletion we remove from the first and add to the second 
# 3. Replacing is simulated by doing a [1:] on the both. Now we update the cache by the miniimum of the three and also we
#	 return this cache 
def LevenshteinDistance(word1, word2):
	if len(word1) == 0 or len(word2) == 0 : raise ValueError
	return LevenshteinDistanceHelper(word1, word2, {})

def LevenshteinDistanceHelper(word1, word2, cache):
	if not word1 and not word2:
		return 0 
	if not word1 or not word2 : return len(word1) or len(word2)
	if word1[0] == word2[0]:
		return LevenshteinDistanceHelper(word1[1:], word2[1:], cache)
	if (word1, word2) not in cache:
		Insert = 1 + LevenshteinDistanceHelper(word1, word2[1:], cache)
		Delete = 1 + LevenshteinDistanceHelper(word1[1:], word2, cache)
		Replace = 1 + LevenshteinDistanceHelper(word1[1:], word2[1:], cache)
		cache[(word1, word2)] = min(Insert, Delete, Replace)
	return cache[(word1, word2)]


word1 = "horse"
word2 = 'ros'
print(LevenshteinDistance(word1, word2)) # 3