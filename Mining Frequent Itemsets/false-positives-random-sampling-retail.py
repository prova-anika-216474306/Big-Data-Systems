#False positives in random sampling retail dataset
#Comparing the time frequent itemsets mined with 1% threshold 
#Using PCY algorithm and random sampling 

#FOR 1% THRESHOLD
all_pairs= []
with open("pcy-retail-1.txt", "r") as f:
    next(f)
    for line in f:
        list_all = line.split("), (")
        for i in list_all: 
            all_pairs.append(i)

rs_pairs= []
with open("random-sampling-pcy-retail-1.txt", "r") as f:
    next(f)
    for line in f:
        list_all = line.split("), (")
        for i in list_all: 
            rs_pairs.append(i)

false_positives = []
for i in rs_pairs:
    if(i not in all_pairs):
        false_positives.append(i)

length_of_rs_pairs = len(rs_pairs)
print("Number Frequent Pairs in Random Sample (1% ST): " + str(length_of_rs_pairs))

length_of_false_positives = len(false_positives)
print("Number False positives in Random Sample (1% ST): " + str(length_of_false_positives))


#FOR 2% THRESHOLD  
all_pairs_2= []
with open("pcy-retail-2.txt", "r") as f:
    next(f)
    for line in f:
        list_all = line.split("), (")
        for i in list_all: 
            all_pairs_2.append(i)

rs_pairs_2= []
with open("random-sampling-pcy-retail-2.txt", "r") as f:
    next(f)
    for line in f:
        list_all = line.split("), (")
        for i in list_all: 
            rs_pairs_2.append(i)

false_positives_2 = []
for i in rs_pairs_2:
    if(i not in all_pairs_2):
        false_positives_2.append(i)

length_of_rs_pairs_2 = len(rs_pairs_2)
print("Number of Frequent Pairs in Random Sample (2% ST): " + str(length_of_rs_pairs_2))

length_of_false_positives_2 = len(false_positives_2)
print("Number of False positives in Random Sample (2% ST): " + str(length_of_false_positives_2))
