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

init = []

#create the two hash functions
def hash_function_1(value1, value2):
    return (value1^value2)%1000

def hash_function_2(itemset, num_of_buckets):
    return sum(itemset) % num_of_buckets

#define the GENERAL functions
def create_bitmap(hash_bucket, threshold):
  bit_map = []
  for key, value in hash_bucket.items():
    if value < threshold:
      bit_map.insert(key, 0)
    else:
      bit_map.insert(key, 1)

  return bit_map


def frequenct_itemset(item_set_counter):
    
    for i in list(item_set_counter):
        if(item_set_counter[i] < s):
            del item_set_counter[i]
    
    return item_set_counter

def create_pairs(frequent_itemset):
    return list(it.combinations(frequent_itemset, 2))
                                    

#FOLLOWIG THE STEPS
#creating 2 different hash_tables 
hash_buckets_table_one = {}
hash_buckets_table_two = {}

for i in data:
    for q in i:
        if(q not in init):
            init.append(q)

    
    #for each line in data, create pairs of items in each bucket: New in PCY
    pairs = list(it.combinations(i, 2))
    for pair in pairs:
        index1 = hash_function_1(pair[0], pair[1]) 
        hash_buckets_table_one[index1] = 1 if index1 not in hash_buckets_table_one else hash_buckets_table_one[index1]+1
        index2 = hash_function_2(pair, len(data))
        hash_buckets_table_two[index2] = 1 if index2 not in hash_buckets_table_two else hash_buckets_table_one[index1]+1

#init is the array of all possible items
init = sorted(init)

#calculating support threshold#calculating support threshold
support_threshold = 0.02
s = int(support_threshold*len(init))


#Creating candidate for pass 1
candidate1 = Counter()
for i in init:
    for d in data:
        #d in line
        if(i in d):
            candidate1[i]+=1


#frequent individual items that occur for more than the threshold
frequent_items = frequenct_itemset(candidate1) 

#create pair of frequent items
frequent_pairs = create_pairs(frequent_items)

#creating bitmap for the two hashtables
bitmap1 = create_bitmap(hash_buckets_table_one, s)
bitmap2 = create_bitmap(hash_buckets_table_two, s)

for pair in frequent_pairs:
    hash_value1 = hash_function_1(pair[0], pair[1])
    hash_value2 = hash_function_2(pair, len(data))
    
    if bitmap1[hash_value1] != 1 and bitmap2[hash_value2] != 1:
      frequent_pairs.remove(pair)

time_taken = time.time() - start_time

print("Time taken for running multihash algorithm (PCY) on Netflix data with 2 percent support threshold is: " + str(time_taken))

f = open("multihash-netflix-2.txt", "a")
f.write("Time taken for running multihash algorithm (PCY) on Netflix data with 2 percent support threshold is: " + str(time_taken))
result_str = ','.join(str(item) for item in frequent_pairs)
f.write(result_str)
f.close()






