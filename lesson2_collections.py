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
for i in range(dictnumber):
    name = "dict_" + str(i)
    exec(name + "={}")
    print(name, "=", eval(name))
    print(type(eval(name)))


testlistkeys = random.randint(2, 10)
print("Number of elements in dictionary: ", testlistkeys)

random.seed(10)
letters = string.ascii_lowercase
keys1 = random.choices(letters, k=testlistkeys)

print(keys1)

values1 = random.sample(range(0, 100), testlistkeys)
print(values1)

# I could not find a proper solution to populate dictionaries dynamically using loop
# so further solution is a bit separate
# We need  to populate each dictionary:
dict_1 = {}
for i in range(len(keys1)):
   dict_1[keys1[i]] = values1[i]
print(dict_1)

dict_2 = {}
for j in range(len(keys1)):
   dict_2[keys1[j]] = values1[j]
print(dict_2)

# creating a list of those dictionaries:
finallist = [dict_1, dict_2]
print(finallist)

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}

# Let`s create a new dictionary:
masterdict = {x: dict_1[x] for x in keys1}

print(masterdict)
