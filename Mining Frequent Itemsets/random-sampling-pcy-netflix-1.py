import random
import itertools as it
from venv import create
from collections import Counter
import time

start_time = time.time()
#retail ndatatset in an array
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

#selecting k to be 50000 because the netflix file has 480000+ baskets so taking approximately 10% data in the random sample
random_sample = random.choices(data, k=50000)	
init = []

#simple hash function to find key value of a pair. 2 different pairs can produce same hash value and
#can be in same bucket
def hash(value1, value2):
    return (value1^value2)%1000

def create_bitmap(hash_bucket, threshold):
  bit_map = []
  for key, value in hash_bucket.items():
    if value < threshold:
      bit_map.insert(key, 0)
    else:
      bit_map.insert(key, 1)

  return bit_map

def frequenct_itemset(item_set_counter, s):
    
    for i in list(item_set_counter):
        if(item_set_counter[i] < s):
            del item_set_counter[i]
    
    return item_set_counter

def create_pairs(frequent_itemset):
    return list(it.combinations(frequent_itemset, 2))
                                    

#FOLLOWIG THE STEPS
#creating hash_buckets from pass 1
hash_buckets = {}

for i in random_sample:
    for q in i:
        if(q not in init):
            init.append(q)

    
    #for each line in RANDOM SAMPLE, create pairs of items in each bucket: New in PCY
    pairs = list(it.combinations(i, 2))
    for pair in pairs:
        index = hash(pair[0], pair[1]) 
        hash_buckets[index] = 1 if index not in hash_buckets else hash_buckets[index]+1

init = sorted(init)

#calculating support threshold
support_threshold = 0.01 
support_count = int(support_threshold*len(init))

#Creating candidate for pass 1

candidate1 = Counter()
for i in init:
    for d in random_sample:
        #d in line
        if(i in d):
            candidate1[i]+=1


#frequent items
frequent_items = frequenct_itemset(candidate1, support_count) 

#create pair of frequent items
frequent_pairs = create_pairs(frequent_items)

#remove pair based on bitmap binary value
bitmap = create_bitmap(hash_buckets, support_count)


for pair in frequent_pairs:
    hash_value = hash(pair[0], pair[1])
    if bitmap[hash_value] != 1:
      frequent_pairs.remove(pair)

#NUMBER OF FREQUENT PAIRS IN THE RANDOM SAMPLE
length = len(frequent_pairs)

time_taken = time.time() - start_time
#return all the frequent pairs
print("Time taken for random sampling (PCY) netflix data with 1% threshold: " + str(time_taken)) 
print(length)

f = open("random-sampling-pcy-netflix-1.txt", "a")
f.write("Time taken for random sampling (PCY) netflix data with 1% threshold: " + str(time_taken))

print(print("Time taken for random sampling (PCY) retail data with 1% threshold: " + str(time_taken)) )
#return all the frequent pairs
result_str = ','.join(str(item) for item in frequent_pairs)
f.write(result_str)
f.close()
print(length)