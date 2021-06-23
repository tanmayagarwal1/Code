def IsRotatation(sti, other):
    if len(sti) == 0 or len(other) == 0 or len(sti) != len(other):
        raise ValueError
    tmp = sti + sti  
    return True if tmp.count(other) else False # Count returns number of time one string occurs in another 

sti = 'ABCD'
other = 'CDAB'
print(IsRotatation(sti, other)) # True 