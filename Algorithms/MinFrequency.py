'''
Find the max number of deletions to be done in a string such that the frequency of each letter is unique 
'''

def minFrequency(sti):
    n = len(sti)
    d = dict()
    for i in sti:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    count, Exists = 0, set()
    for character, frequency in d.items():
        while frequency > 0 and frequency in Exists:
            frequency -= 1
            count += 1
        Exists.add(frequency)
    return count 
print(minFrequency("hogdheejnglfmaidocafjngkf"))