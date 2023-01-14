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
            


son_pairs= []
with open("SON-pcy-retail-1.txt", "r") as f:
    for line in f:
        list_all = line.split("),(")
        for i in list_all: 
            son_pairs.append(i)
          

false_positives = []
for i in son_pairs:
    if(i not in all_pairs):
        false_positives.append(i)

length_of_son_pairs = len(son_pairs)
print("Number Frequent Pairs found using SON on PCY (1% ST): " + str(length_of_son_pairs))

length_of_false_positives = len(false_positives)
print("Number False positives using SON on PCY (1% ST): " + str(length_of_false_positives))


#FOR 2% THRESHOLD  
all_pairs_2= []
with open("pcy-retail-2.txt", "r") as f:
    next(f)
    for line in f:
        list_all = line.split("),(")
        for i in list_all: 
            all_pairs_2.append(i)

son_pairs_2 = []
with open("SON-pcy-retail-2.txt", "r") as f:
    for line in f:
        list_all = line.split("),(")
        for i in list_all: 
            son_pairs_2.append(i)

false_positives_2 = []
for i in son_pairs_2:
    if(i not in all_pairs):
        false_positives_2.append(i)

length_of_son_pairs_2 = len(son_pairs_2)
print("Number Frequent Pairs found using SON on PCY (2% ST): " + str(length_of_son_pairs_2))

length_of_false_positives_2 = len(false_positives_2)
print("Number False positives using SON on PCY (2% ST): " + str(length_of_false_positives_2))