
from collections import Counter
import itertools as it
from venv import create
import time

#parsing thr Netflix dataset and storing into data array
data = []

with open("netflix.data", "r") as f:
    next(f)
    for line in f:
        arr = []
        l = line.split(" ")
        for item in l:
            if (item != '\n' and item != ''):
                arr.append(int(item))
         
        data.append(arr)
        arr = []

data_length = len(data)
data_20_percent = data[0:int(data_length*0.2)]
data_40_percent = data[0:int(data_length*0.4)]
data_60_percent = data[0:int(data_length*0.6)]
data_80_percent = data[0:int(data_length*0.8)]


def frequenct_itemset(item_set_counter, s):
    
    for i in list(item_set_counter):
        if(item_set_counter[i] < s):
            del item_set_counter[i]
    
    return item_set_counter

def create_pairs(frequent_itemset):
    return list(it.combinations(frequent_itemset, 2))
                                    

#FOLLOWIG THE STEPS
def apriori(data):
    init = []
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

    #return all the frequent pairs
    return frequent_pairs
    
#apriori on 40% of the dataset
start40 = time.time()
frequent_pairs = apriori(data_40_percent)

time_for_40_percent = time.time() - start40

print("Time taken for 40 percent of Netflix data: " + str(time_for_40_percent))

f = open("scalability-apriori-netflix-1-40.txt", "a")
f.write("Time taken for 40 percent of Netflix data: " + str(time_for_40_percent))
result_str = ','.join(str(item) for item in frequent_pairs)
f.write(result_str)
f.close()


