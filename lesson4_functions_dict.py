import random
import string


# This part is related to lesson 2:
# Let`s create a function to generate random numbers and generate "Number of dictionaries"
def func_random1():
    dictnumber = random.randint(aa, bb)
    return dictnumber


aa = 2
bb = 10
dictnumber1 = func_random1()
print("Number of dictionaries: ", dictnumber1)


elements = func_random1()


# We can create a function to generate random letters:
def func_letters():
    letters = string.ascii_lowercase
    keys1 = random.choices(letters, k=elements)
    return keys1


# For values:
def func_val():
    values1 = random.sample(range(0, 100), elements)
    return values1


# Let's create a new dictionary:
list_dicts = []
for i in range(dictnumber1):
    func_random1()
    elements = func_random1()
    func_letters()
    func_val()

    letters = string.ascii_lowercase
    keys1 = random.choices(letters, k=elements)

    func_val()
    dict_1 = {}
    for i in range(len(func_letters())):
        dict_1[func_letters()[i]] = func_val()[i]
    print(dict_1)
    list_dicts.append(dict_1)
print(list_dicts)

# 2. get previously generated list of dicts and create one common dict:
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}


def masterdict11():
    masterdict = {}
    lista = []
    for index1 in range(len(list_dicts)):
        for el in list_dicts[index1]:
            if el not in lista:
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
                    for el3 in dict3.items():
                        if el3[1] == x:
                            y = el3[0]
                    masterdict[el+"_"+str(y)] = x
    return masterdict


print(masterdict11())





