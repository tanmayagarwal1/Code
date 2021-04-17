import csv 
from collections import Counter 
c=Counter()
typpe=[]
country=[]
m_count=0
show_count=0
with open(r'/Users/tanmay/Downloads/netflix_titles.csv','r') as fi:
    file_reader= csv.reader(fi)
    count=0
    next(file_reader)
    for line in file_reader:
        if count<1000:
            typpe.append(line[1])
            country.append(line[5])
            count+=1
for i in country:
    c.update([i])
print(c.most_common(10))