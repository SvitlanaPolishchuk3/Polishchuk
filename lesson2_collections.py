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
#print(list_dicts[2].items())

masterdict = {}
for dict1 in list_dicts:
    for el in dict1:
        masterdict[el] = dict1[el]

print(masterdict)

# try:
#     masterdict0 = dict.fromkeys(list_dicts[0].keys(), list_dicts[0].values())
#     masterdict1 = dict.fromkeys(list_dicts[1].keys())
#     masterdict2 = dict.fromkeys(list_dicts[2].keys())
#     masterdict3 = dict.fromkeys(list_dicts[3].keys())
#     masterdict4 = dict.fromkeys(list_dicts[4].keys())
#     masterdict5 = dict.fromkeys(list_dicts[5].keys())
#     masterdict6 = dict.fromkeys(list_dicts[6].keys())
#     masterdict7 = dict.fromkeys(list_dicts[7].keys())
#     masterdict8 = dict.fromkeys(list_dicts[8].keys())
#     masterdict9 = dict.fromkeys(list_dicts[9].keys())
#     masterdict10 = dict.fromkeys(list_dicts[9].keys())
# except:
#     pass
# try:
#     print(masterdict0)
#     print(masterdict1)
#     print(masterdict2)
#     print(masterdict3)
#     print(masterdict4)
#     print(masterdict5)
#     print(masterdict6)
#     print(masterdict7)
#     print(masterdict8)
#     print(masterdict9)
#     print(masterdict10)
# except:
#     pass
#dict(masterdict1.items() | masterdict2.items())
#print(dict)
