# This is my homework for Collections.

# 1. create a list of random number of dicts (from 2 to 10)
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 1. lets define number of dictionaries which we will use:
import random
import string

dictnumber = random.randint(2, 10)
print("Number of dictionaries: ", dictnumber)

# This script will create expected number of dictionaries. This number was defined earlier:
testlistkeys = random.randint(2, 10)
print("Number of elements in dictionary: ", testlistkeys)

letters = string.ascii_lowercase
keys1 = random.choices(letters, k=testlistkeys)
print(keys1)

values1 = random.sample(range(0, 100), testlistkeys)
print(values1)

# Script to create one dictionary:
dict_1 = {}
for i in range(len(keys1)):
    dict_1[keys1[i]] = values1[i]
print(dict_1)

# Let`s create a new dictionary:

list_dicts = []
for i in range(dictnumber):
    testlistkeys = random.randint(2, 10)
    print("Number of elements in dictionary: ", testlistkeys)

    letters = string.ascii_lowercase
    keys1 = random.choices(letters, k=testlistkeys)
    print(keys1)

    values1 = random.sample(range(0, 100), testlistkeys)
    print(values1)
    dict_1 = {}
    for i in range(len(keys1)):
        dict_1[keys1[i]] = values1[i]
    print(dict_1)
    list_dicts.append(dict_1)
print(list_dicts)

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

print(list_dicts[0].keys())
print(list_dicts[0].values())

masterdict = {}
lista = []
for index1 in range(len(list_dicts)):
    for el in list_dicts[index1]:
        if el not in lista:
            #continue
        #else:
            dict3 = {}
            for el2 in range(len(list_dicts)):
                if el in list_dicts[el2]:
                    dict3[el2] = list_dicts[el2][el]
            lista.append(el)
            if len(dict3) == 1:
                masterdict[el] = list_dicts[index1][el]
            else:
                x = max(dict3.values())
                y = 0
                #print(x)
                for el3 in dict3.items():
                    if el3[1] == x:
                        y = el3[0]
                masterdict[el+"_"+str(y)] = x
print(masterdict)

