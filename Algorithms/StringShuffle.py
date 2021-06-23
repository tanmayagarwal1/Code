# Input = Two words and an array of various words. We need to find out if the words in the array can be made by combining 
# The given two words. Simple Implementation using sorted and can be scaled to any number of input words 
def ValidShuffle(words, first, second):
    if len(words) == 0 : raise ValueError
    tmp = first + second 
    return [word for word in words if sorted(tmp) == sorted(word)]

First = "XY"
second = '12'
arr = ["1XY2", "Y1X2", "Y21XX"]
print(ValidShuffle(arr, First, second))
