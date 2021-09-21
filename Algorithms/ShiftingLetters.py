def ShiftingLetters(sti, arr):
    if not arr or not sti : raise ValueError 
    for i in range(len(arr) - 2, -1, -1):
        arr[i] += arr[i + 1]
    res = ""
    for i in range(len(sti)):
        char = chr(((ord(sti[i]) + arr[i] - ord("a")) % 26) + ord("a"))
        res += char 
    return res 


sti = "abc"
arr = [3, 5, 9]
print(ShiftingLetters(sti, arr))