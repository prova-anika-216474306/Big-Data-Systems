import itertools as it
from venv import create
import time

start_time = time.time()
#parsing thr Netflix dataset and storing into data array
data = []

with open("netflix.data", "r") as f:
    next(f)
    for line in f:
        arr = []
        l = line.split(" ")
        for item in l:
            if (item != '\n'):
                arr.append(int(item))
         
        data.append(arr)
        arr = []

init = []

#create C1
from collections import Counter

def frequenct_itemset(item_set_counter, s):
    
    for i in list(item_set_counter):
        if(item_set_counter[i] < s):
            del item_set_counter[i]
    
    return item_set_counter

def create_pairs(frequent_itemset):
    return list(it.combinations(frequent_itemset, 2))
                                    

#FOLLOWIG THE STEPS

for i in data:
    for q in i:
        if(q not in init):
            init.append(q)

init = sorted(init)

#calculating support threshold
support_threshold = 0.01
support_count = int(support_threshold*len(init))

#Creating candidate for pass 1

candidate1 = Counter()
for i in init:
    for d in data:
        #d in line
        if(i in d):
            candidate1[i]+=1


#frequent items
frequent_items = frequenct_itemset(candidate1, support_count) 

#create pair of frequent items
frequent_pairs = create_pairs(frequent_items)

#TIME TAKEN 
time_taken = time.time() - start_time
print("Time taken for running Apriori algorithm on Netflix data with 1 percent support threshold is: " + str(time_taken))
#return all the frequent pairs


f = open("apriori-netflix-1.txt", "a")
f.write("Time taken for running Apriori algorithm on Netflix data with 1 percent support threshold is: " + str(time_taken))
result_str = ','.join(str(item) for item in frequent_pairs)
f.write(result_str)
f.close()













